from __future__ import annotations

import json
import datetime
import logging

from bleak.backends.device import BLEDevice

from victron_ble.scanner import Scanner
from victron_ble.exceptions import AdvertisementKeyMissingError, UnknownDeviceError

logger = logging.getLogger(__name__)


class SKScanner(Scanner):
    def __init__(self, vesselid, device_keys: dict[str, str]=None):
        self.vesselid = vesselid
        super().__init__(device_keys)

    def callback(self, ble_device: BLEDevice, raw_data: bytes):
        logger.debug(
            f"Received data from {ble_device.address.lower()}: {raw_data.hex()}"
        )
        try:
            device = self.get_device(ble_device, raw_data)
        except AdvertisementKeyMissingError:
            return
        except UnknownDeviceError as e:
            logger.error(e)
            return
        parsed = device.parse(raw_data)

        base = f"electrical.batteries.{ble_device.name}"

        values = {
            "voltage": parsed.get_battery_voltage(),
            "temperature": parsed.get_battery_temperature() + 273,
            "balancer_status": parsed.get_balancer_status().name.lower(),
            "bms_flags": parsed.get_bms_flags(),
            "error_flags": parsed.get_error_flags(),
            "model": parsed.get_model_name(),
        }

        values.update(
            {
                f"cells.{i}.voltage": value
                for i, value in enumerate(parsed.get_cell_voltages())
                if value
            }
        )

        blob = {
            "context": self.vesselid,
            "updates": [
                {
                    "source": {
                        "label": "Victron",
                        "src": ble_device.address,
                        "type": "Bluetooth",
                    },
                    "timestamp": datetime.datetime.today().isoformat(),
                    "values": [
                        {"path": f"{base}.{key}", "value": value}
                        for key, value in values.items()
                    ],
                }
            ],
        }
        print(json.dumps(blob))

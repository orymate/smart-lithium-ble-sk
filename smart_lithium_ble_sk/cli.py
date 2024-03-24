import asyncio
import signal
import logging
from typing import List, Tuple

import click

from victron_ble.cli import DeviceKeyParam
from .scanner import SKScanner

logger = logging.getLogger("victron_ble_sk")
logging.basicConfig()

signal.signal(signal.SIGPIPE, signal.SIG_DFL)


@click.group()
@click.option("-v", "--verbose", is_flag=True, help="Increase logging output")
def cli(verbose):
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)


@cli.command(help="Forward data to signalk")
@click.argument("vesselid", type=str)
@click.argument("device_keys", nargs=-1, type=DeviceKeyParam())
def signalk(vesselid: str, device_keys: List[Tuple[str, str]]):
    """Print a stream of SignalK delta object.

    vesselid is the urn SignalK uses to identify your vessel (self doesn't seem to work).
    device_keys are a list of MAC@key pairs for the ble devices to watch.
    """
    loop = asyncio.get_event_loop()

    async def scan(keys):
        scanner = SKScanner(vesselid, keys)
        await scanner.start()

    asyncio.ensure_future(scan({k: v for k, v in device_keys}))
    loop.run_forever()


if __name__ == "__main__":
    cli()

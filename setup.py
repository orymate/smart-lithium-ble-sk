#!/usr/bin/env python

from distutils.core import setup

setup(
    name="smart_lithium_ble_sk",
    version="0.1",
    description="SmartLithium BLE-SignalK bridge",
    author="Mate Ory",
    author_email="orymate@gmail.com",
    packages=["smart_lithium_ble_sk"],
    entry_points={
        "console_scripts": ["smart_lithium_ble_sk = smart_lithium_ble_sk.cli:cli"]
    },
    install_requires=["victron-ble"],  # see README.md
)

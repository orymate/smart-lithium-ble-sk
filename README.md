## Installation

```
# required changes to upstream: https://github.com/keshavdv/victron-ble/pull/47
sudo pip install git+https://github.com/orymate/victron-ble.git@add-smart-lithium#egg=victron-ble

sudo python3 setup.py install
sudo cp ble-sk.socket ble-sk@.service /etc/systemd/system/
sudo cp env.example /etc/default/smart-lithium-ble-sk

# edit devices (see https://github.com/keshavdv/victron-ble/tree/main?tab=readme-ov-file#usage)
sudo vim /etc/default/smart-lithium-ble-sk

sudo systemctl enable --now ble-sk.socket

# test connection
nc -v localhost 1234

# set up a TCP/SignalK connection in signalK, restart

# check  status
systemctl status ble-sk@\*.service
systemctl status ble-sk.socket

```

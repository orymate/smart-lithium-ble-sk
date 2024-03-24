## Installation

```
# required changes to upstream: https://github.com/keshavdv/victron-ble/pull/47
sudo pip install git+https://github.com/orymate/victron-ble.git@add-smart-lithium#egg=victron-ble

sudo python3 setup.py install
sudo cp ble-sk.socket ble-sk@.service /etc/systemd/system/
sudo cp env.example /etc/default/smart-lithium-ble-sk

sudo adduser ble-sk --ingroup bluetooth --disabled-password

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

## NodeRed dashboard example

![image](https://github.com/orymate/smart-lithium-ble-sk/assets/207816/9a06fa2c-c885-4ae9-9e86-0665e4f839e8)
![image](https://github.com/orymate/smart-lithium-ble-sk/assets/207816/71d12300-6618-4742-ab38-915aa8f27a31)
[flows.1.json](examples/flows.1.json)

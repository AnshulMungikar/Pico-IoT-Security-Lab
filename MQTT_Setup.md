# MQTT Setup Guide

## Prerequisites
- Raspberry Pi Pico W with MicroPython
- USB cable
- Fedora/Linux machine (Main Workstation)
- Secondary machine acting as MQTT broker (Proxmox VM/Container)

## How MQTT Works
<img width="1326" height="968" alt="mqtt-protocol-0-1653507626" src="https://github.com/user-attachments/assets/6f147a0a-e2c7-490b-b4c6-94db20ce4fce" />

### MQTT Broker (Secondary Machine)
1. It acts like a central hub for the system
2. Receives all messages from publishers.
3. Filters messages and sends them to the correct subscribers according to the topic name.

### MQTT Publisher (Pico)
1. Creates and sends data (messages).
2. Assigns a topic name to every message it sends which is further used by Broker to sort the data.
3. Connects to the broker only long enough to send the message to save battery power and resources.

### MQTT Subscriber(Main Workstation)
1. Listens for data by telling the broker what topics it wants.
2. Receives any message published to its chosen topics.
3. Can subscribe to multiple topics at the same time.
4. Stays connected to the broker to get real-time updates.


## Steps

### 1. Set up MQTT broker on the secondary machine

Install Mosquitto:
```bash
apt install mosquitto mosquitto-clients -y
```

Start the service:
```bash
sudo systemctl start mosquitto
```

Check for errors:
```bash
sudo systemctl status mosquitto
```

Edit the config file to allow incoming connections:
```bash
/etc/mosquitto/mosquitto.conf
```

Add these lines:
``` 
listener 1883
allow_anonymous true
```

Restart the service:
```bash
sudo systemctl restart mosquitto
```

### 2. Install MQTT client tools on the main workstation

```bash
sudo dnf install mosquitto
```

### 3. Test the connection between broker and workstation

Open terminal 1 and subscribe:
```bash
mosquitto_sub -h <broker-ip> -t 'picosense/01/#' -v
```

Open terminal 2 and publish a test message:
```bash
mosquitto_pub -h <broker-ip> -t 'picosense/01/telemetry' -m 'test'
```

You should see `test` appear in terminal 1.

### 4. Install MQTT library on the Pico

Run this once in the MicroPython REPL:
```python
import mip
mip.install('umqtt.simple')
```

Test publishing from the Pico:
```python
from umqtt.simple import MQTTClient
client = MQTTClient('picosense-01', '<broker-ip>', port=1883)
client.connect()
client.publish('picosense/01/telemetry', 'hello from pico')
```

You should see `hello from pico` appear in the subscriber terminal.

### 5. Run the full firmware

Run `firmware/main.py` on the Pico. 
Telemetry will publish to `picosense/01/telemetry` every 10 seconds.

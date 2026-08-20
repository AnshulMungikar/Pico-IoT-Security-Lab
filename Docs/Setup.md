# Setup Guide

## Prerequisites
- Raspberry Pi Pico W
- USB cable
- Fedora/Linux machine
- Thonny installed

### 1. Flash MicroPython
Flash MicroPython onto the Pico W using Thonny.

### 2. Install screen
```
sudo dnf install screen
```

### 3. Fix serial port permissions
The device appears as `/dev/ttyACM0` and is owned by the `dialout` group.

Note: `chmod` does not work permanently here because `/dev/` device files are recreated by the kernel every time the device is plugged in.

The correct fix is to add your current user to the `dialout` group:
```
sudo usermod -a -G dialout your-username
```
Then reboot main machine for the change to take effect.

### 4. Close Thonny
Thonny holds the serial port open. If it is running, screen will get a "device busy" error. Close Thonny before connecting.

### 5. Connect via screen
```
screen /dev/ttyACM0 115200
```
You should see the MicroPython REPL:
```
>>>
```

### 6. Flash boot.py to the Pico
Open Thonny and create a new file.
Copy the contents of boot.py into it.
Replace WifiPassword with your real Wi-Fi credentials.
Save it to the Pico as boot.py.

### 7. Verify Wi-Fi connection
Reboot the Pico by unplugging the pico.
Connect via screen to see the IP address:
```
screen /dev/ttyACM0 115200
```
Then type:
```
wlan.ifconfig()
```
You should see an IP address like 192.168.1.xxx.

### 8. Confirm from Fedora
Open a new terminal and run:
```
ping 192.168.1.xxx
```
You should see `64 bytes from 192.168.1.xxx: icmp_seq=2 ttl=255 time=34.3 ms`

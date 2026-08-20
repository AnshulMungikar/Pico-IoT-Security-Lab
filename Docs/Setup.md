# Setup Guide

### 1. Flash MicroPython
Flash MicroPython onto the Pico W using Thonny.

### 2. Install screen
```

sudo dnf install minicom

```

### 3. Fix serial port permissions
The device appears as `/dev/ttyACM0` and is owned by the `dialout` group.

Note: `chmod` does not work permanently here because `/dev/` device files are recreated by the kernel every time the device is plugged in.

The correct fix is to add your current user to the `dialout` group:
```

sudo usermod -a -G dialout your-username

```
Then reboot main mahine for the change to take effect.

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

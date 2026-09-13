# Finding: PICO-FW-001

## Issue:
The person who gets access to the firmware can view the wifi ssid and password stored as plain text on the device.

## Impact:
A person with the Pico’s firmware can view the wifi ssid and password.

## Root cause:
There is no encryption while storing the wifi ssid and password.

## Remediation:
We can use standard encryption for storing wifi password but the decryption key will be stored on the device and an attacker with hardware access can easily decrypt the device. In production IoT devices, a dedicated secure element hardware (like ATECC608) is used for credential storage. On the Pico W, such device is not there.

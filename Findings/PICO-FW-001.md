# Finding: PICO-FW-001

## Issue:
The person who gets access to the firmware can view the wifi ssid and password stored as plain text on the device.

## Impact:
A person with the pico’s firmware can view the wifi ssid and password.

## Root cause:
There is no encryption while storing the wifi ssid and password.

## Remediation:
Encrypting the wifi ssid and password. 


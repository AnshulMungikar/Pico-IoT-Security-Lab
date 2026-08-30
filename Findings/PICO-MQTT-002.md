# Finding: PICO-MQTT-002

## Issue:
Anyone can spy on the data being sent. 

## Impact:
The attacker can see the sensitive data being sent.
## Root cause:
There is no encryption while sending the data to the broker or subscriber.

## Remediation:
Encrypting the messages before sending them. We can use TLS on port 8883, which encrypts the data in transit.


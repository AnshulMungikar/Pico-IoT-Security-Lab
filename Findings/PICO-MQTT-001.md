# Finding: PICO-MQTT-001

## Issue:
Anyone can act as the pico and send messages acting like the pico.

## Impact:
An attacker could send fake messages to the broker with will in turn send the fake message to the subscribers.

## Root cause:
There is no verification by the broker of who is sending the messages.

## Remediation:
Only make the broker accept messages from devices with a verified username and password.

## Evidence:

Method:
```
mosquitto_pub -h <Broker-IP> -t 'picosense/01/command' -m '{"command": "LED_ON"}'
```

Result:
```
LED turns on.
```

Conclusion: Messages can be sent without any authentication required.

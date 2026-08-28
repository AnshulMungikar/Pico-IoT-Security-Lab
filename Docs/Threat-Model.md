# Threat Model

## Attacker Profile  

- Anyone with physical or network access to the device
- Low to intermediate skill level — attacks require only basic Linux knowledge and common tools
- Motivation — unauthorized control or data access

## Attacker Capabilities  

- Network access: YES
- Device credentials: NO
- Physical device: YES
- Firmware image: YES
- Local Linux machine: YES

## Attacker Objectives   

1. Read device information
2. Change configuration
3. Send unauthorized commands
4. Impersonate the device
5. Modify MQTT traffic
6. Extract secrets from firmware

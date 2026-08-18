# PicoSense
A minimal IoT weather station built on the Raspberry Pi Pico W for learning embedded systems, Wi-Fi networking, HTTP APIs, MQTT, Linux infrastructure.

## What is PicoSense?

PicoSense is an IoT device built on Raspberry Pi Pico W.

The goal is to build a device that can eventually:
- Measure temperature
- Measure ambient light
- Report device status
- Report uptime
- Report firmware version
- Identify itself with a unique device ID
- Accept commands
- Connect to Wi-Fi
- Expose a small HTTP API
- Publish telemetry using MQTT
- Receive commands over MQTT
- Communicate securely using TLS

## Tech Stack
### Hardware
- Raspberry Pi Pico W
- BH1750 (ambient light sensor)

### Software
- MicroPython

### Infrastructure
- Linux(Fedora) as main machine.

## Roadmap

- [ ] **Phase 0:** Hardware selection & architecture specification
- [ ] **Phase 1:** Firmware base, Wi-Fi connectivity, and serial debugging
- [ ] **Phase 2:** Local HTTP REST API 
- [ ] **Phase 3:** Integration with MQTT broker for telemetry pub/sub

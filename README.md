# Pico IoT Security Lab

This is an isolated IoT security research testbed based on the Raspberry Pi Pico W. This project simulates an IoT device to evaluate attack surfaces, capture network traffic, and test hardening strategies across HTTP, MQTT.


## Summary

The primary objective of this project is to learn embedded security methodology from an attacker and defense perspective. I use this project as a learning experience for IoT security concepts by investigating credential exposure, plaintext telemetry, and unauthenticated commands.
* **Hardware Target**: Raspberry Pi Pico W running MicroPython firmware.
* **Infrastructure**: LAN, Proxmox VM hosting Mosquitto MQTT broker, Fedora Linux workstation.

## Lab Architecture
                        ┌─────────────────────────┐
                        │ Fedora Workstation      │
                        │ (Analyst)               │
                        └────────────-────────────┘
                                     │
                               Wi-Fi / LAN
                    HTTP             │
            ┌─────────➤──────────────▲────────────────────────┐
            │                                                 │
    ┌───────▼────────────────┐               ┌────────────────▼───────────────┐
    │ Pico W Target          │     MQTT      │ Proxmox VM                     │
    │ - HTTP API             ├───────────────► Mosquitto MQTT Broker          │
    │ - Telemetry Publisher  │               │ Logging & Security Controls    │
    └────────────────────────┘               └────────────────────────────────┘



Detailed architectural diagrams and interface specifications can be found in [`Docs/architecture.md`](Docs/architecture.md).

## Findings & Vulnerability Index

Each vulnerability identified in this testbed is documented with root-cause analysis and remediation steps:

| Finding ID | Vulnerability Focus | Document Link |
| :--- | :--- | :--- |
| **PICO-FW-001** | Credential Exposure | [`PICO-FW-001.md`](Findings/PICO-FW-001.md) |
| **PICO-HTTP-001** | Information readable without authentication | [`PICO-HTTP-001.md`](Findings/PICO-HTTP-001.md) |
| **PICO-HTTP-002** | Input Validation | [`PICO-HTTP-002.md`](Findings/PICO-HTTP-002.md) |
| **PICO-HTTP-003** | Unauthenticated command execution | [`PICO-HTTP-003.md`](Findings/PICO-HTTP-003.md) |
| **PICO-MQTT-001** | Missing Broker Access Control Lists | [`PICO-MQTT-001.md`](Findings/PICO-MQTT-001.md) |
| **PICO-MQTT-002** | Plaintext Message Transmission | [`PICO-MQTT-002.md`](Findings/PICO-MQTT-002.md) |


---

## Project Structure & Documentation

* [`Docs/Setup.md`](Docs/Setup.md): Instructions for setting up the hardware, VM, and isolated network.
* [`Docs/Threat-Model.md`](Docs/Threat-Model.md): Attacker profiles, boundaries, and objective definitions.
* [`Docs/api.md`](Docs/api.md): Endpoint descriptions for both vulnerable and hardened device versions.
* [`Docs/MQTT_Setup.md`](Docs/MQTT_Setup.md): Broker configuration, access rules, and TLS setup.
* [`Debugging/MQTT.md`](Debugging/MQTT.md): Hardware, serial console, and broker troubleshooting notes.

---

## Security Testing
Automated test scripts are in `scripts/`:
- `test_http.sh` — tests HTTP authentication
- `test_mqtt.sh` — tests MQTT authentication and TLS

---

## Branches
- `main` — documentation and findings
- `vulnerable` — deliberately vulnerable firmware
- `secure` — hardened firmware and testing scripts

---

## Skills Demonstrated
- Embedded systems programming (MicroPython)
- Network security analysis (Wireshark, MQTT, HTTP)
- Linux systems administration (Fedora, Debian, Proxmox)
- Security research methodology (threat modeling, vulnerability documentation)
- Automation (bash scripting, automated security testing)
- TLS (certificate generation, encrypted communications)

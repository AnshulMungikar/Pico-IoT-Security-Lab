# PicoSense API Reference

Base URL: `http://<pico-ip>`



## GET /status
Returns current device information.

**Example:**
```
curl http://<pico-ip>/status
```
**Response:**
```
{"device": "picosense", "uptime": 1448, "Temperature": 28.9}
```



## GET /config
Returns the current telemetry interval.

**Example:**
```
curl http://<pico-ip>/config
```
**Response:**
```
{"Interval": 10}
```



## POST /config
Updates the telemetry interval.

**Example:**
```
curl -X POST http://<pico-ip>/config -d '{"interval": 30}'
```
**Response:**
```
{"Interval": 30}
```



## POST /command
Controls the device. Accepted commands: `LED_ON`, `LED_OFF`, `REBOOT`.

**Example:**
```
curl -X POST http://<pico-ip>/command -d '{"command": "LED_ON"}'
```
**Response:**
```
{"status": "LED on"}
```

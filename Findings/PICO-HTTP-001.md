# Finding: PICO-HTTP-001

## Issue

Device information readable without authentication

## Impact

Sensitive data like temperature, uptime exposed to anyone on network

## Root cause

No authentication on GET /status

## Remediation

Require authentication to access device data

## Evidence

**Method:**
```bash
curl http://<pico_ipaddr>/status
```

**Result:**
```json
{"uptime": 80215, "device": "picosense-01", "Temperature": 32.193984}
```

**Conclusion:** Device information returned without any authentication required.

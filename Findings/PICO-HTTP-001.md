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
### **Method 1 - Direct request:**

**Method:**
```bash
curl http://<pico_ipaddr>/status
```

**Result:**
```json
{"uptime": 80215, "device": "picosense-01", "Temperature": 32.193984}
```

### **Method 2 - Passive capture:**
Method: Captured network traffic using Wireshark on Fedora.
 - Interface: enp5s0
 - Filter: ip.addr == <PICO_IP>

Result: The following data was visible in plaintext:

   - HTTP request and the data send to the http request sender.

Screenshots:
![HTTP_status_capture](./Screenshots/HTTP_STATUS_WIRESHARK.png)

## **Conclusion:** 
While device data is accessible via curl to anyone on the network, Wireshark demonstrates that even a passive observer — without making any requests — can intercept and read all HTTP traffic including device telemetry.



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

## Remediation Applied
HTTP Basic Authentication implemented (in the secure branch). Requests without valid credentials now receive a 401 Unauthorized response.

Verified:
- Without credentials: 401 Unauthorized
<img width="525" height="72" alt="image" src="https://github.com/user-attachments/assets/b5f4e831-e661-4bd4-bf90-e817c4330621" />

- With credentials: 200 OK
<img width="1632" height="110" alt="image" src="https://github.com/user-attachments/assets/06146a0a-5c62-442c-a475-42d71edd8449" />


## **Conclusion:** 
While device data is accessible via curl to anyone on the network, Wireshark demonstrates that even a passive observer — without making any requests — can intercept and read all HTTP traffic including device telemetry.



# Finding: PICO-HTTP-003

## Issue:

Unauthenticated command execution via HTTP API

## Impact: 

Anyone can execute device commands like LED_ON, LED_OFF, or REBOOT without authentication

## Root cause: 

No authentication on the POST /command endpoint

## Remediation: 

Add authentication so only authorized users can execute commands

## Evidence:

Method:
```
curl -X POST http://<pico-ip>/command -d '{"command": "LED_ON"}'
```

Result:
```
{"status": "LED on"}
```
## Remediation Applied
HTTP Basic Authentication implemented. Requests without valid 
credentials now receive a 401 Unauthorized response.

Verified:
- Without credentials: 401 Unauthorized
- With credentials: 200 OK
<img width="1918" height="194" alt="image" src="https://github.com/user-attachments/assets/e5b7e8d1-8c9c-4bfe-90aa-cb00fe2b65b3" />


## **Conclusion:**
Commands can be run without any authentication required, but with authentication in place they can not be run. 

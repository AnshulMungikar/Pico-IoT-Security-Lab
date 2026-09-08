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

Conclusion: commands can be run without any authentication required.

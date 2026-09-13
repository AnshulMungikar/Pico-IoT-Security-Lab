# Finding: PICO-HTTP-002

## Issue:
We are able to change the config endpoint via curl.

## Impact:
The interval value can be altered, allowing an attacker to set it to an extreme value, either causing the device to publish data so rapidly that it crashes or so infrequently that monitoring becomes ineffective.

## Root cause:
There is no authentication for the HTTP request sender.

## Remediation:
Create authentication such that only the person authorised can change the data.

## Evidence

**Method:**
```bash
curl -X POST http://<pico-ip>/config -d '{"interval": 30}'
```

**Result:**

```json
{"Interval": 30}
```

## Remediation Applied
HTTP Basic Authentication implemented. Requests without valid credentials now receive a 401 Unauthorized response.

Verified:
- Without credentials: 401 Unauthorized
- With credentials: 200 OK
<img width="1926" height="232" alt="image" src="https://github.com/user-attachments/assets/58faec82-c2e4-43f8-a475-ff738e9ac942" />


## **Conclusion:** 
Device information can not be changed without any authentication.

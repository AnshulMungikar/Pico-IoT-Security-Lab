# Finding: PICO-HTTP-003

## Issue:
We are able to send commands to the Pico via the HTTP API.

## Impact:
Any user can send commands to the Pico, which may result in unauthorized command execution.

## Root cause:
There is no authentication for the HTTP request sender.

## Remediation:
Create authentication such that only the person authorised can change the data.


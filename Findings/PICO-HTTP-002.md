# Finding: PICO-HTTP-002

## Issue:
We are able to change the config endpoint via curl.

## Impact:
The interval value can be altered, allowing an attacker to set it to an extreme value, either causing the device to publish data so rapidly that it crashes or so infrequently that monitoring becomes ineffective.

## Root cause:
There is no authentication for the HTTP request sender.

## Remediation:
Create authentication such that only the person authorised can change the data.


# Debugging: HTTP and MQTT Concurrency

## Problem
The device could not run the HTTP server and MQTT publisher simultaneously.

## What I Tried First
Two separate `while True` loops — one for HTTP and one for MQTT. This failed because the first loop never terminates, so the second loop never executes.

## Solution
Used `s.settimeout(1)` combined with `try/except` to allow both services to share a single loop.

## How It Works
1. `settimeout(1)` — makes `s.accept()` give up after 1 second if no HTTP request arrives
2. `s.accept()` raises `OSError` when it times out
3. `try/except OSError` — catches the error so the program doesn't crash
4. `pass` — does nothing; execution continues to the MQTT publish below

## What I Learned
`try/except` allows a program to handle errors gracefully instead of crashing. In embedded systems, this pattern is useful as waiting for infinite amount of time for something to happen is not affordable as the device has to do multiple things.

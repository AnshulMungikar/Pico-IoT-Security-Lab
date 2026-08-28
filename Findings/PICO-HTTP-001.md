# Finding: PICO-HTTP-001

## Issue

Anyone can send data to and from the pico via the HTTP API.

## Impact

An attacker can send unwanted commands to the pico and tap into the communication between the pico and its users using the Wireshark tool.

## Root cause

The cause is that there is no authentication between pico and the user sending and receiving data, meaning any person connected to the network can send and receive commands.

## Remediation

To prevent such attacks, we can add authentication (such as asking for a password) such that only the users who know the password can receive and send the commands. One further addition we can do is that creating two different passwords like one for only receiving messages and the other for only sending commands.

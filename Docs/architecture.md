# PicoSense Architecture

## Overview
Pico W is an IoT device that:
- connects to Wi-Fi
- publishes telemetry using MQTT
- exposes a small HTTP API
- receives commands
    

## System Diagram
       +--------------------+
       |       Fedora       |
       | Machine(subscriber)|
       +----+----------+----+
            |          |
       HTTP |          | MQTT
            |          v
            |     +----------------------+
            |     | Debian Server(Broker)|
            |     +----------+-----------+
            |                ^
            v                | MQTT
       +----+----------------+-----+
       |            PICO           |
       |(HTTP Server, MQTT Pub/Sub)|
       +---------------------------+



## Components


### Fedora Workstation
This is the main workstation which acts like testing, coding ground and a subscriber(for MQTT). 

### Pico W
This is the device that hosts the HTTP API and acts as an MQTT client

### Debian Server (MQTT Broker)
This acts like a the middleman for the MQTT protocol. All the messages are sent here and then it reroutes the messages according to the topic name to the respective devices. 

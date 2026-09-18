#!/bin/bash

# Test 1: Check if MQTT server is allowing requests without authentication
mosquitto_pub -h $PICO_IP  -p 8883 --cafile ca.crt --insecure -t 'picosense/01/command' -m '{"command": "LED_ON"}'
if [ "$?" == "0" ]; then
    echo "[FAIL] Test 1: MQTT server is allowing requests without authentication."
else
    echo "[PASS] Test 1: MQTT server is rejecting requests without authentication."
fi

# Test 2: Check if MQTT server is allowing requests with authentication
mosquitto_pub -h <broker_ip> -p 8883 --cafile ca.crt --insecure -u '<mqtt_username>' -P '<mqtt_password>' -t 'picosense/01/command' -m '{"command": "LED_ON"}'
if [ "$?" == "0" ]; then
    echo "[PASS] Test 2: MQTT server is accepting requests with authentication."
else
    echo "[FAIL] Test 2: MQTT server is rejecting requests with authentication OR Incorrect username and password."
fi


# Test 3: Check if MQTT server is allowing requests without encryption
mosquitto_pub -h <broker_ip> -p 1883 -u '<mqtt_username>' -P '<mqtt_password>' -t 'picosense/01/command' -m '{"command": "LED_ON"}'
if [ "$?" == "0" ]; then
    echo "[FAIL] Test 3: MQTT server is allowing requests without encryption."
else
    echo "[PASS] Test 3: MQTT server is rejecting requests without encryption."
fi

# Test 4: Check if MQTT server is allowing requests with encryption
mosquitto_pub -h <broker_ip> -p 8883 --cafile ca.crt --insecure -u '<mqtt_username>' -P '<mqtt_password>' -t 'picosense/01/command' -m '{"command": "LED_ON"}'
if [ "$?" == "0" ]; then
    echo "[PASS] Test 4: MQTT server is accepting requests with encryption."
else
    echo "[FAIL] Test 4: MQTT server is rejecting requests with encryption OR Incorrect username and password."
fi

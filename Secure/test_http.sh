#!/bin/bash

# Define variables for the Pico W IP address, username, and password
PICO_IP="<PICO_IP>"
USERNAME="<HTTP_User>"
PASSWORD="<HTTP_password>"


# Test 1: Check if the HTTP server is rejecting requests without authentication
result_no_auth=$(curl -s -o /dev/null -w "%{http_code}" http://$PICO_IP/status)
if [ "$result_no_auth" == "401" ]; then
    echo "[PASS] Test 1: Server is rejecting requests without authentication."
elif [ "$result_no_auth" == "200" ]; then
    echo "[FAIL] Test 1: Server is allowing requests without authentication."
else
    echo "Error occured: $result_no_auth"
fi

# Test 2: Check if the HTTP server is accepting requests with authentication
result_with_auth=$(curl -s -o /dev/null -w "%{http_code}" -u $USERNAME:$PASSWORD http://$PICO_IP/status)
if [ "$result_with_auth" == "200" ]; then
    echo "[PASS] Test 2: Server is accepting requests with authentication."
elif [ "$result_with_auth" == "401" ]; then
    echo "[FAIL] Test 2: Server is rejecting requests with authentication OR Incorrect username and password."
else
    echo "Error occured: $result_with_auth"
fi


# Test 3: Check if the HTTP server is rejecting configuration changes without authentication
change_config0=$(curl -s -o /dev/null -w "%{http_code}" -X POST http://$PICO_IP/config -d '{"interval": 30}')
if [ "$change_config0" == "401" ]; then
    echo "[PASS] Test 3: Server is not accepting configuration changes without authentication."
elif [ "$change_config0" == "200" ]; then
    echo "[FAIL] Test 3: Server is accepting configuration changes without authentication."
else
    echo "Error occured: $change_config0"
fi

# Test 4: Check if the HTTP server is accepting configuration changes with authentication
change_config1=$(curl -s -o /dev/null -w "%{http_code}" -u $USERNAME:$PASSWORD  -X POST http://$PICO_IP/config -d '{"interval": 30}')
if [ "$change_config1" == "200" ]; then
    echo "[PASS] Test 4: Server is accepting configuration changes with authentication."
elif [ "$change_config1" == "401" ]; then
    echo "[FAIL] Test 4: Server is rejecting configuration changes with authentication OR Incorrect username and password."
else
    echo "Error occured: $change_config1"
fi


# Test 5: Check if the HTTP server is rejecting command execution without authentication
execute_command0=$(curl -s -o /dev/null -w "%{http_code}" -X POST http://$PICO_IP/command -d '{"command": "LED_ON"}')
if [ "$execute_command0" == "200" ]; then
    echo "[FAIL] Test 5: Server is accepting command execution without authentication."
elif [ "$execute_command0" == "401" ]; then
    echo "[PASS] Test 5: Server is rejecting command execution without authentication."
else
    echo "Error occured: $execute_command0"
fi

# Test 6: Check if the HTTP server is accepting command execution with authentication
execute_command1=$(curl -s -o /dev/null -w "%{http_code}" -u $USERNAME:$PASSWORD  -X POST http://$PICO_IP/command -d '{"command": "LED_ON"}')
if [ "$execute_command1" == "200" ]; then
    echo "[PASS] Test 6: Server is accepting command execution with authentication."
elif [ "$execute_command1" == "401" ]; then
    echo "[FAIL] Test 6: Server is rejecting command execution with authentication OR Incorrect username and password."
else
    echo "Error occured: $execute_command1"
fi

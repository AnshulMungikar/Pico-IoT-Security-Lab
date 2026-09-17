import network
import socket
import json
import time
from machine import ADC
from time import sleep
from machine import Pin
import machine
from umqtt.simple import MQTTClient
import binascii
import ssl


# led config
led = Pin("LED", Pin.OUT)


interval = 10
config_response = json.dumps({"Interval": interval})


#CPU Temperature
sensor_temp = ADC(4)
conversion_factor = 3.3 / 65535
reading = sensor_temp.read_u16() * conversion_factor
temperature = 27 - (reading - 0.706) / 0.001721
response = json.dumps({"device": "picosense-01", "uptime": time.ticks_ms() // 1000, "Temperature": temperature})


# Connect to WiFi
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)
print('Listening on port 80')


#MQTT setup
client = MQTTClient('test', '192.168.1.127', port=8883, 
                    user='admin', password='<MQTT_password>',
                    ssl=True, 
                    ssl_params={"server_hostname": "<Broker_IP>"})
client.connect()
client.publish('picosense/01/telemetry', response)


#MQTT recieve command
def mqtt_callback(topic, msg):
        data1 = json.loads(msg)
        command = data1['command']
        if command == "LED_ON":
            led.on()
            print("LED turned on")
        elif command == "LED_OFF":
            led.off()
            print("LED turned off")
        elif command == "REBOOT":
            machine.reset()
            print("Device rebooting")

client.set_callback(mqtt_callback)
client.subscribe('picosense/01/command')


# For HTTP check if the password is correct or not
def check_auth(request):
    if b"Authorization" not in request:
        return False
    encoded = request.split(b'Basic ')[1].strip()
    decoded = binascii.a2b_base64(encoded)
    credentials = decoded.decode('utf-8')
    user, password = credentials.split(':')
    return user == "admin" and password == "admin"



s.settimeout(1)
while True:
    try:
        conn, addr = s.accept()
        request = conn.recv(1024)


        if not check_auth(request):
            conn.send('HTTP/1.1 401 Unauthorized\r\nWWW-Authenticate: Basic realm="PicoSense"\r\nContent-Type: text/plain\r\n\r\nUnauthorized')
            conn.close()
            continue

        if b"status" in request:
            print(request)
            conn.send('HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n' + response)


        elif b"config" in request and b"POST" in request:
            body = request.split(b'\r\n\r\n')[1]
            data = json.loads(body)
            interval = data['interval']
            config_response = json.dumps({"Interval": interval})
            print(interval)
            conn.send('HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n' + config_response)
        
        elif b"POST" in request and b"/command" in request:
            body = request.split(b'\r\n\r\n')[1]
            data = json.loads(body)
            command = data['command']
            if command == "LED_ON":
                led.on()
                conn.send('HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{"status": "LED on"}')
            elif command == "LED_OFF":
                led.off()
                conn.send('HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{"status": "LED off"}')
            elif command == "REBOOT":
                conn.send('HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nRebooting')
                machine.reset()
            else:
                conn.send('HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nwrong command')
        elif b"config" in request:
            print(interval)
            conn.send('HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n' + config_response)    

        elif b"command" in request:
            conn.send('HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{"commands": ["LED_ON", "LED_OFF", "REBOOT"]}')
            print("hello")

        else:
            conn.send('HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\nNot Found')
            
        conn.close()
    
    except OSError:
        pass
        
    sensor_temp = ADC(4)
    conversion_factor = 3.3 / 65535
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721
    response = json.dumps({"device": "picosense-01", "uptime": time.ticks_ms() // 1000, "Temperature": temperature})
    client.publish('picosense/01/telemetry', response)
    client.check_msg()
    sleep(1)

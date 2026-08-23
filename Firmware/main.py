import network
import socket
import json
import time
from machine import ADC
from time import sleep
from machine import Pin
import machine
from umqtt.simple import MQTTClient


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


#MQTT
client = MQTTClient('picosense-02', '192.168.1.127', port=1883)
client.connect()
client.publish('picosense/01/telemetry', response)






s.settimeout(1)
while True:
    try:
        conn, addr = s.accept()
        request = conn.recv(1024)

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
    sleep(10)

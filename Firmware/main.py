import network
import socket
import json
import time
from machine import ADC
from time import sleep

sensor_temp = ADC(4)
conversion_factor = 3.3 / 65535

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('Listening on port 80')

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721
    response = json.dumps({"device": "picosense-01", "uptime": time.ticks_ms() // 1000, "Temperature": temperature})
    print(response)
    conn, addr = s.accept()
    request = conn.recv(1024)
    if b"status" in request:
        print(request)
        conn.send('HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n' + response)
    else:
        conn.send('HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\nNot Found')
    conn.close()

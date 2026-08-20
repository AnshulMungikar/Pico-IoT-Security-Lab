import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Wifi-SSID", "Wifi-Password")
while not wlan.isconnected():
    print("Connecting to wifi")
print(wlan.ifconfig())

import socket

UDP_IP = "192.168.10.1" # tello's address when connecting to its own Wi-Fi
UDP_PORT = 8889


print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

MESSAGE = b"command"
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
print("message: %s" % MESSAGE)

MESSAGE = b"ap Your-WiFi-Network Your-WiFi-Password"
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
print("message: %s" % MESSAGE)

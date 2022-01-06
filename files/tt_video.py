import socket
import os

# send

UDP_IP = "192.168.0.36" # change to tello's address in your own local Wi-Fi network
UDP_PORT = 8889
MESSAGE = b"command"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

MESSAGE = b"streamon"
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
print("message: %s" % MESSAGE)

os.system('ffplay -probesize 32 -i udp://@:11111 -framerate 30')

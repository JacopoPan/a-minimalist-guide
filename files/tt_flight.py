import time
import socket


UDP_IP = "192.168.0.36" # change to tello's address in your own local Wi-Fi network
UDP_PORT = 8889


print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

MESSAGE = b"command"
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
print("message: %s" % MESSAGE)

time.sleep(1)

MESSAGE = b"takeoff"
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
print("message: %s" % MESSAGE)

time.sleep(3)

MESSAGE = b"flip l"
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
print("message: %s" % MESSAGE)

time.sleep(3)

MESSAGE = b"flip r"
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
print("message: %s" % MESSAGE)

time.sleep(2)

MESSAGE = b"land"
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
print("message: %s" % MESSAGE)

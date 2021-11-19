> A minimalist guide to  a few frameworks⁠—on Ubuntu and Vector computing⁠—for the person who was born yesterday
>> By a novice for the novice

# Part 7 - Heterogeneous Multirobot Teams with the RoboMaster SDK

The following instructions are for macOS Big Sur (11.6.1) on a 2020 Intel MacBook Pro

Everything after a `$` is entered on a terminal; everything after `>>>` is passed to a Python interpreter

## RoboMaster SDK Installation

```
conda create -n robomaster python=3.7
conda activate robomaster
pip3 install robomaster
pip3 install myqr
pip3 install netifaces
pip3 install netaddr
```

## S1 Connection

Download [`robomaster-s1-connect.py`](https://github.com/JacopoPan/a-minimalist-guide/blob/master/files/robomaster-s1-connect.py), set WiFi name and password
```
python3 robomaster-s1-connect.py  # Set
```
Set the slider on the side of the intelligent controller to "Router Connection" and click the "Connect" button besides it

Display the generated QR code to the S1 camera

## Tello UDP Control

```
brew install packetsender
```

Follow these steps
- Launch `PacketSender` 
- Set "Address" to 192.168.10.1, "Port" to "8889"
- Open "packetsender" -> "Preferences" -> "Network" -> "Basics"
- Check "Enable UDP Servers", set "UDP Server Ports" to "8890"
- Go back to `PacketSender`' interface, write command `command` in the "ASCII" field and click "Send"
- The Tello starts returning telemetry
- To use a router connection, send command `ap Your-WiFi-Network Your-WiFi-Password`
- Turn off the Tello Talent
- Set the TT to "Station Mode" (i.e. the up position of the slider on the right side of the open-source controller/dot-matrix display)
- Turn on the Tello Talent, it will connect to your WiFi
- Launch `PacketSender`, again
- Change "Address" to any address the TT took on your network (e.g., 192.168.0.xx)
- Write command `command` in the "ASCII" field and click "Send"
- The Tello starts returning telemetry
- Send the `takeoff` command


-------
> Work carried out @ University of Toronto's [Dynamic Systems Lab](https://github.com/utiasDSL) / [Vector Institute](https://github.com/VectorInstitute) / [Mitacs Elevate](https://www.mitacs.ca/en/projects/multi-agent-reinforcement-learning-decentralized-uavugv-cooperative-exploration)


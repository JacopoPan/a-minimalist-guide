> A minimalist guide to  a few frameworks⁠—on Ubuntu and Vector computing⁠—for the person who was born yesterday
>> By a novice for the novice

# Part 7 - Heterogeneous Multirobot Teams with the RoboMaster SDK

The following instructions are for macOS Big Sur (11.6.1) on a 2020 Intel MacBook Pro

Everything after a `$` is entered on a terminal; everything after `>>>` is passed to a Python interpreter

## RoboMaster SDK

### Installation

```
conda create -n robomaster python=3.7
conda activate robomaster
pip3 install myqr netifaces netaddr
pip3 install robomaster                   # Also see source at https://github.com/dji-sdk/RoboMaster-SDK.git 
```

### Using the RoboMaster SDK (with a small hack)

At the time of writing (January 2022), using the [RoboMaster SKD](https://github.com/dji-sdk/RoboMaster-SDK) with the S1 still requires a workaround ([forum thread](https://forum.dji.com/forum.php?mod=viewthread&tid=212767), [instructions](https://github.com/JacopoPan/a-minimalist-guide/blob/master/files/s1_sdk_hack.zip))

<!--
[alternative](https://github.com/JacopoPan/a-minimalist-guide/blob/master/files/s1_sdk_hack_2.zip)
-->

> All credit to [Bruno Albuquerque](https://github.com/brunoga)

Install and run `adb` on macOS
```
$ brew install android-platform-tools
```

Connect to the RoboMaster Intelligent Controller's (the one on top of the robot's turret) microUSB port (besides the Wi-Fi/AP switch)

Run the following Python snippet from within the [RoboMaster desktop app Lab -> DIY Programming -> Python](https://www.dji.com/ca/robomaster-s1/downloads)
```
def root_me(module):
    __import__=rm_define.__dict__['__builtins__']['__import__']
    return __import__(module,globals(),locals(),[],0)

builtins=root_me('builtins')
subprocess=root_me('subprocess')
proc=subprocess.Popen('/system/bin/adb_en.sh',shell=True,executable='/system/bin/sh',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
```
**Do NOT close the S1 Application!**

Check the connection with `adb`
```
$ adb devices
$ adb shell
```

Upload the necessary files from your laptop to the Intelligent Controller
```
$ wget https://github.com/JacopoPan/a-minimalist-guide/blob/master/files/s1_sdk_hack.zip
$ unzip s1_sdk_hack.zip
$ cd s1_sdk_hack/
$ ./upload.sh
```

Reboot the S1 (from now on, you will hear the start-up chime twice)

### S1 Router Network Connection

Download script [`s1_connect.py`](https://github.com/JacopoPan/a-minimalist-guide/blob/master/files/s1_connect.py)

Set the ssid and password arguments on line 13 to your local WiFi network name and password, then run
```
$ wget https://github.com/JacopoPan/a-minimalist-guide/blob/master/files/s1_connect.py
$ python3 s1_connect.py
```

Set the slider on the side of the intelligent controller to "Router Connection" and click the "Connect" button besides it

Display the generated QR code to the S1 camera

Once the S1 is connected to the same network of a laptop, it can be controlled using its [Python API](https://www.dji.com/ca/robomaster-s1/programming-guide) (or and running the code from within the Lab of the [desktop app](https://www.dji.com/ca/robomaster-s1/downloads))

### S1 Simple Chassis Movement Script

If you have followed the previous steps, your laptop and S1 are now connected to the same network

Download script [`s1_movement.py`](https://github.com/JacopoPan/a-minimalist-guide/blob/master/files/s1_movement.py)

```
$ wget https://github.com/JacopoPan/a-minimalist-guide/blob/master/files/s1_movement.py
$ python3 s1_movement.py                  # Remember to activate the conda environment where you installed the SDK
```

The S1 will now move forward, backward, laterally (to its left and back), and turn in place








## Tello Talent (TT) Router Network UDP Control

### Option 1: using PacketSender on macOS

```
brew install packetsender
```

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
- Change "Address" to any address the TT took on your network (see the connected devices in your router configuration, typically at 192.168.0.1)
- Write command `command` in the "ASCII" field and click "Send"
- The Tello starts returning telemetry
- Send the `takeoff` command
- Fly
- Send the `land` command


### Option 2: using Python 3

#### Instruct the TT to connect to you local Wi-Fi network ([script](https://github.com/JacopoPan/a-minimalist-guide/blob/master/files/tt_set_ap.py))

- Set the TT to "App Mode" (i.e. the down position of the slider on the right side of the open-source controller/dot-matrix display)
- Turn on the TT (using the button on the side of the quadcopter)
- From your latop, connect to **its own** Wi-Fi network and run the following on a terminal

```
$ wget https://github.com/JacopoPan/a-minimalist-guide/blob/master/files/tt_set_ap.py
$ python3 tt_set_ap.py
```

- Turn off the TT (using the button on the side of the quadcopter)
- Set the TT to "Station Mode" (i.e. the up position of the slider on the right side of the open-source controller/dot-matrix display)
- Turn on the TT (using the button on the side of the quadcopter), it will connect to your local network (it might take a few seconds, with the status LED blinking orange, once the connection is established the status LED will turn purple)
- Connect your latop to the same network and try the next scripts

#### Minimal autonomous flight example ([script](https://github.com/JacopoPan/a-minimalist-guide/blob/master/files/tt_flight.py))

- Set the TT to "Station Mode" (i.e. the up position of the slider on the right side of the open-source controller/dot-matrix display)
- Turn on the TT (using the button on the side of the quadcopter)
- From your latop, connect to Wi-Fi network you told the TT to connect to (see [here](https://github.com/JacopoPan/a-minimalist-guide/blob/master/Part7-Heterogeneous-Multirobot-Teams-with-the-RoboMaster-SDK.md#instruct-the-tt-to-connect-to-you-local-wi-fi-network)) and run the following on a terminal

```
$ wget https://github.com/JacopoPan/a-minimalist-guide/blob/master/files/tt_flight.py
$ python3 tt_flight.py
```

#### Get telemetry ([script](https://github.com/JacopoPan/a-minimalist-guide/blob/master/files/tt_telemetry.py)) and video ([script](https://github.com/JacopoPan/a-minimalist-guide/blob/master/files/tt_video.py))

- Set the TT to "Station Mode" (i.e. the up position of the slider on the right side of the open-source controller/dot-matrix display)
- Turn on the TT (using the button on the side of the quadcopter)
- From your latop, connect to Wi-Fi network you told the TT to connect to (see [here](https://github.com/JacopoPan/a-minimalist-guide/blob/master/Part7-Heterogeneous-Multirobot-Teams-with-the-RoboMaster-SDK.md#instruct-the-tt-to-connect-to-you-local-wi-fi-network)) and run the following on a terminal

```
$ wget https://github.com/JacopoPan/a-minimalist-guide/blob/master/files/tt_telemetry.py
$ python3 tt_telemetry.py
```

```
$ wget https://github.com/JacopoPan/a-minimalist-guide/blob/master/files/tt_video.py
$ python3 tt_video.py
```

-------
> Work carried out @ University of Toronto's [Dynamic Systems Lab](https://github.com/utiasDSL) / [Vector Institute](https://github.com/VectorInstitute) / [Mitacs Elevate](https://www.mitacs.ca/en/projects/multi-agent-reinforcement-learning-decentralized-uavugv-cooperative-exploration)


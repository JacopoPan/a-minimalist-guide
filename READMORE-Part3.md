> A minimalist guide to  a few frameworks⁠—on Ubuntu and Vector computing⁠—for the person who was born yesterday
>> Written by a novice for the novice

# Part 3 - Simulating Multiple UAVs with AirSim and ROS

ubuntu 18.04 lts on lenovo p52 
i7-8850H
nvidia quadro p2000

enter, f1 

config  - display  
set - graphic device - to - discrete graphics

security - secure boot 
set -  secure boot - to - disabled

if you can use wifi to download updates and install 3rd party software (graphics/wifi)

click the gear besides sign in and choose ubuntu on wayland

install updates from "software updater" if prompted

nvidia proprietary driver nvidia-driver-440 should be available in software&updates

apply, reboot

the os should finally run smoothly and nvidia-smi report

driver 440, cuda 10.2

## AirSim

software requirements

installing from [binaries](https://microsoft.github.io/AirSim/use_precompiled/)

alternative, installing from [source](https://microsoft.github.io/AirSim/build_linux/)

running a single car example

running a multi-drone example

environments

robots models (in UE4)

robots models (in AirSim)

## ROS

software requirements

installing from package [link](http://wiki.ros.org/ROS/Installation)

installing from source [link](http://wiki.ros.org/ROS/Installation)

using ROS with AirSim

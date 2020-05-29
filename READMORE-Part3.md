> A minimalist guide to  a few frameworks⁠—on Ubuntu and Vector computing⁠—for the person who was born yesterday
>> Written by a novice for the novice

# Part 3 - Simulating Multiple UAVs with AirSim

ubuntu 18.04 lts on lenovo p52 
i7-8850H
nvidia quadro p2000

to install
get 64 bit iso https://releases.ubuntu.com/18.04/

create bootable usb stick https://ubuntu.com/tutorials/tutorial-create-a-usb-stick-on-ubuntu#1-overview

change to following in the p52 bios

enter, f1 

config  - display  
set - graphic device - to - discrete graphics

security - secure boot 
set -  secure boot - to - disabled

if you can, use wifi to download updates and install 3rd party software (graphics/wifi)

click the gear besides sign in and choose ubuntu on wayland https://wiki.ubuntu.com/Wayland for your first login

the interface will be slow for now

install updates from "software updater" if prompted

nvidia proprietary driver nvidia-driver-440 should be available in software&updates

click apply, reboot

the os interface should now run smoothly and nvidia-smi report

driver 440, cuda 10.2

## AirSim

https://microsoft.github.io/AirSim/

https://github.com/microsoft/AirSim

what it is

unreal and unity

software requirements

how it is available (as of may 2020) https://microsoft.github.io/AirSim/#how-to-get-it
win, linux, mac

on linux
you can build ue4 and airsim (in docker or your computer https://microsoft.github.io/AirSim/build_linux/)

or
installing from [binaries](https://microsoft.github.io/AirSim/use_precompiled/)

here we use the binaries for linux using ue4 
i.e. v1.3.1 - Linux
https://github.com/Microsoft/AirSim/releases
as it is a more recent and with more environments release than the unity based one

Africa
Blocks
Building 99
Landscape Mountains
Neighborhood
Soccer Field
TrapCam
Zhangjiajie


note that trapcam is split in two  file zip 001 zip 002
concatenate them first before unzippin
cat TrapCam.zip.00* > TrapCam.zip


after unzipping
run each env binaries using the name.sh script in each folder

select yes or no for car or drone

use alt Enter to switch between full screen and window

use alt Tab to get back to the terminal (and kill the sim with Ctrl C if you want)

(if you have issues with your cursor disappearing/being captured by UE4, simply switch Ubuntu workspace and close the sim from the sidebar)

use Fn + F1 to see the keyboard commands

list them here

in car mode, the arrows can be used to drive the  the vehicle


note that trap cam is a much more complex environment and might take time to load up

it can be use to simulate flora and fauna 
it has an extra interface to adjust this configuration (the default flora is a bit too complex for the p52)
https://arxiv.org/pdf/1904.05916.pdf


running any environment will create a file in ~/Documents/AirSim called setting.json

this file defines the simulation parameters but most notably which vehicles are in it
it is documented here
https://github.com/Microsoft/AirSim/blob/master/docs/settings.md


to stop being askd to choose between car and multirotor add
"SimMode": "Multirotor",

a few note
VehicleType: This could be either PhysXCar, SimpleFlight, PX4Multirotor or ComputerVision. There is no default value therefore this element must be specified.

For cars, we support only PhysX for now (regardless of value in this setting). For multirotors, we support "FastPhysicsEngine" only.

the default flight controller
https://github.com/microsoft/AirSim/blob/master/docs/flight_controller.md
is simple flight
https://github.com/microsoft/AirSim/blob/master/docs/simple_flight.md

to start any environment with 2 simple flight drones 2 meters apart
{
  "SeeDocsAt": "https://github.com/Microsoft/AirSim/blob/master/docs/settings.md",
  "SettingsVersion": 1.2,
  "SimMode": "Multirotor",
  "Vehicles": {
    "Drone0": {
      "VehicleType": "SimpleFlight",
      "X": 0, "Y": 0, "Z": 0, "Yaw": 0
    },
    "Drone1": {
      "VehicleType": "SimpleFlight",
      "X": 2, "Y": 0, "Z": 0, "Yaw": 0
    }
  }
}



programmatically set the camera







add a conda sections

add pip install airsim

https://pypi.org/project/airsim/








a simple usage scrip for two drones






















running a single car example

running a multi-drone example

environments

robots models (in UE4)

robots models (in AirSim)



> A minimalist guide to  a few frameworks⁠—on Ubuntu and Vector computing⁠—for the person who was born yesterday
>> Written by a novice for the novice

# Part 3 - Simulating Multiple UAVs with AirSim

The following instructions are for a fresh install of Ubuntu 18.04 LTS 64-bit on a Lenovo P52 (i7-8850H/Quadro P2000)

Everything after a `$` is entered on a terminal; everything after `>>>` is passed to a Python interpreter

## Ubuntu 18.04 and Nvidia proprietary drivers on Lenovo P52

Download Ubuntu 18.04 LTS 64-bit .iso
```
$ wget https://releases.ubuntu.com/18.04/ubuntu-18.04.4-desktop-amd64.iso
```
Create a bootable USB stick (on Ubuntu, using [Startup Disk Creator](https://ubuntu.com/tutorials/tutorial-create-a-usb-stick-on-ubuntu#4-iso-and-usb-selection))


Important: at boot time, enter P52's bios pressing `Enter`, then `F1`

Under the `Config` menu, enter the `Display` submenu

Set `Graphic Device` to `Discrete Graphics` (instead of `Hybrid Graphics`)⁠—this will prevent crashes during Ubuntu 18's installation

Under the `Security` menu, enter the `Secure Boot` submenu

Set `Secure Boot` to `Disabled`⁠—this will let you install NVIDIA graphic drivers

Install Ubuntu 18 (if possible, use Wi-Fi to "download updates and install 3rd party software" during the process)

At the time of the first login, click the gear icon besides "Sign in"

Choose "Ubuntu on [Wayland](https://wiki.ubuntu.com/Wayland)"

The graphical interface will be very slow⁠—this is expected

If prompted, install updates from "Software Updater" 

In the "Software & Updates" application NVIDIA proprietary driver `nvidia-driver-440` should be available

Select it, click apply, and reboot

This time around, the graphical interface should be runing smoothly

Open a terminal (`Ctrl`+`Alt`+`t`) and run command `$ nvidia-smi`

It will report the use of driver 440 and CUDA 10.2

## Using AirSim binaries

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

### Running each environment

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




### Personalizing a simulation with `setting.json`

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



TO DO programmatically set the camera




### Using AirSim Python APIs with Anaconda


add a conda sections (conda with python 3.5 is recommended as of may 2020
https://microsoft.github.io/AirSim/apis/


$ sudo apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh

$ bash Anaconda3-2020.02-Linux-x86_64.sh

accept terms
type yes
accept default location (enter)

When prompted to "Do you wish the installer to initialize Anaconda3 by running conda init?" answer "yes"

Finally, run

$ source ~/.bashrc
Turn off the auto-activation of the base environment and exit it

$ conda config --set auto_activate_base False
$ conda deactivate

re-enter the (base) environment 
conda activate

or see part 1 to create project-specific one

note that on ubuntu 18 the default pyhton is python3 (3.6)
while in (base) it is python (3.7)

in base you have pip pre-installed which is not the case for in ubuntu 18


now 
pip install msgpack-rpc-python

ERROR: notebook 6.0.3 has requirement tornado>=5.0, but you'll have tornado 4.5.3 which is incompatible.
ERROR: distributed 2.11.0 has requirement tornado>=5; python_version < "3.8", but you'll have tornado 4.5.3 which is incompatible.
Installing collected packages: msgpack-python, tornado, msgpack-rpc-python
  Attempting uninstall: tornado
    Found existing installation: tornado 6.0.3
    Uninstalling tornado-6.0.3:
      Successfully uninstalled tornado-6.0.3
Successfully installed msgpack-python-0.5.6 msgpack-rpc-python-0.4.1 tornado-4.5.3



pip install airsim

https://pypi.org/project/airsim/


### Example: 2-drone patrol and image taking from a ground observer POV


a simple usage scrip for two drones

TBD

run and environments (refer to json with 2 drones)


new terminal
remember conda activate to get in base

run python script




## Compiling the Unreal Engine 4 from source

## Compiling AirSim from source

this is required to modify the flight controller implementation

(note to self, but is it needed to re-compile UE4 or can we re-use binaries for that?)

## Tuning `simpleflight` flight controller

recompiling airsim..

## Custom Unreal Engine 4 environments

unfortunately needs windows

https://microsoft.github.io/AirSim/unreal_custenv/

## Custom drone models

??? 

## PX4 flight controller

do we need/want this?

> A minimalist guide to  a few frameworks⁠—on Ubuntu and Vector computing⁠—for the person who was born yesterday
>> Written by a novice for the novice

# Part 3 - Simulating Multiple UAVs with AirSim

The following instructions are for a fresh install of Ubuntu 18.04 LTS 64-bit on a Lenovo P52 (i7-8850H/Quadro P2000)

Everything after a `$` is entered on a terminal; everything after `>>>` is passed to a Python interpreter

## Ubuntu 18.04 and NVIDIA proprietary drivers on Lenovo P52

Download Ubuntu 18.04 LTS 64-bit .iso: `$ wget https://releases.ubuntu.com/18.04/ubuntu-18.04.4-desktop-amd64.iso` and create a bootable USB stick (e.g., on Ubuntu, using [Startup Disk Creator](https://ubuntu.com/tutorials/tutorial-create-a-usb-stick-on-ubuntu#4-iso-and-usb-selection))

**Important**: at boot time, enter P52's bios pressing `Enter`, then `F1`

1. Under the `Config` menu, enter the `Display` submenu
- Set `Graphic Device` to `Discrete Graphics` (and not `Hybrid Graphics`)⁠—this will prevent crashes during the installation
2. Under the `Security` menu, enter the `Secure Boot` submenu
- Set `Secure Boot` to `Disabled`⁠—this will let you install NVIDIA graphic drivers

Install Ubuntu 18 (if possible, use Wi-Fi to "download updates and install 3rd party software" during the process)

At the time of the first login, click the gear icon besides "Sign in"; choose "Ubuntu on [Wayland](https://wiki.ubuntu.com/Wayland)"

The graphical interface will be very slow⁠—this is expected—if prompted, install updates from "Software Updater" 

Open the "Software & Updates" application: NVIDIA proprietary driver `nvidia-driver-440` should be available

Select it, click apply, and reboot: this time around, the graphical interface should be runing smoothly

Open a terminal (`Ctrl`+`Alt`+`t`) and run command `$ nvidia-smi`: it will report the use of driver 440 and CUDA 10.2

## Using AirSim binaries on Ubuntu 18

AirSim ([Documentation](https://microsoft.github.io/AirSim/),[GitHub](https://github.com/microsoft/AirSim)) is an open source, photorealistic simulator for drones and ground vehicles developed on top of Epic's [Unreal Engine 4](https://github.com/EpicGames/UnrealEngine) (UE4) by Microsoft Research ([arXiv paper](https://arxiv.org/abs/1705.05065))

The rest of this section is about **running AirSim UE4 binaries and using its Python APIs** on Ubuntu 18

Instructions on how to compile both UE4 and AirSim sources on Ubuntu 18 are later in this guide

Alternatively, one can
- [Run AirSim binaries on Windows](https://github.com/microsoft/AirSim/releases) 
- Or [install UE4 and compile AirSim sources on Windows](https://microsoft.github.io/AirSim/build_windows/)

Note that v1.3.1 of [Linux](https://github.com/microsoft/AirSim/releases/tag/v1.3.1-linux) and [Windows](https://github.com/microsoft/AirSim/releases/tag/v1.3.1-windows) precompiled binaries include **different environments**

As of May 2020, [support for Unity](https://microsoft.github.io/AirSim/Unity/) is still experimental

### Download the precompiled environments

Verify what is the latest [Linux release](https://github.com/microsoft/AirSim/releases), here we consider April 2020 [v1.3.1 release](https://github.com/microsoft/AirSim/releases/tag/v1.3.1-linux) which includes the following environments
```
Africa
Blocks
Building 99
Landscape Mountains
Neighborhood
Soccer Field
TrapCam
Zhangjiajie
```
Download all of them (approx. 8GB)
```
$ wget https://github.com/microsoft/AirSim/releases/download/v1.3.1-linux/Africa.zip
$ wget https://github.com/microsoft/AirSim/releases/download/v1.3.1-linux/Blocks.zip
$ wget https://github.com/microsoft/AirSim/releases/download/v1.3.1-linux/Building_99.zip
$ wget https://github.com/microsoft/AirSim/releases/download/v1.3.1-linux/LandscapeMountains.zip
$ wget https://github.com/microsoft/AirSim/releases/download/v1.3.1-linux/Neighborhood.zip
$ wget https://github.com/microsoft/AirSim/releases/download/v1.3.1-linux/SoccerField.zip
$ wget https://github.com/microsoft/AirSim/releases/download/v1.3.1-linux/TrapCam.zip.001
$ wget https://github.com/microsoft/AirSim/releases/download/v1.3.1-linux/TrapCam.zip.002
$ wget https://github.com/microsoft/AirSim/releases/download/v1.3.1-linux/Zhangjiajie.zip
```
Note that `TrapCam` is split into two files that need to be concatenated before unzipping
```
$ cat TrapCam.zip.00* > TrapCam.zip
```

### Running each environment

Unzip and run the environment, e.g. for `Africa.zip`, navigate to the download folder and
```
$ unzip Africa.zip -d Africa
$ cd Africa
$ ./Africa_001.sh                       # Each environment has an executable ".sh" in its top folder 
```
Select "Yes" or "No" to start the environment with a car or drone (this prompt will disappear once you set `SimMode` in `settings.json` as shown below)

Use the `-ResX=num_x_pixels -ResY=num_y_pixels -windowed` options to set a lower resolution 
```
$ ./Africa_001.sh  -ResX=640 -ResY=480 -windowed
```

Once the simulation starts, use `Alt`+`Enter` to switch between full screen and window views

Occasionally, UE4 might capture your cursor: use `Alt`+`Tab` to navigate back to the terminal and kill the simulation with `Ctrl`+`c`; or switch Ubuntu workspace (`Ctrl`+`Alt`+top or bottom arrow) and close it from the sidebar

Use `Fn`+`F1` to display this list of commands
```
F1          Toggle this help
F3          Toggle wireframe whe you press F1
F10         Show weather options
F           Switch to FPV View
B           Switch to "fly with me"
\           Switch to ground observer view
/           Switch to chase with spring arm mode
M           Switch to manual camera control
                    Arrow keys
                    Page Up/Down -> move up, down
                    W, S -> pitch
                    A, D -> yaw
R           Toggle recording
;           Toggle debug report
0           Toggle all sub-windows
1           Toggle depth sub-window
2           Toggle segmentation sub-window
3           Toggle scene sub-window
T           Toggle trace line
Backspace   Reset everything
```
When starting an environment with a car (`"SimMode": "Multirotor"`), the arrows key can also be used to drive the vehicle

Note that the `TrapCam` environment is quite complex environment and can take a few minutes to load: it can be used to simulate flora and fauna (see [this paper](https://arxiv.org/pdf/1904.05916.pdf)) and it includes an interactive interface to to adjust their configuration

### Personalizing a simulation using `setting.json`

The first time you run AirSim, it will create the following file ` ~/Documents/AirSim/settings.json` that will be loaded by all subsequent simulations; originally it only contains the following lines
```
{
  "SeeDocsAt": "https://github.com/Microsoft/AirSim/blob/master/docs/settings.md",
  "SettingsVersion": 1.2
}
```
The documentation for this file is located [here](https://github.com/Microsoft/AirSim/blob/master/docs/settings.md); `settings.json` contains
- Vehicle settings
- Camera settings
- Time-of-day settings
- etc.

Copy the following into `settings.json` starts a simulation with 2 quadcopters, 2 meters apart, from an observer POV
```
{
  "SeeDocsAt": "https://github.com/Microsoft/AirSim/blob/master/docs/settings.md",
  "SettingsVersion": 1.2,
  "SimMode": "Multirotor",
  "ViewMode": "GroundObserver",
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
```
[`SimpleFlight`](https://github.com/microsoft/AirSim/blob/master/docs/simple_flight.md) is AirSim's default [flight controller](https://github.com/microsoft/AirSim/blob/master/docs/flight_controller.md) (see its [code](https://github.com/microsoft/AirSim/tree/master/AirLib/include/vehicles/multirotor/firmwares/simple_flight)); a few other relevant notes from the documentation

> VehicleType: This could be either PhysXCar, SimpleFlight, PX4Multirotor or ComputerVision. There is no default value therefore this element must be specified.

> For cars, we support only PhysX for now (regardless of value in this setting). For multirotors, we support "FastPhysicsEngine" only.

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



```


WIP from here



```


### Example: 2-drone patrol and image taking from a ground observer POV


a simple usage scrip for two drones

TBD

run and environments (refer to json with 2 drones)


new terminal
remember conda activate to get in base

run python script















## Compiling the Unreal Engine 4 from source

## Compiling AirSim from source

docker?

this is required to modify the flight controller implementation

(note to self, but is it needed to re-compile UE4 or can we re-use binaries for that?)

## Tuning `simpleflight` flight controller

recompiling airsim..

## Custom Unreal Engine 4 environments

unfortunately needs windows

https://microsoft.github.io/AirSim/unreal_custenv/

## Custom drone models

to be determined 

## PX4 flight controller

do we need/want this?

## ROS and AirSim C++ APIs

do we need/want this?

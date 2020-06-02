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

Run the Africa environment again to see 2 drones in it
```
$ ./Africa_001.sh  -ResX=640 -ResY=480 -windowed
```

> UE 4.24 uses Vulkan drivers by default, but they can consume more GPU memory. If you get memory allocation errors, then you can try switching to OpenGL using `-opengl`

### Using AirSim Python APIs with Anaconda

AirSim exposes [Python aAPIs](https://microsoft.github.io/AirSim/apis/) to control vehicles—the use AirSim's C++ APIs is detailed below in this guide)—and, as of May 2020, Python 3.5 (or newer) and Anconda are recommended for their use

More thorough instructions to install and use `coda` are provided in [`README.md` of this repository](https://github.com/JacopoPan/a-minimalist-guide/blob/master/README.md); these are minimal steps
```
$ sudo apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
$ wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
$ bash Anaconda3-2020.02-Linux-x86_64.sh
```
Accept the terms and conditions; type `yes`; accept the default installation location by pressing `Enter`

When prompted to "Do you wish the installer to initialize Anaconda3 by running conda init?" type `yes` again

Finally, run
```
$ source ~/.bashrc
$ conda config --set auto_activate_base False   #this turns off the auto-activation of the (base) environment
```
Verify you can exit and re-enter the `(base)` `conda`'s environment 
```
$ conda deactivate
$ conda activate
```
Note that in Ubuntu 18 the default Pyhton is `python3` (version 3.6) while in `conda`'s environment `(base)` the interpreter is `python` (version 3.7) and `pip` is pre-installed⁠—which is not the case in Ubuntu 18, outside `(base)`)

In `(base)`, install inter-process messaging library MessagePack-RPC 
```
$ conda activate
$ pip install msgpack-rpc-python
```
add one of these
```
(base) pip install opencv-python
conda install opencv
```
Note that this might throw the following error and roll back `tornato` from version 6.0.3 to 4.5.3—**this is ok**
```
ERROR: notebook 6.0.3 has requirement tornado>=5.0, but you'll have tornado 4.5.3 which is incompatible.
ERROR: distributed 2.11.0 has requirement tornado>=5; python_version < "3.8", but you'll have tornado 4.5.3 which is incompatible.
Installing collected packages: msgpack-python, tornado, msgpack-rpc-python
  Attempting uninstall: tornado
    Found existing installation: tornado 6.0.3
    Uninstalling tornado-6.0.3:
      Successfully uninstalled tornado-6.0.3
Successfully installed msgpack-python-0.5.6 msgpack-rpc-python-0.4.1 tornado-4.5.3
```
Install [AirSim's Python APIs](https://pypi.org/project/airsim/)
```
$ pip install airsim
```




----------
```
WIP below here
```
----------

point out the difference between 
using pip
and building AirSim (`import airsim` will only work within `AirSim/PythonClient`)
use conda with both (e.g. numpy is already in (base))

in doubt
conda activate
pip uninstall airsim

see `AirSim/PythonClient/setup_path.py`


### 2-drone example


add simPrintLogMessage("Iteration: ", to_string(i))

save these two scripts
```
import airsim

client = airsim.MultirotorClient()                       # connect to the simulator
client.confirmConnection()
client.enableApiControl(True, vehicle_name="Drone0")     # enable API control on Drone0
client.armDisarm(True, vehicle_name="Drone0")            # arm Drone0

client.takeoffAsync(vehicle_name="Drone0")               # let Drone0 take-off asynchronously (i.e. non-blocking)
airsim.wait_key('Press any key to move')                 # the simulator waits for a key to start moving Drone1

client.moveToPositionAsync(10, 5, -1.5, 5, vehicle_name="Drone0").join()
client.hoverAsync(vehicle_name="Drone0").join()          # Drone0 moves to (10, 5, -1.5) at 5m/s and hovers
                                                         # .join() let the script wait for asynchronous (non-blocking) methods

airsim.wait_key('Press any key to reset')                # press a key
client.armDisarm(False, vehicle_name="Drone0")           # to disarm Drone0
client.reset()                                           # reset the simulation
client.enableApiControl(False, vehicle_name="Drone0")    # and disable API control of Drone0
```


```
import airsim

client = airsim.MultirotorClient()                       # connect to the simulator
client.confirmConnection()
client.enableApiControl(True, vehicle_name="Drone1")     # enable API control on Drone1
client.armDisarm(True, vehicle_name="Drone1")            # arm Drone1

client.takeoffAsync(vehicle_name="Drone1")               # let Drone1 take-off asynchronously (i.e. non-blocking)
airsim.wait_key('Press any key to move')                 # the simulator waits for a key to start moving Drone1

client.moveToPositionAsync(10, 4, -0.5, 5, vehicle_name="Drone1").join()
client.hoverAsync(vehicle_name="Drone1").join()          # Drone1 moves to (10, 4, -0.5) at 5m/s and hovers
                                                         # .join() let the script wait for asynchronous (non-blocking) methods

airsim.wait_key('Press any key to reset')                # press a key
client.armDisarm(False, vehicle_name="Drone1")           # to disarm Drone1
client.reset()                                           # reset the simulation
client.enableApiControl(False, vehicle_name="Drone1")    # and disable API control of Drone1
```

add taking images

add pfm format apis
https://microsoft.github.io/AirSim/pfm/

run an environments (refer to json with 2 drones)

new terminal, remember conda activate to get in base, run python script
```
$ conda activate
$ python 
```

note on control from a single script


api use NED, vehicle starts in 0,0,0
note z is up in UE4 and down in AirSim
OriginGeopoint sets lat lon alt of Player Start



mention
pausing
collision
time of day / lat, lon, sun position
weather
https://github.com/Microsoft/AirSim/blob/master/PythonClient/computer_vision/weather.py





### Using AirSim Python C++ with ROS

install ros steps (point below for installation from source)

https://microsoft.github.io/AirSim/airsim_ros_pkgs/
https://github.com/microsoft/AirSim/blob/master/docs/airsim_tutorial_pkgs.md





## AirSim Python APIs

explain `duration` `max_wait_seconds` `Async` `join` etc

expalin drivetrain, yaw_mode, lookahead, and adaptive_lookahead

documenting the APIs with the help of James

https://github.com/microsoft/AirSim/blob/master/PythonClient/airsim/client.py

By default AirSim uses carrot following algorithm.

Currently lowest level control available in AirSim is moveByAngleThrottleAsync

## AirSim C++ APIs

documenting in full with the help of James

https://github.com/microsoft/AirSim/blob/master/AirLib/src/vehicles/multirotor/api/MultirotorApiBase.cpp



## Compiling the Unreal Engine 4 and AirSim from source

recompiling airsim is required to modify the flight controller implementation
(note to self, but is it needed to re-compile UE4 or can we re-use binaries for that?)

in my case, i'm building outside the conda env

### UE4

to get ue4 sources you need
github account https://github.com/
epic account https://www.epicgames.com/id/login
follow these instructions https://www.unrealengine.com/en-US/ue4-on-github
to link your github and epic accounts
to be added to epic dev team on github https://github.com/orgs/EpicGames/teams/developers
and be able to clone https://github.com/EpicGames/UnrealEngine

as of may 2020, 4.25 is the latest
we are using 4.24 as recommended in airsim docs

```
sudo apt install git
git clone -b 4.24 https://github.com/EpicGames/UnrealEngine.git
cd UnrealEngine
./Setup.sh
say yes to register file types if prompted
./GenerateProjectFiles.sh
make
```
this takes a bit over 1h on the p52
a few tempnam warnings 

full docs
https://docs.unrealengine.com/en-US/Platforms/Linux/index.html

### AirSim

```
cd ..
git clone https://github.com/Microsoft/AirSim.git
cd AirSim
./setup.sh #insert your password note that this will install clang-8 and python 2.7 among other ubuntu packages
./build.sh
```
throws plenty of warnings

## first use

```
echo  'export PATH=~/UnrealEngine/Engine/Binaries/Linux:$PATH' >> ~/.bashrc #(note prefixing and use of single quote '
source ~/.bashrc
```

run UE4 bin from anywhere with simply

$ UE4Editor
can take a few minues (the first time only)

Select or Create New Project
click "More"
Browse
navigate to AirSim/Unreal/Environments/Blocks

Blocks.uproject and Open

next time it will be in recent projects on the Select or Create New Project menu

Convert Project
More options
Convert in-place

no more prompts but if you do refer to https://microsoft.github.io/AirSim/build_linux/

dismiss new plugin notification, close the interface tour, some shaders will still be compiling

click play or Alt+P

wait for shaders to finish compiling

it loaded settings.json in your ~/AirSim/... so you should see the car(s), drone(s) set there

eg refer to the example settings in section above Personalizing a simulation using `setting.json` for 2 drones 2 meters apart observed from the ground observer pov

fn f1 for menu (it will activate wireframe visal go back with fn f3)

m for manual camera then arrows + pgup pgdn and wsad to explore the environment

esc to terminate

**Unreal is slowed down dramatically when I run API**
> After Unreal Editor loads, press Play button. Tip: go to 'Edit->Editor Preferences', in the 'Search' box type 'CPU' and ensure that the 'Use Less CPU when in Background' is unchecked.


remember of the script defined above  in Example: 2-drone patrol and image taking from a ground observer POV

you can run it in blocks as well

alt p again

new terminal

test api control




## Custom Unreal Engine 4 environments

needs Epic Games Launcher (Windows, macOS?) to create and Unreal project folder
https://microsoft.github.io/AirSim/unreal_custenv/

then just copy it over to your Linux machine (how many of the steps above can we move to Ubuntu?)


add notes on Updating Your Environment to Latest Version of AirSim










## Customizing the drone 

https://microsoft.github.io/AirSim/custom_drone/

### pyhsics and model

https://github.com/Microsoft/AirSim/wiki/hexacopter

### New APIs

example
https://github.com/Microsoft/AirSim/commit/f0e83c29e7685e1021185e3c95bfdaffb6cb85dc

### Tuning `simpleflight` flight controller

Please note that simple_slight currently doesn't support state estimator which means estimated and ground truth kinematics values would be same for simple_flight.

recompiling airsim
https://github.com/microsoft/AirSim/tree/master/AirLib/include/vehicles/multirotor


## Create new binaries

For custom environment/airsim
at once ore in separate steps?
TBD


## Headless AirSim on a remote server

TBD, ideally on Vector's cluster
https://microsoft.github.io/AirSim/settings/#viewmode NoDisplay(?)

## (optional) PX4 flight controller

TBD, if needed

## (optional) ROS installation from source

TBD, if needed

## (alternative) Docker installation

TBD, if needed https://github.com/Microsoft/AirSim/blob/master/docs/docker_ubuntu.md
TBD

> A minimalist guide to  a few frameworks⁠—on Ubuntu and Vector computing⁠—for the person who was born yesterday
>> Written by a novice for the novice

# Part 3 - Simulating Multiple UAVs with AirSim

The following instructions are for a fresh install of Ubuntu 18.04 LTS 64-bit on a Lenovo P52 (i7-8850H/Quadro P2000)

Everything after a `$` is entered on a terminal; everything after `>>>` is passed to a Python interpreter

## Ubuntu 18.04 and NVIDIA proprietary drivers on Lenovo P52

Download Ubuntu 18.04 LTS's 64-bit ISO image: `$ wget https://releases.ubuntu.com/18.04/ubuntu-18.04.4-desktop-amd64.iso` and create a bootable USB stick (e.g., on Ubuntu, using [Startup Disk Creator](https://ubuntu.com/tutorials/tutorial-create-a-usb-stick-on-ubuntu#4-iso-and-usb-selection))

**Important**: at boot time, enter the Lenovo P52's BIOS pressing `Enter`, then `F1`

1. Under the `Config` menu, enter the `Display` submenu
- Set `Graphic Device` to `Discrete Graphics` (and not `Hybrid Graphics`)⁠—this will prevent crashes during the installation
2. Under the `Security` menu, enter the `Secure Boot` submenu
- Set `Secure Boot` to `Disabled`⁠—this will let you install NVIDIA graphic drivers

Install Ubuntu 18 (if possible, use Wi-Fi to "download updates and install 3rd party software" during the process)

At the time of the first login, click the gear icon besides "Sign in"; choose "Ubuntu on [Wayland](https://wiki.ubuntu.com/Wayland)"

The graphical interface will be very slow⁠—this is expected, the system is not using the GPU nor the CPU integrated graphics

If prompted, install updates from "Software Updater" 

Open the "Software & Updates" application: NVIDIA's proprietary driver `nvidia-driver-440` should be available

Select it, click apply, and reboot: this time around, the graphical interface will be running smoothly

Open a terminal (`Ctrl`+`Alt`+`t`) and run command `$ nvidia-smi`: it will report the use of driver 440 and CUDA 10.2

## Using AirSim binaries on Ubuntu 18

AirSim ([Documentation](https://microsoft.github.io/AirSim/), [GitHub](https://github.com/microsoft/AirSim)) is an open source, photorealistic simulator for drones and ground vehicles developed on top of Epic's [Unreal Engine 4](https://github.com/EpicGames/UnrealEngine) (UE4) by Microsoft Research ([arXiv paper](https://arxiv.org/abs/1705.05065))

Concretely, AirSim is a [_UE4 Plugin_](https://docs.unrealengine.com/en-US/Programming/Plugins/index.html)—code and data you can add to any UE4 project;
the simplest way to use AirSim on Ubuntu 18 is to:
- Run the binaries of a **precompiled UE4 environment** containing the AirSim pluging
- Control the robots through AirSim's **Python APIs**

Note 1: the steps to build the UE4 Editor (necessary to modify models, environments, and add the AirSim plugin) and AirSim (including Python/C++ libraries and ROS nodes to interface with it) from source code are given below

Note 2: one can also [use the binaries](https://github.com/microsoft/AirSim/releases) or [build from source](https://microsoft.github.io/AirSim/build_windows/) on Windows

Note 3: [Epic Games Launcher](https://www.epicgames.com/unrealtournament/en-US/download) can be used to download new maps/assets from UE4's [Marketplace](https://www.unrealengine.com/marketplace/en-US/store). It is **not available on Linux** (Windows and Mac only). Yet, assets can be transferred to Ubuntu after download ([see the next part of this guide](https://github.com/JacopoPan/a-minimalist-guide/blob/master/Part4-Modifying-AirSim.md)) and [3rd party alternatives exist](https://github.com/neutrino-steak/UE4LinuxLauncher)

Note 4: as of June 2020, [support for Unity](https://microsoft.github.io/AirSim/Unity/) is still experimental

### Download the precompiled environments

Find the latest AirSim's [Linux release](https://github.com/microsoft/AirSim/releases)—April 2020's [v1.3.1 release](https://github.com/microsoft/AirSim/releases/tag/v1.3.1-linux) includes the following environments:
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
Note: [Windows' v1.3.1](https://github.com/microsoft/AirSim/releases/tag/v1.3.1-windows) precompiled binaries include **different environments**

Download all of environments (approx. 8GB)
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

### Run a precompiled environment

Use an environment, e.g. `Africa.zip`, by navigating to the folder where it was downloaded and running
```
$ unzip Africa.zip -d Africa
$ cd Africa
$ ./Africa_001.sh                       # Note: each environment has a single executable ".sh" script in its top folder, its name can vary 
```
Select "Yes" or "No" to start the environment with either a car or drone

Note: this prompt will disappear once you set `SimMode` in file `~/Documents/AirSim/settings.json` (more on this below)

Once the simulation starts, use `Alt`+`Enter` to switch between full screen and window views

Note: if the environment's display window captures your cursor:
- Use `Alt`+`Tab` to navigate back to the terminal and kill it with `Ctrl`+`c`
- Or switch Ubuntu workspace (`Ctrl`+`Alt`+top or bottom arrow) and close it from the sidebar (right click and `Quit`)

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
When starting an environment with a car (you answered "Yes" to the prompt), the arrows key can be used to drive it

Use the `-ResX=num_x_pixels -ResY=num_y_pixels -windowed` options to set your preferred resolution 
```
$ ./Africa_001.sh  -ResX=640 -ResY=480 -windowed
```
UE 4.24 uses Vulkan drivers which can take up more GPU memory. If you get memory allocation errors, you can switch to OpenGL with
```
$ ./Africa_001.sh  -ResX=640 -ResY=480 -windowed -opengl
```
Note: the `TrapCam` environment is a quite complex one and it can take a few minutes to load: it simulates flora and fauna (see [this paper](https://arxiv.org/pdf/1904.05916.pdf)) and it includes an interactive interface to to adjust their configuration

### Customize a simulation with `settings.json`

The very first time you run AirSim, it will create file ` ~/Documents/AirSim/settings.json` with the following lines:
```
{
  "SeeDocsAt": "https://github.com/Microsoft/AirSim/blob/master/docs/settings.md",
  "SettingsVersion": 1.2
}
```
`settings.json` will be loaded everytime you load the AirSim plugin (e.g., running precompiled binaries or pressing "Play" in the UE4 Editor)

`settings.json` can be used to configure many world's, vehicles', and cameras' parameters⁠—a complete list is provided [here](https://github.com/Microsoft/AirSim/blob/master/docs/settings.md)

For example, copy the following into `settings.json` to start a simulation 
- Using quadcopters (`"SimMode": "Multirotor"`)
- Containing 2 of them (named `Drone0` and `Drone1`)
- Setting them 2 meters apart along the `X` axis, and 1 along `Y`
- And making the default `ViewMode` that of a `GroundObserver`
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
      "X": 2, "Y": 1, "Z": 0, "Yaw": 0
    }
  }
}
```
Note 1: `VehicleType` can be `PhysXCar`, `SimpleFlight`, `PX4Multirotor`, or `ComputerVision`; there is no default value: it must be specified

Note 2: [`SimpleFlight`](https://github.com/microsoft/AirSim/blob/master/docs/simple_flight.md) is AirSim's default [flight controller](https://github.com/microsoft/AirSim/blob/master/docs/flight_controller.md) (see its code [here](https://github.com/microsoft/AirSim/tree/master/AirLib/include/vehicles/multirotor/firmwares/simple_flight))

Note 3: `"ViewMode": "noDisplay",` can be used to [freeze rendering](https://microsoft.github.io/AirSim/settings/#viewmode) while still exposing AirSim's APIs (including the ones for compute vision) and improve performance (i.e., frames per second)

Note 4: while a `PhysicsEngineName` setting exists, AirSim only supports `PhysX` for cars and `FastPhysicsEngine` for multirotors

Running the `Africa` environment again will display 2 drones within it
```
$ ./Africa_001.sh  -ResX=640 -ResY=480 -windowed
```

### Option A: use AirSim's Python APIs with Anaconda

AirSim exposes [Python APIs](https://github.com/microsoft/AirSim/blob/master/docs/apis.md) to control vehicles—as of June 2020, Python 3.5 (or newer) and Anconda are recommended for their use

More thorough instructions to install and use `coda` are provided in [here](https://github.com/JacopoPan/a-minimalist-guide#install-conda); these are minimal steps
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
Verify that you can exit and re-enter the default `conda` environment called `(base)`
```
$ conda deactivate
$ conda activate
```
Note: Ubuntu 18's default Pyhton is `python3` (version 3.6) without `pip`; in `conda`'s environment `(base)` the interpreter is called `python` (version 3.7) and `pip` is pre-installed⁠

In `(base)`, install the inter-process messaging library [MessagePack-RPC](https://github.com/msgpack-rpc/msgpack-rpc)
```
$ conda activate
$ pip install msgpack-rpc-python
```
Note that this might throw an error and roll-back `tornado` from version 6.0.3 to 4.5.3—**this is ok**
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
If `tornado` is accidentally upgraded later on, check [this potential fix](https://github.com/microsoft/AirSim/blob/master/docs/faq.md#when-making-api-call-i-get-error)

Install [AirSim's Python APIs](https://pypi.org/project/airsim/) (as of June 2020, v1.2.8) in `(base)` from the Python Package Index (PyPI)
```
$ conda activate
$ pip install airsim
```
Note: to eventually modify AirSim's Python APIs, **remember to uninstall this package** and use a local build from source (more on this below)
```
$ conda activate
$ pip uninstall airsim
```

#### AirSim's Python APIs 2-drone example

To run a 2-drone example, make sure that `~/Documents/AirSim/settings.json` contains the configuration proposed [above](https://github.com/JacopoPan/a-minimalist-guide/blob/master/Part3-Using-AirSim.md#customize-a-simulation-with-settingsjson)

Save the following 2 scripts in your home folder as `~/drone0.py` and `~/drone1.py`
```
# drone0.py
import airsim

client = airsim.MultirotorClient()                       # connect to the simulator
client.confirmConnection()
client.enableApiControl(True, vehicle_name="Drone0")     # enable API control on Drone0
client.armDisarm(True, vehicle_name="Drone0")            # arm Drone0

client.takeoffAsync(vehicle_name="Drone0").join()        # let Drone0 take-off
client.moveToPositionAsync(15, -3, -4, 5, vehicle_name="Drone0").join()
client.hoverAsync(vehicle_name="Drone0").join()          # Drone0 moves to (15, -3, 4) at 5m/s and hovers (note the inverted Z axis)
                                                         # .join() let the script wait for asynchronous (i.e. non-blocking) methods

# take an image of type "Scene" from the "bottom_center" of "Drone0"
raw = client.simGetImage("bottom_center", airsim.ImageType.Scene, vehicle_name="Drone0")
f = open("Drone0a.png", "wb")
f.write(raw)                                             # save the image as a PNG file
f.close()

# take an image of type "Segmentation" from the "bottom_center" of "Drone0"
raw = client.simGetImage("bottom_center", airsim.ImageType.Segmentation, vehicle_name="Drone0")
f = open("Drone0b.png", "wb")
f.write(raw)                                             # save the image as a PNG file
f.close()

airsim.wait_key('Press any key to reset')                # press any key
client.armDisarm(False, vehicle_name="Drone0")           # disarm Drone0
client.reset()                                           # reset the simulation
client.enableApiControl(False, vehicle_name="Drone0")    # disable API control of Drone0
```
And
```
# drone1.py
import airsim

client = airsim.MultirotorClient()                       # connect to the simulator
client.confirmConnection()
client.enableApiControl(True, vehicle_name="Drone1")     # enable API control on Drone1
client.armDisarm(True, vehicle_name="Drone1")            # arm Drone1

client.takeoffAsync(vehicle_name="Drone1").join()        # let Drone1 take-off
client.moveToPositionAsync(20, 3, -1, 5, vehicle_name="Drone1").join()
client.hoverAsync(vehicle_name="Drone1").join()          # Drone1 moves to (20, 3, 1) at 5m/s and hovers (note the inverted Z axis)
                                                         # .join() let the script wait for asynchronous (i.e. non-blocking) methods

# take an image of type "Scene" from the "bottom_center" of "Drone1"
raw = client.simGetImage("bottom_center", airsim.ImageType.Scene, vehicle_name="Drone1")
f = open("Drone1a.png", "wb")
f.write(raw)                                             # save the image as a PNG file
f.close()

# modify the orientation for camera "bottom_center" of "Drone1"
client.simSetCameraOrientation("bottom_center", airsim.to_quaternion(1.5, 0, 0), vehicle_name="Drone1"); # radians

# take another image of type "Scene" from the "bottom_center" of "Drone1"
raw = client.simGetImage("bottom_center", airsim.ImageType.Scene, vehicle_name="Drone1")
f = open("Drone1b.png", "wb")
f.write(raw)                                             # save the image as a PNG file
f.close()

airsim.wait_key('Press any key to reset')                # press any key
client.armDisarm(False, vehicle_name="Drone1")           # disarm Drone1
client.reset()                                           # reset the simulation
client.enableApiControl(False, vehicle_name="Drone1")    # disable API control of Drone1
```
Open 3 terminals (3x `Ctrl`+`Alt`+`t`); in the first one, run an AirSim environment, e.g., for "Neighborhood"
```
$ cd Neighborhood
$ ./AirSimNH.sh  -ResX=640 -ResY=480 -windowed
```
In each of the other 2 terminals, run the Python scripts
```
$ conda activate
$ python ~/drone0.py
```
And
```
$ conda activate
$ python ~/drone1.py
```
The 2 drones will perform a short flight and create 4 PNG images in `~`: `Drone0a.png`, `Drone0b.png`, `Drone1a.png`, `Drone1b.png`

Note 1: AirSim's APIs use North-East-Down (NED) coordinates (`Z` points up in UE4 but down in AirSim)

Note 2: latitude and longitude of (0,0,0) can be set in `settings.json` by adding
```
  "OriginGeopoint": {
    "Latitude": 47.641468,
    "Longitude": -122.140165,
    "Altitude": 122
  },
```
Note: if you add this at the end (i.e., before the last `}`) of `settings.json`, you must remove the trailing comma and add one at the end of the previous setting

##### Cameras APIs and settings

The scripts above use camera `bottom_center`; the [available cameras](https://github.com/microsoft/AirSim/blob/master/docs/image_apis.md#available-cameras) are
```
Car and Multirotor
    front_center
    front_right
    front_left
    back_center
Car only
    fpv
Multirotor only
    bottom_center
```
The scripts above use 2 image types, `airsim.ImageType.Scene` and `airsim.ImageType.Segmentation`; the [available image types](https://github.com/microsoft/AirSim/blob/master/docs/image_apis.md#available-imagetype-values) are
```
  Scene = 0,                  # UE4 rendered view
  DepthPlanner = 1,           # ground truth, camera plan depth 
  DepthPerspective = 2,       # ground truth, projection ray depth 
  DepthVis = 3, 
  DisparityNormalized = 4,
  Segmentation = 5,           # ground truth using UE4's meshes
  SurfaceNormals = 6,
  Infrared = 7                # currently, a mapping from object id to the 0-255 range
```
Script `drone1.py` uses `client.simSetCameraOrientation(..)` to [modify the orientation](https://github.com/microsoft/AirSim/blob/master/docs/image_apis.md#camera-apis) of a camera on "Drone1"

The default resolution of a camera capture is 256x144 pixels, to [change camera settings and resolution](https://github.com/microsoft/AirSim/blob/master/docs/image_apis.md#changing-resolution-and-camera-parameters)
```
  "CameraDefaults": {
      "CaptureSettings": [
        {
          "ImageType": 0,
          "Width": 1024,
          "Height": 576,
          "FOV_Degrees": 90,
          "AutoExposureSpeed": 100,
          "MotionBlurAmount": 0
        }
    ]
  },
```
Note 1: if you add this at the end (i.e., before the last `}`) of `settings.json`, you must remove the trailing comma and add one at the end of the previous setting

Note 2: `"ImageType": 0,` means that this will only affect the new resolution (1024x576) of `airsim.ImageType.Scene`

Note 3: more information about the computer vision API are available at these links: [APIs](https://github.com/microsoft/AirSim/blob/master/docs/image_apis.md), [pfm](https://github.com/microsoft/AirSim/blob/master/docs/pfm.md)

Note 4: the time of the day (affecting the sun's position) can be set through the [APIs](https://github.com/microsoft/AirSim/blob/master/docs/apis.md#time-of-day-api) or [`settings.json`](https://github.com/microsoft/AirSim/blob/master/docs/settings.md#timeofday)

Note 5: the weather can be modified from the [APIs](https://github.com/microsoft/AirSim/blob/master/docs/apis.md#weather-apis) (see the [code](https://github.com/Microsoft/AirSim/blob/master/PythonClient/computer_vision/weather.py))

Note 6: the [clock speed](https://github.com/microsoft/AirSim/blob/master/docs/settings.md#clockspeed) can also be adjusted from `settings.json`

Before moving on to the next steps, **remember to uninstall `airsim` from `(base)`** to avoid conflicts with the locally built AirSim from source
```
$ conda activate
$ pip uninstall airsim
```

## Building Unreal Engine 4 and AirSim from source

Building the Unreal Engine 4 (and Editor) and AirSim allows to use the latter's C++ APIs and their ROS wrapper node.

The UE4 Editor and AirSim source code are also necessary to create custom maps, robot models, flight controllers, new APIs, etc. as shown in the [next part of this guide](https://github.com/JacopoPan/a-minimalist-guide/blob/master/Part4-Modifying-AirSim.md)

### Build UE4 and UE4Editor

The first step is to build the [Unreal Engine 4.24 on Ubuntu 18](https://docs.unrealengine.com/en-US/Platforms/Linux/index.html), to do so, one needs
- A [GitHub account](https://github.com/login)
- An [Epic account](https://www.epicgames.com/id/login)

Follow [these instructions](https://www.unrealengine.com/en-US/ue4-on-github) to link your GitHub and Epic accounts

Once you have been added to [Epic Games' organization](https://github.com/EpicGames) as a [developer](https://github.com/orgs/EpicGames/teams/developers), you will be able to `git clone` [UE4's source code](https://github.com/EpicGames/UnrealEngine)

As of June 2020, 4.25 is the latest release but we use 4.24, as recommended by AirSim's documentation

The following steps take **a bit more than 1 hour** on a Lenovo P52 (and throw a few warnings)
```
$ sudo apt install git
$ cd ~
$ git clone -b 4.24 https://github.com/EpicGames/UnrealEngine.git
$ cd UnrealEngine
$ ./Setup.sh                 # if prompted, say yes to register file types
$ ./GenerateProjectFiles.sh
$ make
```
Modify your `~/.bashrc` file to add the location of UE4's binaries to the `PATH` environmental variable
```
$ echo  'export PATH=~/UnrealEngine/Engine/Binaries/Linux:$PATH' >> ~/.bashrc             # note the use of single quotes ' and the prefixing
$ source ~/.bashrc
```
You can now run `$ UE4Editor` from any folder/location 

### Build AirSim

The following steps build AirSim in just a few minutes (and throw plenty of warnings)
```
$ cd ~
$ git clone https://github.com/Microsoft/AirSim.git
$ cd AirSim
$ ./setup.sh                   # insert your password, if asked,; note that this will install clang-8 and python 2.7 among other Ubuntu packages
$ ./build.sh
```
Modify your `~/.bashrc` file to add the location of AirSim's Python APIs to the `PYTHONPATH` environmental variable
```
$ echo  'export PYTHONPATH=~/AirSim/PythonClient:$PYTHONPATH' >> ~/.bashrc                # note the use of single quotes ' and the prefixing
$ source ~/.bashrc
```
You can now use `>>> import airsim` in a Python interpreter from any folder/location 

### First use of the UE4Editor, Blocks environment, and Python APIs

Run the Unreal Engine 4 Editor from any folder by simply typing
```
$ UE4Editor
```
The first time, this might take a few minutes; when the UE4Editor start, to use the default "Blocks" environment, follow [these steps](https://microsoft.github.io/AirSim/build_linux/)
- Choose "Select or Create New Project"
- Click on "More", then "Browse"
- Navigate to `~/AirSim/Unreal/Environments/Blocks`
- Select `Blocks.uproject` and "Open"
- Choose "Convert Project", then "More options"
- Finally, "Convert in-place:
Note: the next time you run UE4Editor, Blocks will appear among the recent projects in the "Select or Create New Project" menu

You can dismiss the "New plugin" notification and close the UE4Editor interface tour; some shaders will still be compiling

**Important**: go to "Edit -> Editor Preferences"; in the "Search" box, type "CPU" and ensure that the "Use Less CPU when in Background" is unchecked

Wait for shaders to finish compiling, then click the "Play" button (or `Alt`+`p`)

The settings from `~/Documents/AirSim/settings.json` will be loaded (thus, you will see 2 drones if you followed the steps above)

`Fn`+`F1` will show the in-game menu; open a terminal (`Ctrl`+`Alt`+`t`) to run one of the Python examples
```
$ conda activate
$ python ~/drone0.py
```
Press `Esc` to end the simulation

### Option B: Compile an executable that uses AirSim's C++ APIs

The simplest way to use AirSim's [C++ APIs](https://microsoft.github.io/AirSim/apis_cpp/) is to duplicate one of the example projects (e.g. `~/AirSim/HelloDrone`) and use the same [CMake-based](https://cmake.org/) compiler tool chain

Copy `~/AirSim/HelloDrone` into a new folder called `NewDroneProject`
```
$ cp -r ~/AirSim/HelloDrone ~/AirSim/NewDroneProject
```
Remove Visual Studio's files and replace the content of `HelloDrone.cpp`
```
$ rm ~/AirSim/NewDroneProject/HelloDrone.vcxproj ~/AirSim/NewDroneProject/HelloDrone.vcxproj.filters
$ gedit ~/AirSim/NewDroneProject/HelloDrone.cpp
```
With the following lines
```
#include <iostream>
#include "vehicles/multirotor/api/MultirotorRpcLibClient.hpp"

int main() 
{
    using namespace std;
    msr::airlib::MultirotorRpcLibClient client;

    cout << "Press Enter to enable API control" << endl; cin.get();
    client.enableApiControl(true);

    cout << "Press Enter to arm the drone" << endl; cin.get();
    client.armDisarm(true);

    cout << "Press Enter to takeoff" << endl; cin.get();
    client.takeoffAsync(5)->waitOnLastTask();

    cout << "Press Enter to move 5 meters in x direction with 1 m/s velocity" << endl; cin.get();  
    auto position = client.getMultirotorState().getPosition(); // from current location
    client.moveToPositionAsync(position.x() + 5, position.y(), position.z(), 1)->waitOnLastTask();

    cout << "Press Enter to land" << endl; cin.get();
    client.landAsync()->waitOnLastTask();

    return 0;
}
```
Duplicate `HelloDrone`'s cmake folder into one called `~/AirSim/cmake/NewDroneProject`
```
$ cp -r ~/AirSim/cmake/HelloDrone ~/AirSim/cmake/NewDroneProject
```
Modify the `CMakeLists.txt` file in this folder by replacing the occurrences of `HelloDrone` with `NewDroneProject`
```
$ sed -i 's/HelloDrone/NewDroneProject/g' ~/AirSim/cmake/NewDroneProject/CMakeLists.txt
```
Add the name of this folder to the top level `CMakeLists.txt`
```
$ echo  'add_subdirectory("NewDroneProject")' >> ~/AirSim/cmake/CMakeLists.txt
```
Finally, setup and build AirSim again
```
$ cd ~/AirSim
$ ./setup.sh              # optional, if you had run it before
$ ./build.sh
```
The executable of `NewDroneProject` will be located in `~/AirSim/build_debug/output/bin/` and can be run as
```
$ ~/AirSim/build_debug/output/bin/NewDroneProject
```
Remember to first start the UE4Editor and Blocks—and press "Play"—for the `NewDroneProject` executable to connect

### Option C: using AirSim with ROS Melodic

AirSim's also provides a [ROS wrapper node around its C++ library called `airsim_node`](https://github.com/microsoft/AirSim/blob/master/docs/airsim_ros_pkgs.md)

#### Install ROS Melodic

First, install ROS Melodic following [these steps](https://wiki.ros.org/melodic/Installation/Ubuntu)
```
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
$ sudo apt update
$ sudo apt install ros-melodic-desktop-full
$ echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
$ sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
$ sudo apt install python-rosdep
$ sudo rosdep init
$ rosdep update
```
Note: while this guide focusses on Ubuntu 18 and ROS Melodic, as of June 2020, AirSim still works with Ubuntu 16 and [ROS Kinetic](http://wiki.ros.org/kinetic/Installation) as well

#### Build AirSim ROS nodes

Install additional packages and dependencies 
```
$ sudo apt install ros-melodic-mavros ros-melodic-mavros-extras
$ sudo apt-get install gcc-8 g++-8
```
Set `gcc8` as the [default `gcc`](https://stackoverflow.com/questions/7832892/how-to-change-the-default-gcc-compiler-in-ubuntu) in Ubuntu 18
```
$ sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 700 --slave /usr/bin/g++ g++ /usr/bin/g++-7
$ sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 800 --slave /usr/bin/g++ g++ /usr/bin/g++-8
```




------------------------------------

notes on debugging of the pd controller

eg pd_position_controller_simple.cpp
line 64 subscribes to "/airsim_node/odom_local_ned" but it should be "/airsim_node/VEHICLE_NAME/odom_local_ned"

>  think the yaw max velocity was used instead of the max z velocity. Double check lines 333 to 338 in pd_position_controller_simple.cpp , vel_cmd_.twist.angular.z should be replaced with vel_cmd_.twist.linear.z

check this issue from last month https://github.com/microsoft/AirSim/issues/2709

[note this pull req](https://github.com/microsoft/AirSim/pull/2743)

------------------------------------




Finally, build AirSim's ROS nodes; add to `~/.bashrc` and source the `~/AirSim/ros/` workspace
```
$ cd ~/AirSim/ros
$ catkin_make
$ echo  "source ~/AirSim/ros/devel/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
```

#### Launch AirSim ROS nodes

how to use 
[link](https://github.com/microsoft/AirSim/blob/master/docs/airsim_ros_pkgs.md)

3 main nodes
- wrapper around the c++ apis
- rviz
- pd controler (contains bugs, see minimal fix above)

```
$ roslaunch airsim_ros_pkgs airsim_node.launch
$ roslaunch airsim_ros_pkgs rviz.launch
```
3 provided examples in [link](https://github.com/microsoft/AirSim/blob/master/docs/airsim_tutorial_pkgs.md) (ignore build steps)

#### Use AirSim's ROS nodes' topics and services

http://wiki.ros.org/rostopic#rostopic_list
http://wiki.ros.org/rosservice#rosservice_list
```
$ rostopic list -v

Published topics:
 * /airsim_node/origin_geo_point [airsim_ros_pkgs/GPSYaw] 1 publisher
 * /airsim_node/Drone0/global_gps [sensor_msgs/NavSatFix] 1 publisher
 ...

Subscribed topics:
 * /airsim_node/all_robots/vel_cmd_body_frame [airsim_ros_pkgs/VelCmd] 1 subscriber
 * /airsim_node/Drone0/vel_cmd_body_frame [airsim_ros_pkgs/VelCmd] 1 subscriber
...

$ rosservice list -n

/airsim_node/Drone0/land /airsim_node
/airsim_node/Drone0/takeoff /airsim_node
...
```
using of services
```
$ rostopic echo /airsim_node/Drone0/global_gps

$ rosservice call /airsim_node/Drone0/takeoff 0
success: False
$ rosservice call /airsim_node/Drone0/land 0
success: False
```
tab to auto complete
```
$ rosservice call /airsim_node/Drone0/takeoff "waitOnLastTask: false" 
```
aaa
```
$ rosservice type /airsim_node/Drone0/takeoff | rossrv show
bool waitOnLastTask
---
bool success
```
notes on other launch files in `~/AirSim/ros/src/airsim_ros_pkgs/launch`
```
airsim_all.launch
airsim_node.launch
airsim_with_simple_PD_position_controller.launch
dynamic_constraints.launch
position_controller_simple.launch
rviz.launch
static_transforms.launch
```

----------------------------------------

Work in progress by [James Xu](https://github.com/Jamesjrxu/AirSim_doc)

## List of AirSim's Python APIs
See [Python_API.md](https://github.com/Jamesjrxu/AirSim_doc/blob/master/Python_API.md)


## List of AirSim's C++ APIs
See [CPP_API.md](https://github.com/Jamesjrxu/AirSim_doc/blob/master/CPP_API.md)


## List of AirSim's ROS topics and services 
See [ROS_Wrapper.md](https://github.com/Jamesjrxu/AirSim_doc/blob/master/ROS_Wrapper.md)

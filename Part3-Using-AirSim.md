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

Run the Africa environment again to see 2 drones in it (or neighborhood?)
```
$ ./Africa_001.sh  -ResX=640 -ResY=480 -windowed
```

> UE 4.24 uses Vulkan drivers by default, but they can consume more GPU memory. If you get memory allocation errors, then you can try switching to OpenGL using `-opengl`

noDisplay option
https://microsoft.github.io/AirSim/settings/#viewmode NoDisplay(?)

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
otherwise check this https://microsoft.github.io/AirSim/faq/#when-making-api-call-i-get-error

add one of these (?)
```
(base) pip install opencv-python
conda install opencv
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
```
{
  "SettingsVersion": 1.2,
  "CameraDefaults": {
      "CaptureSettings": [
        {
          "ImageType": 0,
          "Width": 256,
          "Height": 144,
          "FOV_Degrees": 90,
          "AutoExposureSpeed": 100,
          "MotionBlurAmount": 0
        }
    ]
  },
  "SimMode": "ComputerVision"
}
```

```
  Scene = 0, 
  # but also 
  DepthPlanner = 1, # ground truth 
  DepthPerspective = 2, # ground truth 
  DepthVis = 3, 
  DisparityNormalized = 4,
  Segmentation = 5,   # ground truth based on unreal meshes
  SurfaceNormals = 6,
  Infrared = 7 # TBD
```

use bottom camera, explain ids
move camera
```
airsim.wait_key('Press any key to set camera-0 gimble to 15-degree pitch')
client.simSetCameraOrientation("0", airsim.to_quaternion(0.261799, 0, 0)); #radians
```

png/rgb/float/pfm format apis
https://microsoft.github.io/AirSim/image_apis/
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



## Other stuff one can do with APIs/settings.json

mention
pausing
collision
time of day / lat, lon, sun position
weather
https://github.com/Microsoft/AirSim/blob/master/PythonClient/computer_vision/weather.py


clock speed
recoding

https://microsoft.github.io/AirSim/settings/

```
"Vehicles": {
    "FishEyeDrone": {
      "VehicleType": "SimpleFlight",
      "Cameras": {
        "front-center": {
          "CaptureSettings": [
            {
              "ImageType": 0,
              "FOV_Degrees": 120
            }
          ]
        }
      }
    }
}
```

px4 settings? (ignore for now)
https://microsoft.github.io/AirSim/settings/#additional-px4-settings



uninstall from (base)
```
pip uninstall airsim
```




setup and build Unreal / AirSim here..

## Compiling the Unreal Engine 4 and AirSim from source

recompiling airsim is required to modify the flight controller implementation
(note to self, but is it needed to re-compile UE4 or can we re-use binaries for that?)

in my case, i'm building outside the conda env

### UE4

required to build airsim

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
./setup.sh #insert your password, if asked, note that this will install clang-8 and python 2.7 among other ubuntu packages
./build.sh
```
throws plenty of warnings

## first use

- remove pip installed airsim if any an add build path to pythonpath

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

click play or Alt+p

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

`Alt` `p` again

new terminal

test api control

```
# If you are running you code from PythonClient folder in repo then you can also do this:
import setup_path 
import airsim
```





conda list -> no airsim

import airsim only works in ~/AirSim/PythonClient

to make it system wide

```
echo  'export PYTHONPATH=~/AirSim/PythonClient:$PYTHONPATH' >> ~/.bashrc # note prefixing and use of single quote '
source ~/.bashrc
```








### Using AirSim C++ APIs

use with C++
see includes and examples https://microsoft.github.io/AirSim/apis_cpp/
https://github.com/microsoft/AirSim/issues/758

copy ~/AirSim/HelloDrone into a new project folder
```
cp -r ~/AirSim/HelloDrone ~/AirSim/NewDroneProject
rm ~/AirSim/NewDroneProject/HelloDrone.vcxproj ~/AirSim/NewDroneProject/HelloDrone.vcxproj.filters
gedit ~/AirSim/NewDroneProject/HelloDrone.cpp
```
and replace content with the following

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

minor cmake changes
```
cp -r ~/AirSim/cmake/HelloDrone ~/AirSim/cmake/NewDroneProject
echo  'add_subdirectory("NewDroneProject")' >> ~/AirSim/cmake/CMakeLists.txt
sed -i 's/HelloDrone/NewDroneProject/g' ~/AirSim/cmake/NewDroneProject/CMakeLists.txt
```

nothing more but replacing the name in two places `project()` and `include_directories()`


```
setup.sh
build.sh
```
or just build if you already run setup










### Using AirSim and ROS Melodic

install ros steps (point below for installation from source)

https://wiki.ros.org/melodic/Installation/Ubuntu

```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo apt install ros-melodic-desktop-full
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
sudo apt install python-rosdep
sudo rosdep init
rosdep update
```

additional reqs
```
sudo apt install ros-melodic-mavros ros-melodic-mavros-extras
sudo apt-get install gcc-8 g++-8
```

set gcc8 as default
```
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 700 --slave /usr/bin/g++ g++ /usr/bin/g++-7
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 800 --slave /usr/bin/g++ g++ /usr/bin/g++-8
```
https://askubuntu.com/questions/1028601/install-gcc-8-only-on-ubuntu-18-04
https://stackoverflow.com/questions/7832892/how-to-change-the-default-gcc-compiler-in-ubuntu

requirements
build airsim and ros nodes

```
cd ~/AirSim/ros
catkin_make
```

```
source ~/AirSim/ros/devel/setup.bash
roslaunch airsim_ros_pkgs airsim_node.launch
```
```
source ~/AirSim/ros/devel/setup.bash
roslaunch airsim_ros_pkgs rviz.launch
```

provided examples

```
source ~/AirSim/ros/devel/setup.bash
```
or 
```
echo  "source ~/AirSim/ros/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```


any of these 3 example (but ignore the build steps)

https://github.com/microsoft/AirSim/blob/master/docs/airsim_tutorial_pkgs.md

how to use 
https://microsoft.github.io/AirSim/airsim_ros_pkgs/

add creating and compiling a new ros example

```
$ roslaunch airsim_ros_pkgs airsim_node.launch;
$ roslaunch airsim_ros_pkgs rviz.launch
```


http://wiki.ros.org/rostopic#rostopic_list
http://wiki.ros.org/rosservice#rosservice_list
```
jacopo@jacopo-ThinkPad-P52:~$ rostopic list -v

Published topics:
 * /move_base_simple/goal [geometry_msgs/PoseStamped] 1 publisher
 * /airsim_node/Drone1/global_gps [sensor_msgs/NavSatFix] 1 publisher
 * /rosout [rosgraph_msgs/Log] 3 publishers
 * /airsim_node/Drone1/odom_local_ned [nav_msgs/Odometry] 1 publisher
 * /tf [tf2_msgs/TFMessage] 2 publishers
 * /clicked_point [geometry_msgs/PointStamped] 1 publisher
 * /tf_static [tf2_msgs/TFMessage] 1 publisher
 * /initialpose [geometry_msgs/PoseWithCovarianceStamped] 1 publisher
 * /rosout_agg [rosgraph_msgs/Log] 1 publisher
 * /airsim_node/Drone0/odom_local_ned [nav_msgs/Odometry] 1 publisher
 * /airsim_node/origin_geo_point [airsim_ros_pkgs/GPSYaw] 1 publisher
 * /airsim_node/Drone0/global_gps [sensor_msgs/NavSatFix] 1 publisher

Subscribed topics:
 * /airsim_node/all_robots/vel_cmd_body_frame [airsim_ros_pkgs/VelCmd] 1 subscriber
 * /airsim_node/Drone0/vel_cmd_body_frame [airsim_ros_pkgs/VelCmd] 1 subscriber
 * /airsim_node/front_left_custom/DepthPlanner/registered/points [sensor_msgs/PointCloud2] 1 subscriber
 * /airsim_node/MyQuad/lidar/LidarCustom [sensor_msgs/PointCloud2] 1 subscriber
 * /rosout [rosgraph_msgs/Log] 1 subscriber
 * /airsim_node/group_of_obots/vel_cmd_world_frame [airsim_ros_pkgs/VelCmdGroup] 1 subscriber
 * /airsim_node/group_of_robots/vel_cmd_body_frame [airsim_ros_pkgs/VelCmdGroup] 1 subscriber
 * /tf_static [tf2_msgs/TFMessage] 1 subscriber
 * /airsim_node/Drone1/vel_cmd_body_frame [airsim_ros_pkgs/VelCmd] 1 subscriber
 * /airsim_node/all_robots/vel_cmd_world_frame [airsim_ros_pkgs/VelCmd] 1 subscriber
 * /airsim_node/Drone0/vel_cmd_world_frame [airsim_ros_pkgs/VelCmd] 1 subscriber
 * /tf [tf2_msgs/TFMessage] 1 subscriber
 * /airsim_node/gimbal_angle_quat_cmd [airsim_ros_pkgs/GimbalAngleQuatCmd] 1 subscriber
 * /airsim_node/gimbal_angle_euler_cmd [airsim_ros_pkgs/GimbalAngleEulerCmd] 1 subscriber
 * /airsim_node/Drone1/vel_cmd_world_frame [airsim_ros_pkgs/VelCmd] 1 subscriber
 * /airsim_node/MyQuad/odom_local_ned [nav_msgs/Odometry] 1 subscriber



jacopo@jacopo-ThinkPad-P52:~$ rosservice list -n

/airsim_node/Drone0/land /airsim_node
/airsim_node/Drone0/takeoff /airsim_node
/airsim_node/Drone1/land /airsim_node
/airsim_node/Drone1/takeoff /airsim_node
/airsim_node/all_robots/land /airsim_node
/airsim_node/all_robots/takeoff /airsim_node
/airsim_node/get_loggers /airsim_node
/airsim_node/group_of_robots/land /airsim_node
/airsim_node/group_of_robots/takeoff /airsim_node
/airsim_node/reset /airsim_node
/airsim_node/set_logger_level /airsim_node

/ned_to_enu_pub/get_loggers /ned_to_enu_pub
/ned_to_enu_pub/set_logger_level /ned_to_enu_pub

/rosout/get_loggers /rosout
/rosout/set_logger_level /rosout

/rviz/get_loggers /rviz
/rviz/load_config /rviz
/rviz/reload_shaders /rviz
/rviz/save_config /rviz
/rviz/set_logger_level /rviz
```

usage of services
```
rostopic echo /airsim_node/Drone0/global_gps

jacopo@jacopo-ThinkPad-P52:~$ rosservice call /airsim_node/Drone0/takeoff 0
success: False
jacopo@jacopo-ThinkPad-P52:~$ rosservice call /airsim_node/Drone0/land 0
success: False
```

tab to auto complete
```
 rosservice call /airsim_node/Drone0/takeoff "waitOnLastTask: false" 
```


```
rosservice type /airsim_node/Drone0/takeoff | rossrv show

jacopo@jacopo-ThinkPad-P52:~$ rosservice type /airsim_node/Drone0/takeoff | rossrv show
bool waitOnLastTask
---
bool success
```

note on other launch files but some seem wip

```
jacopo@jacopo-ThinkPad-P52:~/AirSim/ros/src/airsim_ros_pkgs/launch$ ls
airsim_all.launch
airsim_node.launch
airsim_with_simple_PD_position_controller.launch
dynamic_constraints.launch
position_controller_simple.launch
rviz.launch
static_transforms.launch
```

eg pd_position_controller_simple.cpp
line 64 subscribes to "/airsim_node/odom_local_ned" but it should be "/airsim_node/VEHICLE_NAME/odom_local_ned"

>  think the yaw max velocity was used instead of the max z velocity. Double check lines 333 to 338 in pd_position_controller_simple.cpp , vel_cmd_.twist.angular.z should be replaced with vel_cmd_.twist.linear.z



## List of AirSim Python APIs

make sure to disamibguate old and new apis https://microsoft.github.io/AirSim/upgrade_apis/

explain `duration` `max_wait_seconds` `Async` `join` etc

expalin drivetrain, yaw_mode, lookahead, and adaptive_lookahead

documenting the APIs with the help of James

https://github.com/microsoft/AirSim/blob/master/PythonClient/airsim/client.py

By default AirSim uses carrot following algorithm.

> Currently lowest level control available in AirSim is moveByAngleThrottleAsync

not true, as pointed out by James, https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/client.py#L793

sensors 
https://microsoft.github.io/AirSim/sensors/

lidar needs to be enabled in settings https://microsoft.github.io/AirSim/lidar/
example https://github.com/microsoft/AirSim/blob/master/PythonClient/multirotor/drone_lidar.py

## List of AirSim C++ APIs

documenting in full with the help of James

https://github.com/microsoft/AirSim/blob/master/AirLib/src/vehicles/multirotor/api/MultirotorApiBase.cpp

> A minimalist guide to  a few frameworks⁠—on Ubuntu and Vector computing⁠—for the person who was born yesterday
>> Written by a novice for the novice

# Part 4 - Building and Customizing AirSim

The following instructions are for a fresh install of Ubuntu 18.04 LTS 64-bit on a Lenovo P52 (i7-8850H/Quadro P2000)

Everything after a `$` is entered on a terminal; everything after `>>>` is passed to a Python interpreter



--------------
--------------
--------------



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

```
# If you are running you code from PythonClient folder in repo then you can also do this:
import setup_path 
import airsim
```




## Modifying AirSim

code structure
https://microsoft.github.io/AirSim/code_structure/

review the `.bat` and `.sh` scripts
https://microsoft.github.io/AirSim/dev_workflow/

essentially, build.sh copies the useful files to Blocks

> For Linux, make code changes in AirLib or Unreal/Plugins folder and then run ./build.sh to rebuild. This step also copies the build output to Blocks sample project. You can then follow above steps again to re-run.
https://microsoft.github.io/AirSim/unreal_blocks/

the FAQs are Windows/Visual Studio based
contemplate VS Code (?) https://code.visualstudio.com/docs/?dv=linux64_deb

### New Python APIs

example
https://github.com/Microsoft/AirSim/commit/f0e83c29e7685e1021185e3c95bfdaffb6cb85dc

### New C++ APIs

add printout of date of the most recent compilation

### Tuning `simpleflight` flight controller

https://microsoft.github.io/AirSim/flight_controller/ / https://microsoft.github.io/AirSim/simple_flight/

> We thus view flight controller simply as collection of algorithms packaged in a library. Another key emphasis is to develop this code as dependency free header-only pure standard C++11 code.

> Internally simple_flight uses cascade of PID controllers to finally generate actuator signals. 

> Please note that simple_slight currently doesn't support state estimator which means estimated and ground truth kinematics values would be same for simple_flight.

> We plan to add complimentary filter based state estimation for angular velocity and orientation using 2 sensors (gyroscope, accelerometer) in near future. In more longer term, we plan to integrate another library to do velocity and position estimation using 4 sensors (gyroscope, accelerometer, magnetometer and barometer) using EKF. If you have experience this area than we encourage you to engage with us and contribute!

> simple_flight uses steppable clock by default which means clock advances when simulator tells it to advance (unlike wall clock which advances strictly according to passage of time). Otherwise add `"ClockType": "ScalableClock"`

recompiling airsim
https://github.com/microsoft/AirSim/tree/master/AirLib/include/vehicles/multirotor









## Custom Unreal Engine 4 environments

needs Epic Games Launcher (Windows, macOS?) to create and Unreal project folder
https://microsoft.github.io/AirSim/unreal_custenv/

then just copy it over to your Linux machine (how many of the steps above can we move to Ubuntu?)


add notes on Updating Your Environment to Latest Version of AirSim

## Customizing the drone model

https://microsoft.github.io/AirSim/custom_drone/

### pyhsics and 3D model

use own model
https://microsoft.github.io/AirSim/settings/#pawnpaths

from 2017: https://github.com/Microsoft/AirSim/wiki/hexacopter
- use the same model
- does the physics code still exists?

For cars, we support only PhysX for now (regardless of value in this setting). For multirotors, we support "FastPhysicsEngine" only.










## Create new binaries

For custom environment/airsim
at once ore in separate steps?
TBD


















## (optional) ROS installation from source

TBD, if needed

## (alternative) Docker installation

TBD, if needed https://github.com/Microsoft/AirSim/blob/master/docs/docker_ubuntu.md
TBD

## (optional) PX4 flight controller

### SITL

https://microsoft.github.io/AirSim/px4_sitl/ /  https://microsoft.github.io/AirSim/px4_build/

px4 and mavlink
- https://github.com/Microsoft/AirSim/wiki/Intercepting-MavLink-messages
- https://microsoft.github.io/AirSim/px4_logging/
- https://microsoft.github.io/AirSim/mavlinkcom/

### HTIL 

left for later

with xbox controller https://microsoft.github.io/AirSim/xbox_controller/
on linux https://microsoft.github.io/AirSim/remote_control/
see "RC" under vehicle in `settings.json`

https://microsoft.github.io/AirSim/px4_setup/


> A minimalist guide to  a few frameworks⁠—on Ubuntu and Vector computing⁠—for the person who was born yesterday
>> Written by a novice for the novice

# Part 4 - Building and Customizing AirSim

The following instructions are for a fresh install of Ubuntu 18.04 LTS 64-bit on a Lenovo P52 (i7-8850H/Quadro P2000)

Everything after a `$` is entered on a terminal; everything after `>>>` is passed to a Python interpreter



--------------
--------------
--------------




## Headless AirSim on a remote server

TBD, ideally on Vector's cluster
example of distributed RL with Azure
https://github.com/microsoft/AutonomousDrivingCookbook/tree/master/DistributedRL



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

multirotor model, etc.
https://github.com/microsoft/AirSim/blob/master/AirLib/include/vehicles/multirotor/MultiRotorParams.hpp

https://github.com/microsoft/AirSim/blob/master/AirLib/include/vehicles/multirotor/firmwares/simple_flight/SimpleFlightQuadXParams.hpp









## Custom Unreal Engine 4 environments

needs Epic Games Launcher (Windows, macOS?) to create and Unreal project folder
https://microsoft.github.io/AirSim/unreal_custenv/

download (on mac or win)
https://www.epicgames.com/unrealtournament/en-US/download
run Epic Games Launcher
login with your epic games account
unreal engine tab in the left
learn tab on top
find content with download
e.g sun temple or blueprints under "Engine Features Samples"
click the "free" button and then "create project"
select UE4 v 4.24 
(if you haven't installed it the number will be red and say "The selected engine association is not valid.", ignore it)
accept the default download folder typically under ~/Documents/Unreal Projects/
accept the license agreement

copy the folder "e.g. ~/Documents/Unreal Projects/Sun Temple to your ubuntu machine

open the .uproject (e.g. SunTemple.uproject) with Unreal Engine Editor
you will be asked to confirm the location of the UE editor (e.g. /home/$USER/UnrealEngine/)

From the File menu select New C++ class, leave default None on the type of class, click Next, leave default name MyClass, and click Create Class. 
We need to do this because Unreal requires at least one source file in project. 
This will trigger C++ compilation of the project
add Binaries, Source folders, Makefile, CMakeLists.txt files (and more) in folder /SunTemple

close UE4Editor

copy folder Plugins ~/AirSim/Unreal/Plugins inside folder SunTemple/

replace the content of SunTemple.uproject with 
```
{
    "FileVersion": 3,
    "EngineAssociation": "4.24",
    "Category": "Samples",
    "Description": "",
    "Modules": [
        {
            "Name": "SunTemple",
            "Type": "Runtime",
            "LoadingPhase": "Default",
            "AdditionalDependencies": [
                "AirSim"
            ]
        }
    ],
    "TargetPlatforms": [
        "MacNoEditor",
        "WindowsNoEditor",
    ],
    "Plugins": [
        {
            "Name": "AirSim",
            "Enabled": true
        }
    ]
}
```

open .uproject again, confirm location of the Uengine binaries again

you will be asked to rebuild the airsim module, click yes

on the bottom right you might see a dialogue about new plugins, if you click manage plugins it shoudl show airsim
(and it is enabled)

in the world outliner search bar (should be on the top right by default)
search player start, click to show properties (i.e. the position where to spawn vehicles in airsim)

in SunTemple it exists already but you shold create it otherwise https://docs.unrealengine.com/en-US/Engine/Actors/PlayerStart/index.html

then click Window -> World Settings
in the menu that will appear on the right, set set the GameMode Override to AirSimGameMode

remember to 
Go to 'Edit->Editor Preferences' in Unreal Editor, in the 'Search' box type 'CPU' and ensure that the 'Use Less CPU when in Background' is unchecked. If you don't do this then UE will be slowed down dramatically when UE window loses focus.

save (ctrl shift s)

press alt p or the play button to load the config an vehicles in settings.json
use the python/c++ apis or ros wrapper to control the vehicles

if/when you modify or update AirSim, remember to replace the Plugins folder in the project 


### Alternative: create UE4 project from scratch https://docs.unrealengine.com/en-US/Engine/Basics/Projects/Browser/index.html

run UE4Editor
New Project Categories -> Games
Select Template -> Blank
Project Settings -> arrow right of Blueprint and choose C++; arrow right of With Starter Content and choose No Starter Content; also select folder/location and name for this empty project

once the project is created 
open it (.uproject file with UE4Editor, note you do not need to add a New C++ Class this time

click yes if asked to recompile

close UE4Editor

copy folder Plugins ~/AirSim/Unreal/Plugins inside folder MyProject/

replace the content of MyProject.uproject with (note that you only change the Name field under Modules
```
{
    "FileVersion": 3,
    "EngineAssociation": "4.24",
    "Category": "Samples",
    "Description": "",
    "Modules": [
        {
            "Name": "MyProject",
            "Type": "Runtime",
            "LoadingPhase": "Default",
            "AdditionalDependencies": [
                "AirSim"
            ]
        }
    ],
    "TargetPlatforms": [
        "MacNoEditor",
        "WindowsNoEditor",
    ],
    "Plugins": [
        {
            "Name": "AirSim",
            "Enabled": true
        }
    ]
}
```

open uproject with UE4Editor again, confirm location of UE4Editor binaries again

confirm rebuilding of airsim

on the bottom right you might see a dialogue about new plugins, if you click manage plugins it shoudl show airsim
(and it is enabled)

in the world outliner search bar (should be on the top right by default)
search player start, click to show the new tab "Details"
the position where to spawn vehicles in airsim is under "Transform"

again, it should already exist

then click Window -> World Settings
in the menu that will appear on the right, set set the GameMode Override to AirSimGameMode

remember to 
Go to 'Edit->Editor Preferences' in Unreal Editor, in the 'Search' box type 'CPU' and ensure that the 'Use Less CPU when in Background' is unchecked. If you don't do this then UE will be slowed down dramatically when UE window loses focus.

save (ctrl shift s)

you will be asked to prompt a name for the asset to be saved under /MyProject/Content/

press alt p or the play button to load the config an vehicles in settings.json
use the python/c++ apis or ros wrapper to control the vehicles

if/when you modify or update AirSim, remember to replace the Plugins folder in the project 

### Alternative 2: create UE4 project from scratch and add assets from Epic Games Launcher/Marketplace

#### on ubuntu 

run UE4Editor
New Project Categories -> Games
Select Template -> Blank
Project Settings -> arrow right of Blueprint and choose C++; arrow right of With Starter Content and choose No Starter Content; also select folder/location and name for this empty project

once the project is created 
open it (.uproject file with UE4Editor, note you do not need to add a New C++ Class this time

click yes if asked to recompile

close UE4Editor

copy the complete project folder over to the computer running epic games launcher

#### on mac/win with epic games launcher

copy the empty project folder to where you would download assets/projects
~/Documents/Unreal Projects

run epic games launcher;
unreal engine (on the left menu);
marketplace (on the top menu)

select a free environment like Infinity Blade: Hideout

click "add to project";
check "Show all projects";
select "MyProject";
choose 4.24 under "Select version:";
wait for the content to download/verify/install;

copy back the folder to ubuntu

#### on ubuntu




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


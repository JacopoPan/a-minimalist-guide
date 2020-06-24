> A minimalist guide to  a few frameworks⁠—on Ubuntu and Vector computing⁠—for the person who was born yesterday
>> Written by a novice for the novice

# Part 4 - Building and Customizing AirSim

The following instructions are for a fresh install of Ubuntu 18.04 LTS 64-bit on a Lenovo P52 (i7-8850H/Quadro P2000)

Everything after a `$` is entered on a terminal; everything after `>>>` is passed to a Python interpreter



## Custom Unreal Engine 4 environments

### Create UE4 project from scratch 

ubuntu only

[create projects](https://docs.unrealengine.com/en-US/Engine/Basics/Projects/Browser/index.html)

- run UE4Editor
- New Project Categories -> Games
- Select Template -> Blank
- Project Settings -> arrow right of Blueprint and choose C++; arrow right of With Starter Content and choose No Starter Content; also select folder/location and - name for this empty project

once the project is created 
- open it (.uproject file with UE4Editor, note you do not need to add a New C++ Class this time
- click yes if asked to recompile
- close UE4Editor
- copy folder Plugins ~/AirSim/Unreal/Plugins inside folder MyProject/
```
$ cp
```
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
- open uproject with UE4Editor again, confirm location of UE4Editor binaries again
- confirm rebuilding of airsim

on the bottom right you might see a dialogue about new plugins
- if you click manage plugins it shoudl show airsim (and it is enabled)

in the world outliner search bar (should be on the top right by default)
- search player start, click to show the new tab "Details"
- the position where to spawn vehicles in airsim is under "Transform" (again, it should already exist)

then click Window -> World Settings
- in the menu that will appear on the right, set set the GameMode Override to AirSimGameMode
- save (ctrl shift s)

??? you will be asked to prompt a name for the level to be saved under /MyProject/Content/

to make it the default start (now that you have set its game mode)
- Edit -> Project Settings -> Maps & Modes
- Default Maps -> Editor Startup Map
- choose "the name you have given to the level just above"

(you can set DefaultGameMode to AirSimGameMode and the Game Default Map to DemoMap1, if you like)
- save again (ctrl shift s)
- press alt p or the play button to load the config an vehicles in settings.json
- use the python/c++ apis or ros wrapper to control the vehicles

always remember 1
Go to 'Edit->Editor Preferences' in Unreal Editor, in the 'Search' box type 'CPU' and ensure that the 'Use Less CPU when in Background' is unchecked. If you don't do this then UE will be slowed down dramatically when UE window loses focus.

always remember 2 
if/when you modify or update AirSim, remember to replace the Plugins folder in the project 

### Create UE4 project from scratch and add assets from Marketplace with Epic Games Launcher

needs ubuntu and either a win or mac machine (or a 3rd party solution doing the same as Epic Games Launcher)

#### on ubuntu 

- run UE4Editor
- New Project Categories -> Games
- Select Template -> Blank
- Project Settings -> arrow right of Blueprint and choose C++; arrow right of With Starter Content and choose No Starter Content; also select folder/location and name for this empty project

once the project is created 
- open it (.uproject file with UE4Editor, note you do not need to add a New C++ Class this time
- click yes if asked to recompile
- close UE4Editor
- copy the complete project folder over to the computer running epic games launcher

#### on mac/win with epic games launcher

- copy the empty project folder to where you would download assets/projects, e.g., `~/Documents/Unreal Projects`
- run epic games launcher;
- unreal engine (on the left menu);
- marketplace (on the top menu)
- select a free environment like Infinity Blade: Hideout
- click "add to project";
- check "Show all projects";
- select "MyProject";
- choose 4.24 under "Select version:";
- wait for the content to download/verify/install;
- copy back the folder to ubuntu

altenratively download a complete project from the learn tab
- learn tab on top
- find content with download
e.g sun temple or blueprints under "Engine Features Samples"
- click the "free" button and then "create project"
- select UE4 v 4.24 
(if you haven't installed it the number will be red and say "The selected engine association is not valid.", ignore it)
- accept the default download folder typically under ~/Documents/Unreal Projects/
- accept the license agreement
- copy the folder "e.g. ~/Documents/Unreal Projects/Sun Temple to your ubuntu machine

#### on ubuntu

- copy folder Plugins ~/AirSim/Unreal/Plugins inside folder MyProject/
- replace the content of MyProject.uproject with (note that you only change the Name field under Modules
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
troubleshoot, if you copied from mac, remove `._` files
```
jacopo@jacopo-ThinkPad-P52:~/Documents/Unreal Projects/MyProject/Source$ rm ._MyProject*
```
[link](https://apple.stackexchange.com/questions/14980/why-are-dot-underscore-files-created-and-how-can-i-avoid-them)

- open uproject with UE4Editor again, confirm location of UE4Editor binaries again
- confirm rebuilding of airsim AND the project MyProject itself
- on the bottom right you might see a dialogue about new plugins, if you click manage plugins it shoudl show airsim
(and it is enabled)

- in the Content tab (should be on the bottom of the screen or find it from the window menu)
- select EnvironmentPack3 -> Maps
- then DemoMap1

in the world outliner search bar (should be on the top right by default)
- search player start, click to show the new tab "Details"
- the position where to spawn vehicles in airsim is under "Transform"
again, it should already exist (create it otherwise)

then click Window -> World Settings
- in the menu that will appear on the right, set set the GameMode Override to AirSimGameMode

to make it the default start (now that you have set its game mode)
- Edit -> Project Settings -> Maps & Modes
- Default Maps -> Editor Startup Map
- choose DemoMap1

(you can set DefaultGameMode to AirSimGameMode and the Game Default Map to DemoMap1, if you like)
- save again (ctrl shift s)
- press alt p or the play button to load the config an vehicles in settings.json
- use the python/c++ apis or ros wrapper to control the vehicles

always remember 1
Go to 'Edit->Editor Preferences' in Unreal Editor, in the 'Search' box type 'CPU' and ensure that the 'Use Less CPU when in Background' is unchecked. If you don't do this then UE will be slowed down dramatically when UE window loses focus.

always remember 2 
if/when you modify or update AirSim, remember to replace the Plugins folder in the project 

## Custmom vehicle mesh

e.g. the hexacopter 3d model from https://github.com/Microsoft/AirSim/wiki/hexacopter
```
wget https://github.com/Microsoft/AirSim/wiki/images/DJI%20S900.zip
```
the .obj static mesh of this model https://grabcad.com/library/dji-s900-hex-rotor-drone-1 
in step format https://en.wikipedia.org/wiki/ISO_10303-21

use custom model
https://microsoft.github.io/AirSim/settings/#pawnpaths

> This allows you to specify your own vehicle pawn blueprints, for example, you can replace the default car in AirSim with your own car. 

> Your vehicle BP can reside in Content folder of your own Unreal project (i.e. outside of AirSim plugin folder). For example, if you have a car BP located in file Content\MyCar\MySedanBP.uasset in your project then you can set "DefaultCar": {"PawnBP":"Class'/Game/MyCar/MySedanBP.MySedanBP_C'"}. 

> The XYZ.XYZ_C is a special notation required to specify class for BP XYZ. 

> Please note that your BP must be derived from CarPawn class. By default this is not the case but you can re-parent the BP using the "Class Settings" button in toolbar in UE editor after you open the BP and then choosing "Car Pawn" for Parent Class settings in Class Options. 

> It's also a good idea to disable "Auto Possess Player" and "Auto Possess AI" as well as set AI Controller Class to None in BP details. Please make sure your asset is included for cooking in packaging options if you are creating binary.


within your project (with AirSim) copy MyProject/Plugin/AirSim/Content/Blueprints/BP_FlyingPawn.uasset
to MyProject/Content

open the project

import the static mesh and propellers;
replace BP_FlyingPawn' static mesh
edit the mesh (scale, rotate, add propellers, etc)

edit `settings.json` adding
```
  "PawnPaths": {
    "DefaultQuadrotor": {"PawnBP": "Class'/Game/BP_FlyingPawn.BP_FlyingPawn_C'"}
  },
```

`/Game/BP_FlyingPawn.BP_FlyingPawn_C` will lead to the use of the the model in `MyProject/Content/BP_FlyingPawn.uasset`

note that re-naming won't work (where to change this

refer to these issues as well
https://github.com/microsoft/AirSim/issues/627
https://github.com/microsoft/AirSim/issues/1506







## Custom vehicle pyhsical properties

> For cars, we support only PhysX for now (regardless of value in this setting). For multirotors, we support "FastPhysicsEngine" only.

You can create new config like this for physics parameters: https://github.com/Microsoft/AirSim/blob/v1.1.10/AirLib/include/vehicles/multirotor/configs/SimpleFlightQuadX.hpp

transfer px4 hex physics to simple flight 
https://github.com/Microsoft/AirSim/wiki/hexacopter

also see this pull request
https://github.com/microsoft/AirSim/pull/1890









## Modifying AirSim APIs and controllers

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

### `simpleflight` flight controller

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

#### adding state estimation

potential project
- https://github.com/microsoft/AirSim/blob/master/docs/simple_flight.md#state-estimation
- https://github.com/microsoft/AirSim/blob/master/AirLib/include/vehicles/multirotor/firmwares/simple_flight/AirSimSimpleFlightEstimator.hpp
- https://github.com/microsoft/AirSim/blob/master/AirLib/include/vehicles/multirotor/firmwares/simple_flight/AirSimSimpleFlightBoard.hpp





### PX4 flight controller

#### SITL

https://microsoft.github.io/AirSim/px4_sitl/ 

https://microsoft.github.io/AirSim/px4_build/

https://github.com/microsoft/AirSim/issues/2647

px4 and mavlink
- https://github.com/Microsoft/AirSim/wiki/Intercepting-MavLink-messages
- https://microsoft.github.io/AirSim/px4_logging/
- https://microsoft.github.io/AirSim/mavlinkcom/







## Packaging custom UE4 environments and AirSim

For custom environment/airsim

https://docs.unrealengine.com/en-US/Engine/Basics/Projects/Packaging/index.html






--------------
--------------
--------------
--------------

## (TBD) HTIL 

left for later

with xbox controller https://microsoft.github.io/AirSim/xbox_controller/
on linux https://microsoft.github.io/AirSim/remote_control/
see "RC" under vehicle in `settings.json`

https://microsoft.github.io/AirSim/px4_setup/

real custom drone: 
https://microsoft.github.io/AirSim/custom_drone/

## (TBD) Headless AirSim on a remote server

TBD, ideally on Vector's cluster
example of distributed RL with Azure
https://github.com/microsoft/AutonomousDrivingCookbook/tree/master/DistributedRL

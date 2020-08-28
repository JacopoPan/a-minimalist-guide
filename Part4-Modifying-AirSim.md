> A minimalist guide to  a few frameworks⁠—on Ubuntu and Vector computing⁠—for the person who was born yesterday
>> Written by a novice for the novice

# Part 4 - Building and Customizing AirSim

The following instructions are for a fresh install of Ubuntu 18.04 LTS 64-bit on a Lenovo P52 (i7-8850H/Quadro P2000)

Everything after a `$` is entered on a terminal; everything after `>>>` is passed to a Python interpreter


## Custom Unreal Engine 4 environments

[AirSim](https://github.com/microsoft/AirSim) is packaged as an [Unreal Engine 4 Plugin](https://docs.unrealengine.com/en-US/Programming/Plugins/index.html)
and it can be added to essentially any new UE4 project

### Create a UE4 project with AirSim's plugin from scratch 

On Ubuntu, one can create a [new UE4 project](https://docs.unrealengine.com/en-US/Engine/Basics/Projects/Browser/index.html) from scratch and add AirSim's plugin as follows 

- Start the `UE4Editor` (if you followed [Part 3](https://github.com/JacopoPan/a-minimalist-guide/blob/master/Part3-Using-AirSim.md), type `$ UE4Editor` in your terminal)
- On the "Select or Create New Project" menu, under "New Project Categories", choose "Games" and click "Next"
- On the "Select Template" menu, pick "Blank" and click "Next"
- On the "Project Settings" menu, open the dropdown menu of the "Blueprint" tile and choose "C++" instead
- On the same menu,  open the dropdown menu of the "With Starter Content" tile and choose "No Starter Content"
- On the same menu, pick a folder (e.g. `~/Documents/Unreal\ Projects`) and name (e.g. [`Oxcart`](https://www.cia.gov/library/readingroom/docs/DOC_0001458639.pdf)) for the project
- Click on "Create Project"
- Once the project is created, navigate to the folder where it was created (`~/Documents/Unreal\ Projects/Oxcart`)
- Open file `Oxcart.uproject` with the Unreal Engine Editor (default or select by right click)
- If you are prompted for "Missing Modules" and asked "Would you like to rebuild them now?", choose "Yes"
- Close the Unreal Engine Editor
- Copy AirSim's Unreal Plugins folder into the new project
```
$ cp -r ~/AirSim/Unreal/Plugins ~/Documents/Unreal\ Projects/Oxcart
```
- Open `Oxcart.uproject` with a text editor
```
$ gedit ~/Documents/Unreal\ Projects/Oxcart/Oxcart.uproject
```
- Replace its content with the following (making sure that `"Name"` under `"Modules"` matches the project)
```
{
    "FileVersion": 3,
    "EngineAssociation": "4.24",
    "Category": "Samples",
    "Description": "",
    "Modules": [
        {
            "Name": "Oxcart",
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
- Open `Oxcart.uproject` with the Unreal Engine Editor again
- On menu "Select Unreal Engine Verion", confirm the location of your UE4's build (usually `~/UnrealEngine`), click "Ok"
- If you are prompted for "Missing Modules" (AirSim in this case) and asked "Would you like to rebuild them now?", choose "Yes"
- When the Editor launches, you'll see a prompt "New plugins are available" on the bottom right of the screen
- Clicking on "Manage plugins" will open a menu showing that AirSim is *installed* and *enabled* (close this menu)
- In the "World Outliner" level editor (top right by default or under the "Window" menu) search bar, type "Player Start"
- Click on the "Player Start" result to open the "Details" tab
- The origin position for AirSim's vehicles is the "Location" under "Transform"
- If a "Player Start" does not exist, add it from "Modes" tab (on the top left)
- From the "Window" dropdown menu, click on "World Settings"
- In the "GameMode Override" dropdown menu, select "AirSimGameMode"
- Save the project (`Ctrl`+`s`)
- You will be prompted to save the level with a name (e.g. `OxcartLvl1`) under `~/Documents/Unreal\ Projects/Oxcart/Content`, click "Save"
- Make this level the default start: from menu "Edit" select "Project Settings"
- On the left of the new window, under "Project", select "Maps & Modes"
- On the right, under "Default Maps", select `OxcartLvl1` from the dropdown menu for the "Editor Startup Map"
- Also make "AirSimGameMode" the "Default GameMode" and `OxcartLvl1` the "Game Default Map", if desired
- Close the "Project Settings" menu, save the project (`Ctrl`+`s`)

The project can now be used as an AirSim environemnt, pressing "Play" (`Alt`+`p`) will load the AirSim vehicles and options in `~/Documents/AirSim/settings.json`

**Note**:
Go to 'Edit->Editor Preferences' in Unreal Editor, in the 'Search' box type 'CPU' and ensure that the 'Use Less CPU when in Background' is unchecked. If you don't do this then UE will be slowed down dramatically when UE window loses focus.

**Note**:
if/when you modify or update AirSim, remember to replace the Plugins folder in the project 
```
$ 
```





### Assets from Epic Games Launcher's Marketplace 

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

identical up to line XYZ

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
(if you havent installed it the number will be red and say "The selected engine association is not valid.", ignore it)

- accept the default download folder typically under ~/Documents/Unreal Projects/
- accept the license agreement
- copy the folder "e.g. `~/Documents/Unreal Projects/Sun Temple` to your ubuntu machine


#### on ubuntu

identical from line XYZ

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





## Custom vehicle mesh

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







## AirSim on a remote server

e.g. on Vector's cluster
- https://github.com/microsoft/AirSim-NeurIPS2019-Drone-Racing/issues/112
- https://github.com/microsoft/AirSim/issues/1224
- https://github.com/microsoft/AirSim-NeurIPS2019-Drone-Racing/issues/64







## Packaging custom UE4 environments and AirSim

For custom environment/airsim https://docs.unrealengine.com/en-US/Engine/Basics/Projects/Packaging/index.html








--------

## Additional readings


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

example: pull request changing cameraOrientation to cameraPose https://github.com/microsoft/AirSim/pull/2710

### New Python APIs

example https://github.com/Microsoft/AirSim/commit/f0e83c29e7685e1021185e3c95bfdaffb6cb85dc


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

## PX4 flight controller

### SITL
- https://microsoft.github.io/AirSim/px4_sitl/ 
- https://microsoft.github.io/AirSim/px4_build/
- https://github.com/microsoft/AirSim/issues/2647

px4 and mavlink
- https://github.com/Microsoft/AirSim/wiki/Intercepting-MavLink-messages
- https://microsoft.github.io/AirSim/px4_logging/
- https://microsoft.github.io/AirSim/mavlinkcom/

## HTIL 
- [PX4](https://microsoft.github.io/AirSim/px4_setup/)
- [Custom drone](https://microsoft.github.io/AirSim/custom_drone/)


-------

move to part 2

## Checkpoints

- [Checkpoints](https://support.vectorinstitute.ai/CheckpointRestartInstructions), [about `v`](https://support.vectorinstitute.ai/AboutVaughan2), symlinks, etc.

## Viz

- [Viz](https://support.vectorinstitute.ai/wandb), `$ /usr/local/bin/usageStats.sh`

## Jupyer Notebooks

- [Link 1](https://support.vectorinstitute.ai/jupyter_notebook), [link 2](https://jupyter.org/install), [link 3](https://jupyter.readthedocs.io/en/latest/running.html#running)

## MuJoCo, PyBullet

- [MuJoCo](https://github.com/openai/mujoco-py/). [Vector link 1](https://support.vectorinstitute.ai/mujoco_updated), [link 2](https://support.vectorinstitute.ai/SoftwareVaughan)
- [PyBullet](https://pybullet.org/wordpress/) gym-pybullet-drones



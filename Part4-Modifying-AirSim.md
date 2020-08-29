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
- You will be prompted to save the level with a name (e.g. `OxcartLvl1`) under `Unreal\ Projects/Oxcart/Content`, click "Save"
- Make this level the default start: from menu "Edit" select "Project Settings"
- On the left of the new window, under "Project", select "Maps & Modes"
- On the right, under "Default Maps", select `OxcartLvl1` from the dropdown menu for the "Editor Startup Map"
- Also make "AirSimGameMode" the "Default GameMode" and `OxcartLvl1` the "Game Default Map", if desired
- Close the "Project Settings" menu, save the project (`Ctrl`+`s`)

The project can now be used as an AirSim environemnt, pressing "Play" (`Alt`+`p`) will load the AirSim vehicles and options in `~/Documents/AirSim/settings.json`

**Note**, always remember to **uncheck** option 'Use Less CPU when in Background': "Edit", "Editor Preferences", then search for 'CPU' to show the option

**Note**, when you modify or **update** AirSim, you should replace (and rebuild) the `AirSim` folder under the `Plugins` folder of your project






### Assets from Epic Games Launcher's Marketplace 

Grabbing assets (models, maps, levels) from [Unreal Engine's Marketplace](https://unrealengine.com/marketplace/en-US/store) requires [Epic Games Launcher](https://www.epicgames.com/store/en-US/download) which is only available for Windows and macOS (even though [3rd party solutions for Linux exist](https://lutris.net/games/epic-games-store/)) 

To *add assets* to a project
- Create an empty project as show in the previous section (i.e., the first 11 bullet points)
- Copy the entire project folder to the (Windows or macOS) computer running "Epic Games Launcher"
- Start "Epic Games Launcher"
- On the left, select "Unreal Engine"
- On the top, select "Marketplace"
- Find a free environment (e.g. "Infinity Blade: Hideout")
- Click on "Add to project"
- Use "Show all projects" to select "YourProjectName" (e.g. `Oxcart`);
- Under "Select version:", choose "4.24" (UE4 version used by AirSim at the time of this writing)
- Wait for the content to download, verify, and install
- You can now copy back the entire project folder to an Ubuntu machine

Alternatively, to *obtain a complete project* from the "Learn" tab
- Follow the first 4 steps in the previous list
- On the top, select "Learn"
- Find content with dowload (e.g. "Sun Temple" under "Engine Features Samples")
- Click the "Free" button and "Create project"
- Select "UE4 v4.24" (if UE4 is not installed on the computer used for the downlaod the number will be red and say "The selected engine association is not valid.", you can ignore the warning)
- Accept the default download folder (`~/Documents/Unreal\ Projects/`) and licence agreement
- You can now copy back the entire project folder to an Ubuntu machine

Then, follow the bullet points from the 12th on from the previous section (i.e., "Copy AirSim's Unreal Plugins folder..")

The "Content" tab (at the bottom or under "Window") will have the new assets

E.g. for "Infinity Blade: Hideout", `EnvironmentPack3` -> `Maps` -> `DemoMap1`

You can make `DemoMap1` the default "Editor Startup Map" and "Game Startup Map" under "Project Settings" -> "Maps & Modes"

**Troubleshoot**: if you copied files from  macOS, remember to remove [`._` files](https://apple.stackexchange.com/questions/14980/why-are-dot-underscore-files-created-and-how-can-i-avoid-them) to avoid build errors














## Custom vehicle mesh

rememver the pgup, pgdn, keys and right click+mouse for panning

e.g. the hexacopter 3d model usere [here](https://github.com/Microsoft/AirSim/wiki/hexacopter)
```
$ wget https://github.com/Microsoft/AirSim/wiki/images/DJI%20S900.zip
```

unzip

within the project to which you added AirSim make a copy of
`Oxcart/Plugin/AirSim/Content/Blueprints/BP_FlyingPawn.uasset`
to `Oxcart/Content`

open the project iwith the unreal engine editor

"Import" to Oxcart/Content from tab "Content Browser" the two obj files

in the "FBX Import Options" menu select "Import All"

the "Message Log" will show 3 warnings, ignore them

the DJI_S900, DJI_MotorProp, defaultMat as well as 
BP_FlyingPawn will appear on the Content Browser at the bottom

double click on folder DJI_S900, right click DJI_S900 and select "Edit.."

in the "Details" tab on the right, scroll down to "Import Settings" and set the "X" value of "Import Rotation" to 90

the click on the "Asset" dropdown menu at the top and "Reimport DJI_S900", this should fix the orientation of the mesh

save and close DJI_S900

repeat these steps to rotate by 90 degrees DJI_MotorProp as well

for DJI_MotorProp, under "Transform" set the X and Y of "Import Translation" to 200 and -345, respectively

(this will center the pivot frame wrt the propeller)

if you want, make "defaultMat" a differnt color
right clikc "Edit.."
select "Param", on the "Details" tab, find "Material Expression Vector Parameter" and modify "Default Value"
connecto the the "Metallic" option in the "defaultMat" tile, if desired
save and close defaultMat

go back to the "Content" folder in the "Content Browser"

right click on BP_FlyingPawn and "Edit.."

under "Components" on the left, select "BodyMesh"

on the left, under "Static Mesh" open the dropdown menu saying "Quadrotor1" and select "DJI_S900"

under "Transform", set the 3 values besides "Scale" to .2

click on  "Prop3" "Prop2" "Prop1" "Prop0" and change their "Static Mesh" for "DJI_MotorProp"

use the "Viewport" for place the 6 propellers in the right positions on each arm

change the "Position Grid Snap" value from 10 to 1 

edit `settings.json` adding https://microsoft.github.io/AirSim/settings/#pawnpaths
```
  "PawnPaths": {
    "DefaultQuadrotor": {"PawnBP": "Class'/Game/BP_FlyingPawn.BP_FlyingPawn_C'"}
  },
```

> Note: `/Game/BP_FlyingPawn.BP_FlyingPawn_C` will lead to the use of the the model in `MyProject/Content/BP_FlyingPawn.uasset`
> The XYZ.XYZ_C is a special notation required to specify class for BP XYZ. 
> Please note that your BP must be derived from CarPawn class. By default this is not the case but you can re-parent the BP using the "Class Settings" button in toolbar in UE editor after you open the BP and then choosing "Car Pawn" for Parent Class settings in Class Options. 

> It's also a good idea to disable "Auto Possess Player" and "Auto Possess AI" as well as set AI Controller Class to None in BP details. Please make sure your asset is included for cooking in packaging options if you are creating binary.


how to use 6 propellers,
also see https://github.com/microsoft/AirSim/pull/1890/files










## Packaging custom UE4 environments and AirSim

See [these instructons](https://docs.unrealengine.com/en-US/Engine/Basics/Projects/Packaging/index.html)

## AirSim on a remote server

e.g. on Vector's cluster

```
$ DISPLAY= ./AirSimExe.sh -opengl4
or 
$ ./AirSimExe.sh -nullrhi - not that if you call simGetImages with -nullrhi option, it would result in an error.
```
https://github.com/microsoft/AirSim-NeurIPS2019-Drone-Racing/issues/112

**multiple instances**
set "LocalHostIp": "127.0.0.1",  "127.0.0.2", etc

AirSim gives higher priority to a settings.json lying in the same directory as the linux/windows unreal binary, as compared to the one lying in /home/$USER/Documents/AirSim/settings.json

So, one way to do this is to copy paste the unreal binaries, and have different settings.json in each binary folder.

For example, you can place a settings.json in
PATH_TO/AirSim_1/AirSimExe/Binaries/Linux/settings.json, with a particular port number, and when you run it with ./AirSim_1/AirSimExe.sh -windowed

And then you can copy-paste the unreal engine binaries:
PATH_TO/AirSim_2/AirSimExe/Binaries/Linux/settings.json, with a new port number, and when you run it with ./AirSim_2/AirSimExe.sh -windowed it should use the new port number

https://github.com/microsoft/AirSim-NeurIPS2019-Drone-Racing/issues/64




## Modifying AirSim's source

links

how to recompile

reminders of what to change

# PX4 SITL

https://github.com/microsoft/AirSim/blob/master/docs/px4_sitl.md










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



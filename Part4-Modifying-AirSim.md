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
    "Category": "",
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

Replacing a vehicle's mesh can be done within the Unreal Engine Editor an modifying `settings.json`

Adding simple functionalities (e.g. the spin motion of additional propellers) requires to edit AirSim's plugin source and re-build an environment

The simplest way to do so is by using the Blocks environment located in `~/AirSim/Unreal/Environments/Blocks/`

Modify the code in `~/AirSim/Unreal/Plugins/AirSim/`, then
```
$ cd ~/AirSim
$ ./setup.sh
$ ./build.sh
```  
Open the editor (`$ UE4Editor`) and confirm rebuilding of Blocks and AirSim

### Make `DefaultQuadrotor` look like a Hexacopter

To purely change the appearance of AirSim's `DefaultQuadrotor`, follow these steps
- Replace files `FlyingPawn.h` and `FlyingPawn.cpp` in folder `~/AirSim/Unreal/Plugins/AirSim/Source/Vehicles/Multirotor` with those provided [here](https://github.com/JacopoPan/a-minimalist-guide/tree/master/files)
> Note that the only modifications are line 43 in `FlyingPawn.h`
```
static constexpr size_t rotor_count = 6;
```
> And lines 94-109 in `FlyingPawn.cpp`
```
if (rotor_index==0) {
    auto comp = rotating_movements_[4];
    if (comp != nullptr) {
        comp->RotationRate.Yaw = 
            rotor_infos.at(rotor_index).rotor_speed * rotor_infos.at(rotor_index).rotor_direction *
            180.0f / M_PIf * RotatorFactor;
    }
}
if (rotor_index==2) {
    auto comp = rotating_movements_[5];
    if (comp != nullptr) {
        comp->RotationRate.Yaw = 
            rotor_infos.at(rotor_index).rotor_speed * rotor_infos.at(rotor_index).rotor_direction *
            180.0f / M_PIf * RotatorFactor;
    }
}
```
> These changes are simply meant to copy the rotation of propellers 0 and 2 (CW and CCW) into `Rotation4` and `Rotation5`

- If desired, add debug information printed to screen with this instruction
```
GEngine->AddOnScreenDebugMessage(-1, 5.f, FColor::Red, TEXT("Screen Message"));
```
- Rebuild AirSim
```
$ cd ~/AirSim
$ ./setup.sh
$ ./build.sh
```  
- Open the editor (`$ UE4Editor`) and confirm rebuilding of Blocks and AirSim
- Close the Unreal Engine Editor
- Download folder [`Hexacopter`](https://github.com/JacopoPan/a-minimalist-guide/tree/master/files/Hexacopter)
- Move it inside folder `~/AirSim/Unreal/Environments/Blocks/Content/`
- Re-open the editor (`$ UE4Editor`)
- In the "Content Manager" tab at the bottom, find `FlyingPawnHex.uasset` in folder `Hexacopter`
- Right click on it and select "Edit.."
- In the new window, under "Components" on the left, select "BodyMesh"
- On the right panel, make sure that "Static Mesh" is set to "DJI_S900"
- Similarly, make sure that the "Static Mesh" of all propellers ("Prop0", etc.) is "DJI_MotorProp"
> Note: this steps are only necessary in case the relative paths between these `.uasset` files have changed

- If desired, use the "Viewport" tab to change the positions of 6 propellers w.r.t the drone's body
> Tip: change the "Position Grid Snap"'s value from 10 to 1 

> Tip: use arrows, `PgUp`, `PgDn`, and trackpad + right or left click to navigate the viewport

- Add the [`PawnPaths`](https://microsoft.github.io/AirSim/settings/#pawnpaths) option to `~/Documents/AirSim/settings.json`
```
  "PawnPaths": {
    "DefaultQuadrotor": {"PawnBP": "Class'/Game/FlyingPawnHex/BP_FlyingPawnHex.BP_FlyingPawnHex_C'"}
  },
```
> Note: `/Game/XYZ.XYZ_C` refers to BP `Oxcart/Content/XYZ.uasset`, `XYZ.XYZ_C` is notation required to specify the class for BP XYZ. 

- Play the game (`Alt`+`p`) to see the default quadrotor model replaced by a hexacopter




## Packaging custom UE4 environments and AirSim

One can package their UE4 environment (level), assets (e.g. the hexacopter), and AirSim's plugin in a precompiled set of binaries like [these](https://github.com/Microsoft/AirSim/releases)

> **Important**: if using Unreal Engine's version 4.24, first fix [this bug](https://github.com/EpicGames/UnrealEngine/commit/cb388710a7fbe43eaa82a6d8c43b1632f25f6386) by replacing `AnimCurveTypes.h` and `AnimCurveTypes.cpp` in `~/UnrealEngine/Engine/Source/Runtime/Engine/Public/Animation/` and `[..]/Private/Animation/` with the files provided [here](https://github.com/JacopoPan/a-minimalist-guide/tree/master/files/) and [recompile the engine](https://github.com/JacopoPan/a-minimalist-guide/blob/master/Part3-Using-AirSim.md#build-ue4-and-ue4editor)

Packaging is detailed [here](https://docs.unrealengine.com/en-US/Engine/Basics/Projects/Packaging/index.html)
- Make sure the "Game Default Map" is set in `Edit > Project Settings > Maps & Modes` (alreay the case in Blocks)
- Go to `File > Package Project > Packaging Settings..`
- Under "Packaging", uncheck "Use Pak file"
- Under "Additional Asset Directories to Cook" add `/Game/Hexacopter` (if you followed the steps above)
- Add any other desired asset folder
- Package for Ubuntu with `File > Package Project > Linux`
- Specifiy a destination folder (e.g. `~/Desktop`) and proceed

The packaging process can be time consuming

The results is folder `~/Desktop/LinuxNoEditor` whose content can be launched with
```
$ ~/Desktop/LinuxNoEditor/Blocks.sh -ResX=640 -ResY=480 -windowed
```
To make it self-contained, move `settings.json` from `~/Documents/AirSim/` to `~/Desktop/LinuxNoEditor/Blocks/Binaries/Linux/`






## AirSim on a remote server

To run a packaged Unreal environment with AirSim on a remote machine—e.g. Vector Institute's cluster—there are 2 main options

Using the `DISPLAY` [environment variable](https://help.ubuntu.com/community/EnvironmentVariables)
```
$ DISPLAY= ./Blocks.sh
```
or using option `-nullrhi`, to avoid any tier 1 rendering
```
$ ./AirSimExe.sh -nullrhi
```
Note that calling `simGetImages` with -`nullrhi` would result in an [error](https://github.com/microsoft/AirSim-NeurIPS2019-Drone-Racing/issues/112)

To [save resources](https://microsoft.github.io/AirSim/settings/#viewmode), consider adding to `settings.json`
```
"--ViewMode": "NoDisplay",
```

To run and connect to [multiple instances](https://github.com/microsoft/AirSim-NeurIPS2019-Drone-Racing/issues/64) of the same environment on one cluster node
- Replicate the environment N times
- Copy `settings.json` within folder `[..]/Blocks/Binaries/Linux/` of each packaged environment
- Add a different address with option [`LocalHostIp`](https://microsoft.github.io/AirSim/settings/#localhostip-setting) to each copy of `settings.json`
```
"LocalHostIp": "127.0.0.x",
```
- Start multiple environments and connect to each by their address, e.g. using the Python APIs
```
>>> import airsim
>>> airsimClient = airsim.MultirotorClient("127.0.0.x")
```
An example of how to wrap AirSim's APIs within [RLlib](https://github.com/JacopoPan/a-minimalist-guide#ray-rllib)'s `ExternalMultiAgentEnv` class is given in [`minimal-airsim-rllib-ma-env.py`](https://github.com/JacopoPan/a-minimalist-guide/blob/master/files/minimal-airsim-rllib-ma-env.py)
```
class ExternalAirSimMultiAgent(ExternalMultiAgentEnv):

    def __init__(self, env_config: EnvContext, action_space: gym.Space, observation_space: gym.Space, max_concurrent: int):
       self.address = "127.0.0."+str(env_config.worker_index+1)
       super().__init__(action_space, observation_space, max_concurrent)

    def run(self):
       self.airsimclient = airsim.MultirotorClient(self.address)
       self.airsimclient.confirmConnection()
       self.airsimclient.simPause(True)
       ...
```




--------

## Additional links

- Review AirSim's [code structure](https://microsoft.github.io/AirSim/code_structure/) and [development workflow](https://microsoft.github.io/AirSim/dev_workflow/)

- Check out `AirLib`'s `multirotor` [`src`](https://github.com/microsoft/AirSim/tree/master/AirLib/src/vehicles/multirotor/api) and [`include` folders](https://github.com/microsoft/AirSim/tree/master/AirLib/include/vehicles/multirotor)

- For examples of how to add new APIs to AirSim, check out this [commit](https://github.com/Microsoft/AirSim/commit/f0e83c29e7685e1021185e3c95bfdaffb6cb85dc) and [pull request](https://github.com/microsoft/AirSim/pull/2710)

- The default [flight controller](https://microsoft.github.io/AirSim/flight_controller/) in AirSim  is [`simple_flight`](https://microsoft.github.io/AirSim/simple_flight/)

> [..] simply [..] (a) collection of algorithms packaged in a library [..] develop this code as dependency free header-only pure standard C++11

> Internally `simple_flight` uses cascade of PID controllers to finally generate actuator signals. 

> Note that `simple_slight` currently does not support state estimation, i.e. estimated and ground truth kinematics values are the same

> Notably, `simple_flight` usesca steppable clock which means its clock advances when simulator tells it to advance, this is convenient for learning applications, Otherwise add `"ClockType": "ScalableClock"` to `settings.json`

- Alternatively, AirSim's simlation can be used with PX4 autopilot's stack as software-in-the-loop (SITL), [link 1](https://github.com/microsoft/AirSim/blob/master/docs/px4_sitl.md), [link 2](https://github.com/microsoft/AirSim/blob/master/docs/px4_build.md)





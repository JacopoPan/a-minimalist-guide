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
> Note: `/Game/XYZ.XYZ_C` refers to BP `Oxcart/Content/XYZ.uasset`, `XYZ.XYZ_C` is a special notation required to specify the class for BP XYZ. 
> Please note that your BP must be derived from CarPawn class. By default this is not the case but you can re-parent the BP using the "Class Settings" button in toolbar in UE editor after you open the BP and then choosing "Car Pawn" for Parent Class settings in Class Options. 
> It's also a good idea to disable "Auto Possess Player" and "Auto Possess AI" as well as set AI Controller Class to None in BP details. Please make sure your asset is included for cooking in packaging options if you are creating binary.

- Play the game (`Alt`+`p`) to see the default quadrotor model replaced by a hexacopter




## Packaging custom UE4 environments and AirSim

first, if using u4.24, fix this error
https://github.com/EpicGames/UnrealEngine/commit/cb388710a7fbe43eaa82a6d8c43b1632f25f6386

replace 2 files with those provied

ideally, recompile UE4

then see [these instructons](https://docs.unrealengine.com/en-US/Engine/Basics/Projects/Packaging/index.html)
package for "Linux"

you want to cook the custom hex pawn, to do so
 "File" -> "Package Project" -> "Packaging Settings.."
 under "Packaging" 
 uncheck "Use Pak file"
 
 "Additional Asset Directories to Cook" add "/Game/Hexacopter"
  
you will end up with folder of precompiled binaries

move settings json

runs as `$ command`




## AirSim on a remote server

e.g. on Vector's cluster

```
$ DISPLAY= ./AirSimExe.sh -opengl4
or 
$ ./AirSimExe.sh -nullrhi - not that if you call simGetImages with -nullrhi option, it would result in an error.
```
https://github.com/microsoft/AirSim-NeurIPS2019-Drone-Racing/issues/112

**running multiple instances**
set "LocalHostIp": "127.0.0.1",  "127.0.0.2", etc

AirSim gives higher priority to a settings.json lying in the same directory as the linux/windows unreal binary, as compared to the one lying in /home/$USER/Documents/AirSim/settings.json

So, one way to do this is to copy paste the unreal binaries, and have different settings.json in each binary folder.

For example, you can place a settings.json in
PATH_TO/AirSim_1/AirSimExe/Binaries/Linux/settings.json, with a particular port number, and when you run it with ./AirSim_1/AirSimExe.sh -windowed

And then you can copy-paste the unreal engine binaries:
PATH_TO/AirSim_2/AirSimExe/Binaries/Linux/settings.json, with a new port number, and when you run it with ./AirSim_2/AirSimExe.sh -windowed it should use the new port number

https://github.com/microsoft/AirSim-NeurIPS2019-Drone-Racing/issues/64

**using AirSim's UE4 binaries as RLlib external environment**

```
import time
import random
import airsim
import ray
import gym
import numpy as np

from ray import tune
from ray.tune import register_env

from ray.rllib.env.env_context import EnvContext
from ray.rllib.env.external_multi_agent_env import ExternalMultiAgentEnv

from ray.rllib.agents import ppo

from ray.rllib.models import ModelCatalog

class ExternalAirSimMultiAgent(ExternalMultiAgentEnv):

    def __init__(self, env_config: EnvContext, action_space: gym.Space, observation_space: gym.Space, max_concurrent: int):
       self.address = "127.0.0."+str(env_config.worker_index+1)
       print("Init of the environment that will connect to AirSim client", self.address)
       super().__init__(action_space, observation_space, max_concurrent)

    def run(self):
       self.airsimclient = airsim.MultirotorClient(self.address)
       self.airsimclient.confirmConnection()
       self.airsimclient.simPause(True)
       self.num_drones = 2
       for i in range(self.num_drones):
           v_str = "Drone"+str(i)
           self.airsimclient.enableApiControl(True, vehicle_name=v_str)
           self.airsimclient.armDisarm(True, vehicle_name=v_str)
           self.airsimclient.takeoffAsync(timeout_sec=2.0, vehicle_name=v_str)
       self.airsimclient.simContinueForTime(2.0)
       steps_counter = 0
       episode_id = self.start_episode()
       print("starting episode id:", episode_id, "with client", self.address)
       while True:
           steps_counter += 1
           obs = {}
           for i in range(self.num_drones):
               v_str = "Drone"+str(i)
               if self.airsimclient.getMultirotorState(vehicle_name=v_str).kinematics_estimated.position.y_val > 0:
                   obs[i] = 1
               else:
                   obs[i] = 0
           actions = self.get_action(episode_id, obs)                         # or self.log_action(episode_id, obs, action)
           for i in range(self.num_drones):
               v_str = "Drone"+str(i)
               if actions[i]==0:
                   self.airsimclient.moveToPositionAsync(0, -1, -2, 1.0, vehicle_name=v_str)
               if actions[i]==1:
                   self.airsimclient.moveToPositionAsync(0, 1, -2, 1.0, vehicle_name=v_str)
           self.airsimclient.simContinueForTime(1.0)
           rewards = {}
           for i in range(self.num_drones):
               v_str = "Drone"+str(i)
               rewards[i] = self.airsimclient.getMultirotorState(vehicle_name=v_str).kinematics_estimated.position.y_val
           self.log_returns(episode_id, rewards)
           if steps_counter > 4:
               steps_counter = 0
               print("ending episode id:", episode_id, "with client", self.address)
               self.end_episode(episode_id, obs)
               episode_id = self.start_episode()
               print("starting episode id:", episode_id, "with client", self.address)

if __name__ == "__main__":

    print("Initializing Ray")
    ray.shutdown()
    ray.init(ignore_reinit_error=True)
    print("Dashboard URL: http://{}".format(ray.get_webui_url()))

    print("Registering the environment")
    def env_creator(env_config):
        o = gym.spaces.Discrete(2)
        a = gym.spaces.Discrete(2)
        max_conc = 2                                                          # TO BE FIXED (?) should be 1 but throws error if too low
        return ExternalAirSimMultiAgent(env_config, o, a, max_conc)
    register_env("ext-ma-airsim", env_creator)
    #tune.register_env("ext-ma-airsim", lambda env_config: ExternalAirSimMultiAgent(env_config,o,a,max_conc))

    print("Training")
    stop = {
        "episode_reward_mean": 100,
        "timesteps_total": 2,
    }

    obs_space_dict = {
        "agent_1": gym.spaces.Discrete(2),
        "agent_2": gym.spaces.Discrete(2),
    }
    act_space_dict = {
        "agent_1": gym.spaces.Discrete(2),
        "agent_2": gym.spaces.Discrete(2),
    }

    o_s = gym.spaces.Discrete(2)
    a_s = gym.spaces.Discrete(2)
    config = {
        "env": "ext-ma-airsim",
        "num_workers": 0,
        "env_config": {
            "actions_are_logits": True,
        },
        "multiagent": {
            "policies": {
                "pol1": (None, o_s, a_s, {"agent_id": 0,}),
                "pol2": (None, o_s, a_s, {"agent_id": 1,}),
            },
            "policy_mapping_fn": lambda agent_id: "pol1" if agent_id == 0 else "pol2",
        },
        "framework": "torch",
    }

    tune.run("PPO",stop=stop, config=config, verbose=1)
    ray.shutdown()

```


## Modifying AirSim's source

links

how to recompile

reminders of what to change










--------

## Additional links


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

# PX4 SITL

https://github.com/microsoft/AirSim/blob/master/docs/px4_sitl.md

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





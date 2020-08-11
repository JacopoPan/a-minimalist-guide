

# AirSim Python API Documentation 

## Table of Contents
- [Vehicle Client](#vehiclecient-class)
- [Car Client](#carclient-class)
- [Multirotor Client](#multirotorclient-class)


## `VehicleClient` Class

#### `VehicleClient.__init__()` 
> Initialize vehicle client. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `ip`            | [str][s] | _optional_, default=`''`          |                                       |
| `port`          | [int][i] | _optional_, default=`41451`       |                                       |
| `timeout_value` | [int][i] | _optional_, default=`3600`        |                                       |

---

#### `VehicleClient.reset()` 
> Reset the vehicle to its original starting state.

---

#### `VehicleClient.ping()` 
> If connection is established then this call will return true otherwise it will be blocked until timeout. 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [bool][b]                     | Returns whether call is successful                                                     |

---

#### `VehicleClient.getClientVersion()` 
> Request client version. 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [int][i]                      | Returns version                                                           |

---

#### `VehicleClient.getServerVersion()` 
> Request server version. 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [int][i]                      | Returns version                                                           |

---
 
#### `VehicleClient.getMinRequiredServerVersion()` 
> Request minimum server version. 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [int][i]                      | Returns version                                                           |

---
 
#### `VehicleClient.getMinRequiredClientVersion()` 
> Request minimum client version. 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [int][i]                      | Returns version                                                           |

---
 
#### `VehicleClient.enableApiControl(is_enabled)` 
> Enables or disables API control for vehicle corresponding to vehicle_name. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `is_enabled`    | [bool][b]| _required_                        | Enable or Disable API                 |
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---

#### `VehicleClient.isApiControlEnabled()`
> Returns true if API control is established.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [bool][b]                     | Whether API control is enabled                                                    |

---

#### `VehicleClient.armDisarm(arm)` 
> Arms or disarms vehicle.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `arm`           | [bool][b]| _required_                        | True to arm, False to disarm the vehicle                |
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [bool][b]                     | Whether call was successful                                                    |

---

#### `VehicleClient.simPause(is_paused)` 
> Pauses simulation.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `is_paused`     | [bool][b]| _required_                        | True to pause the simulation, False to release |

---

#### `VehicleClient.simIsPause()` 
> Returns true if the simulation is paused. 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [bool][b]                     | Whether simulation is paused                                                  |

---

#### `VehicleClient.simContinueForTime(seconds)` 
> Continue the simulation for the specified number of seconds.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `seconds`       | [float][f]| _required_                      | Time to run the simulation for |


---

#### `VehicleClient.getHomeGeoPoint()` 
> Get the Home location of the vehicle.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| GeoPoint[geo]                 | Home location of the vehicle |

---

#### `VehicleClient.confirmConnection()` 
> Checks state of connection every 1 sec and reports it in Console so user can see the progress for connection.

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [bool][b]                     | Whether connection is established                                                 |

---

#### `VehicleClient.simSwapTextures(tags)` 
> Runtime Swap Texture API.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `tags`          | [str][s] | _required_ | string of "," or ", " delimited tags to identify on which actors to perform the swap| 
| `tex_id`        | [int][i] | _optional_, default=`0` | indexes the array of textures assigned to each actor undergoing a swap | 
| `component_id`  | [int][i] | _optional_, default=`0` |               |
| `material_id`   | [int][i] | _optional_, default=`0` |               |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| list of [str][s]              | List of objects which matched the provided tags and had the texture swap perfomed   | 

---

#### `VehicleClient.simSetTimeOfDay(is_enabled)` 
> Control the position of Sun in the environment.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `is_enabled`    | [bool][b]| _required_ | True to enable time-of-day effect, False to reset the position to original | 
| `start_datetime`| [str][s] | _optional_, default=`''` | ate & Time in %Y-%m-%d %H:%M:%S format, e.g. `2018-02-12 15:20:00` | 
| `is_start_datetime_dst`| [bool][b]| _optional_, default=`False` | True to adjust for Daylight Savings Time |
| `celestial_clock_speed`| [float][f]| _optional_, default=`1` | Run celestial clock faster or slower than simulation clock |
| `update_interval_secs` | [float][f]| _optional_, default=`60` | Interval to update the Sun's position |
| `move_sun` | [bool][b] | _optional_, default=`True` |  Whether or not to move the Sun |

---

#### `VehicleClient.simEnableWeather(enable)` 
> Enable Weather effects. Needs to be called before using `simSetWeatherParameter` API.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `enable`        | [bool][b]| _required_ | True to enable, False to disable | 

---

#### `VehicleClient.simSetWeatherParameter(param, val)` 
> Enable various weather effects.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `param`         | [WeatherParameter][wea] | _required_ | Weather effect to be enabled | 
| `val`           | [float][f] | _required_ | Intensity of the effect, Range 0-1 | 

---

#### `VehicleClient.simGetImage(camera_name, image_type)` 
> Get a single image.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `camera_name`   | [str][s] | _required_                        | Name of the camera, for backwards compatibility, ID numbers such as 0,1,etc. can also be used | 
| `image_type`    | [ImageType][imgtype]| _required_                 | Type of image required | 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [str][s]                      | Binary string literal of compressed png image | 

---

#### `VehicleClient.simGetImages(requests)` 
> Get multiple images. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `requests`      | List of [ImageRequest][imgreq]| _required_ | Images required | 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| List of [ImageResponse][imgres]|              | 

---

#### `VehicleClient.simGetMeshPositionVertexBuffers()` 
> Returns the static meshes that make up the scene. See https://microsoft.github.io/AirSim/meshes/ for details and how to use this. 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| List of [MeshPositionVertexBuffersResponse][mesh]|   more information [here][https://github.com/microsoft/AirSim/blob/master/docs/meshes.md]           | 

---

#### `VehicleClient.simGetCollisionInfo()` 
> Returns information aboout collision with vehicle. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [CollisionInfo][col]          |                       | 

---

#### `VehicleClient.simSetVehiclePose(pose, ignore_collison)` 
> Set the pose of the vehicle.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `pose`          | [Pose][pose]| _required_   | Desired Pose pf the vehicle | 
| `ignore_collision`| [bool][b] | _required_ | Whether to ignore any collision or not | 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---

#### `VehicleClient.simGetVehiclePose()` 
> Returns current pose of the vehicle. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [Pose][pose]                  |                            | 

---

#### `VehicleClient.simSetTraceLine(color_rgba)` 
> Modify the color and thickness of the line when Tracing is enabled.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `color_rgba`    | List of [float][f]| _required_ | desired RGBA values from 0.0 to 1.0 | 
| `thickness`     | [float][f]| _optional_, default='1.0' | Thickness of the line | 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---

#### `VehicleClient.simGetObjectPose(object_name)` 
> Returns current pose of the object.  

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `object_name`   | [str][s] | _required_ | Object to get the Pose of | 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [Pose][pose]                  |                     | 

---

#### `VehicleClient.simSetObjectPose(object_name, pose)` 
> Set the pose of the object(actor) in the environment.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `object_name`   | [str][s] | _required_ | Object to get the Pose of | 
| `pose`          | [Pose][pose]| _required_   | Desired Pose pf the vehicle | 
| `teleport`      | [bool][b] | _optional_, default=`True` | Whether to move the object immediately without affecting their velocity |  

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [bool][b]                     | Whether the move was successful   | 

---

#### `VehicleClient.simListSceneObjects()` 
> Lists the objects present in the environment.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `name_regex`    | [str][s] | _optional_, default=`'.*'`        | String to match actor names against, e.g. "Cylinder.*" | 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| List of [str][s]              | List containing all the names | 

---

#### `VehicleClient.simSetSegmentationObjectID(mesh_name, object_id)` 
> Set segmentation ID for specific objects. See https://microsoft.github.io/AirSim/image_apis/#segmentation for details. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `mesh_name`     | [str][s] | _required_  | Name of the mesh to set the ID of (supports regex) | 
| `object_id`     | [int][i] |  _required_ | Object ID to be set, range 0-255 | 
| `is_name_regex` | [bool][b] | _optional_, default=`False`| Whether the mesh name is a regex | 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [bool][b]                     | If the mesh was found | 

---

#### `VehicleClient.simGetSegmentationObjectID(mesh_name)` 
> Returns Object ID for the given mesh name. Mapping of Object IDs to RGB values can be seen at https://microsoft.github.io/AirSim/seg_rgbs.txt. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `mesh_name`     | [str][s] | _required_                        | Name of the mesh to get the ID of | 

---

#### `VehicleClient.simPrintLogMessage(message)` 
> Prints the specified message in the simulator's window.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `message`       | [str][s] | _required_ | Message to be printed | 
| `message_param` | [str][s] | _optional_, default=`''` | Parameter to be printed next to the message | 
| `severity`      | [int][i] | _optional_, default=`0`  | Range 0-3, inclusive, corresponding to the severity of the message | 

---

#### `VehicleClient.simGetCameraInfo(camera_name)` 
> Get details about the camera.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `camera_name`   | [str][s] | _required_ | Name of the camera, for backwards compatibility, ID numbers such as 0,1,etc. can also be used | 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [CameraInfo][cam]             |      | 

---

#### `VehicleClient.simSetCameraOrientation(camera_name, orientation)` 
> Control the orientation of a selected camera.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `camera_name`   | [str][s] | _required_ | Name of the camera to be controlled | 
| `orientation`   | [Quaternionr][quat] | _required_ | Quaternion representing the desired orientation of the camera | 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---

#### `VehicleClient.simSetCameraFov(camera_name, fov_degrees)` 
> Control the field of view of a selected camera.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `camera_name`   | [str][s] | _required_ | Name of the camera to be controlled | 
| `fov_degrees`   | [float][f]| _required_ | Value of field of view in degrees | 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---

#### `VehicleClient.simGetGroundTruthKinematics()` 
> Get Ground truth kinematics of the vehicle. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [KinematicsState][kin]        | Ground truth of the vehicle | 

---

#### `VehicleClient.simGetGroundTruthEnvironment()` 
> Get ground truth environment state. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [EnvironmentState][env]       | Ground truth environment state | 

---

#### `VehicleClient.getImuData()` 
> Returns informaton about IMU. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `imu_name`      | [str][s] | _optional_, default=`''`          | Name of IMU to get data from, specified in [`settings.json`][settings] | 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [ImuData][imu]                | more information [here][https://github.com/microsoft/airsim/blob/master/docs/sensors.md]      | 

---

#### `VehicleClient.getBarometerData()` 
> Returns information about barometer. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `barometer_name`| [str][s] | _optional_, default=`''`          | Name of Barometer to get data from, specified in [`settings.json`][settings] | 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [BarometerData][baro]         | more information [here][https://github.com/microsoft/airsim/blob/master/docs/sensors.md]         | 

---

#### `VehicleClient.getMagnetometerData()` 
> Returns information about magnetometer. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `magnetometer_name`| [str][s] | _optional_, default=`''`       | Name of Magnetometer to get data from, specified in [`settings.json`][settings] | 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MagnetometerData][mag]       |   more information [here][https://github.com/microsoft/airsim/blob/master/docs/sensors.md]      | 

---

#### `VehicleClient.getGpsData()` 
> Returns information about GPS. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `gps_name`      | [str][s] | _optional_, default=`''`          | Name of GPS to get data from, specified in [`settings.json`][settings] | 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [GpsData][gps]                |   more information [here][https://github.com/microsoft/airsim/blob/master/docs/sensors.md]        | 

---

#### `VehicleClient.getDistanceSensorData()` 
> Returns information about distance sensor. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `distance_sensor_name`| [str][s] | _optional_, default=`''`    | Name of distance sensor to get data from, specified in [`settings.json`][settings] | 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [DistanceSensorData][dist]    |    more information [here][https://github.com/microsoft/airsim/blob/master/docs/sensors.md]               | 

---

#### `VehicleClient.getLidarData()` 
> Get information about LiDAR. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `lidar_name`    | [str][s] | _optional_, default=`''`          | Name of LiDAR to get data from, specified in [`settings.json`][settings] | 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [LidarData][lidar]            |    more information [here][https://github.com/microsoft/airsim/blob/master/docs/lidar.md]            | 

---

#### `VehicleClient.simGetLidarSegmentation()` 
> Returns Segmentation ID of each point's collided object in the last Lidar update.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `lidar_name`    | [str][s] | _optional_, default=`''`          | Name of LiDAR to get data from, specified in [`settings.json`][settings] | 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| List of [int][i]              | Segmentation IDs of the objects | 

---

#### `VehicleClient.simFlushPersistentMarkers()` 
> Clear any persistent markers - those plotted with setting `is_persistent=True`. 

---

#### `VehicleClient.simPlotPoints(points)` 
> Plot a list of 3D points in World NED frame. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `points`        | List of [Vector3r][vec]| _required_ | List of Vector3r objects | 
| `color_rgba`    | list of [float][f] | _optional_, default=`[1.0, 0.0, 0.0, 1.0]` | desired RGBA values from 0.0 to 1.0 | 
| `size`          | [float][f] | _optional_, default=`10.0` | Size of plotted point | 
| `duration`      | [float][f] | _optional_, default=`-1.0` | Duration (seconds) to plot for | 
| `is_persistent` | [bool][b] | _optional_, default=`False` | If set to True, the desired object will be plotted for infinite time. | 

---

#### `VehicleClient.simPlotLineStrip(points)` 
> Plots a line strip in World NED frame, defined from points[0] to points[1], points[1] to points[2], ... , points[n-2] to points[n-1]. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `points`        | List of [Vector3r][vec]| _required_ | List of Vector3r objects | 
| `color_rgba`    | list of [float][f] | _optional_, default=`[1.0, 0.0, 0.0, 1.0]` | desired RGBA values from 0.0 to 1.0 | 
| `thickness`     | [float][f] | _optional_, default=`5.0`  | Thickness of line | 
| `duration`      | [float][f] | _optional_, default=`-1.0` | Duration (seconds) to plot for | 
| `is_persistent` | [bool][b] | _optional_, default=`False` | If set to True, the desired object will be plotted for infinite time. | 

---

#### `VehicleClient.simPlotLineList(points)` 
> Plots a line strip in World NED frame, defined from points[0] to points[1], points[2] to points[3], ... , points[n-2] to points[n-1]. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `points`        | List of [Vector3r][vec]| _required_ | List of Vector3r objects | 
| `color_rgba`    | list of [float][f] | _optional_, default=`[1.0, 0.0, 0.0, 1.0]` | desired RGBA values from 0.0 to 1.0 | 
| `thickness`     | [float][f] | _optional_, default=`5.0`  | Thickness of line | 
| `duration`      | [float][f] | _optional_, default=`-1.0` | Duration (seconds) to plot for | 
| `is_persistent` | [bool][b] | _optional_, default=`False` | If set to True, the desired object will be plotted for infinite time. | 

---

#### `VehicleClient.simPlotArrows(points_start, points_end)` 
> Plots a list of arrows in World NED frame, defined from points_start[0] to points_end[0], points_start[1] to points_end[1], ... , points_start[n-1] to points_end[n-1]. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `points_start`  | List of [Vector3r][vec]| _required_ | List of 3D start positions of arrow start positions, specified as Vector3r objects | 
| `points_end`    | List of [Vector3r][vec]| _required_ | List of 3D end positions of arrow start positions, specified as Vector3r objects | 
| `color_rgba`    | list of [float][f] | _optional_, default=`[1.0, 0.0, 0.0, 1.0]` | desired RGBA values from 0.0 to 1.0 | 
| `thickness`     | [float][f] | _optional_, default=`5.0`  | Thickness of line | 
| `arrow_size`    | [float][f] | _optional_, default=`2.0`  | Size of arrow head | 
| `duration`      | [float][f] | _optional_, default=`-1.0` | Duration (seconds) to plot for | 
| `is_persistent` | [bool][b] | _optional_, default=`False` | If set to True, the desired object will be plotted for infinite time. | 

---

#### `VehicleClient.simPlotStrings(strings, positions)` 
> Plots a list of strings at desired positions in World NED frame.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `strings`       | List of [str][s] | _required_ | List of strings to plot | 
| `positions`    | List of [Vector3r][vec]| _required_ | List of positions where the strings should be plotted. Should be in one-to-one correspondence with the strings' list | 
| `scale`         | [float][f] | _optional_, default=`5` | Font scale of transform name | 
| `color_rgba`    | list of [float][f] | _optional_, default=`[1.0, 0.0, 0.0, 1.0]` | desired RGBA values from 0.0 to 1.0 | 
| `duration`      | [float][f] | _optional_, default=`-1.0` | Duration (seconds) to plot for | 

---

#### `VehicleClient.simPlotTransforms(poses)` 
> Plots a list of transforms in World NED frame.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `poses`         | List of [Pose][pose] | _required_     | List of Pose objects representing the transforms to plot | 
| `scale`         | [float][f] | _optional_, default=`5` | Font scale of transform name | 
| `thickness`     | [float][f] | _optional_, default=`5.0`  | Thickness of line | 
| `duration`      | [float][f] | _optional_, default=`-1.0` | Duration (seconds) to plot for | 
| `is_persistent` | [bool][b] | _optional_, default=`False` | If set to True, the desired object will be plotted for infinite time. | 

---

#### `VehicleClient.simPlotTransformsWithNames(poses, names)` 
> Plots a list of transforms with their names in World NED frame.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `poses`         | List of [Pose][pose] | _required_     | List of Pose objects representing the transforms to plot | 
| `names`         | List of [str][s] | _required_ | List of strings with one-to-one correspondence to list of poses | 
| `tf_scale`      | [float][f] | _optional_, default=`5.0` | Length of transforms' axes | 
| `tf_thickness`  | [float][f] | _optional_, default=`5.0` | Thickness of transforms' axes | 
| `text_scale`    | [float][f] | _optional_, default=`5` | Font scale of transform name | 
| `text_color_rgba` | list of [float][f] | _optional_, default=`[1.0, 0.0, 0.0, 1.0]` | desired RGBA values from 0.0 to 1.0 | 
| `duration`      | [float][f] | _optional_, default=`-1.0` | Duration (seconds) to plot for | 

---

#### `VehicleClient.cancelLastTask()` 
> Cancel previous Async task. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---

#### `VehicleClient.waitOnLastTask()` 
> Wait for the last Async task to complete. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `timeout_sec`   | [float][f] | _optional_, default=`float('nan')`| Time for the task to complete | 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [bool][b]                     | Result of the last task | 

---

[b]: https://docs.python.org/3/c-api/bool.html
[geo]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L221
[wea]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L40
[imgtype]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L22
[imgreq]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L258
[imgres]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L272 
[mesh]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L502
[col]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L211
[pose]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L196
[cam]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L355
[quat]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L109
[kin]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L315
[env]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L323
[imu]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L365
[baro]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L371
[mag]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L377
[gps]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L396
[dist]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L401
[lidar]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L360

## `CarClient` Class
#### `CarClient.__init__()` 

> initializes car client.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `ip`            | [str][s] | _optional_, default=`''`          |                                       |
| `port`          | [int][i] | _optional_, default=`41451`       |                                       |
| `timeout_value` | [int][i] | _optional_, default=`3600`        |                                       |

---

#### `CarClient.setCarControls(controls)` 
> Control the car using throttle, steering, brake, etc.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `controls`      | [CarControls][Cctl]| _required_              | Struct containing control values      | 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---

#### `CarClient.getCarState():`
> Get current state of the vehicle.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [CarState][Cstate]            | State the of the vehicle.                                                              |

---

#### `CarClient.getCarControls()` 
> Get current control values of the vehicle. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [CarControls][Cctl]           | Struct containing control values of the vehicle.                                       |

---

[Cctl]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L285
[Cstate]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L331


## `MultirotorClient` Class
By default AirSim uses carrot following algorithm. By default `Async` methods will start immediately after _starting_ the task. 
---

#### `MultirotorClient.__init__()`

> initializes multirotor client

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `ip`            | [str][s] | _optional_, default=`''`          |                                       |
| `port`          | [int][i] | _optional_, default=`41451`       |                                       |
| `timeout_value` | [int][i] | _optional_, default=`3600`        |                                       |

---

#### `MultirotorClient.takeoffAsync()`

> takeoff vehicle to 3m above ground; vehicle should not be moving when this API is used

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `timeout_sec`   | [int][i] | _optional_, default=`20`          | Takeoff time, in seconds.                         |
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [msgpackrpc.future.Future][F] | use `.join()` to make the call blocking/wait to finish—`client.method().join()`  |

---



#### `MultirotorClient.landAsync()`
> Land the vehicle

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `timeout_sec`   | [int][i] | _optional_, default=`20`          | Landing time, in seconds.                         |
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [msgpackrpc.future.Future][F] | use `.join()` to make the call blocking/wait to finish—`client.method().join()`  |

---


#### `MultirotorClient.goHomeAsync()`
> Return vehicle to Home i.e. Launch location

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `timeout_sec`   | [int][i] | _optional_, default=`3e38`          | Travel time, in seconds. Process will end after this time regardless whether vehicle as reached destination  |
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [msgpackrpc.future.Future][F] | use `.join()` to make the call blocking/wait to finish—`client.method().join()`  |

---

#### `MultirotorClient.moveByAngleZAsync(pitch, roll, z, yaw, duration)`
> Does not work 

---

#### `MultirotorClient.moveByAngleThrottleAsync(pitch, roll, throttle, yaw_rate, duration)`
> Does not work 

---

#### `MultirotorClient.moveByVelocityAsync(vx, vy, vz, duration)` 
> Move vehicle at desired velocity.AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `vx`            | [float][f] | _required_                      | Desired velocity in world (NED) X axis            |
| `vy`            | [float][f] | _required_                      | Desired velocity in world (NED) Y axis            |
| `vz`            | [float][f] | _required_                      | Desired velocity in world (NED) Z axis            |
| `duration`      | [float][f] | _required_                      | Amount of time to send this command for , in seocnds  |
| `drivetrain`    | [DrivetrainType][drivetrain] | _optional_, default=`MaxDegreeofFreedom`  | more information [here][https://microsoft.github.io/AirSim/apis/#drivetrain]                |
| `yaw_mode`    | [YawMode][yawmode] | _optional_, default=`YawMode()`  |   more information [here][https://microsoft.github.io/AirSim/apis/#yaw_mode]              |
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [msgpackrpc.future.Future][F] | use `.join()` to make the call blocking/wait to finish—`client.method().join()`  |

---

#### `MultirotorClient.moveByVelocityZAsync(vx, vy, z, duration)` 
> Move vehicle at desired velocity (XY only). AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `vx`            | [float][f] | _required_                      | Desired velocity in world (NED) X axis            |
| `vy`            | [float][f] | _required_                      | Desired velocity in world (NED) Y axis            |
| `z`             | [float][f] | _required_                      | Desired position in world (NED) Z axis            |
| `duration`      | [float][f] | _required_                      | Amount of time to send this command for , in seocnds  |
| `drivetrain`    | [DrivetrainType][drivetrain] | _optional_, default=`MaxDegreeofFreedom`  |    more information [here][https://microsoft.github.io/AirSim/apis/#drivetrain]             |
| `yaw_mode`    | [YawMode][yawmode] | _optional_, default=`YawMode()`  |   more information [here][https://microsoft.github.io/AirSim/apis/#yaw_mode]               |
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [msgpackrpc.future.Future][F] | use `.join()` to make the call blocking/wait to finish—`client.method().join()`  |

---

#### `MultirotorClient.moveOnPathAsync(path, velocity)`  _untested_
> move vehicle along coordinates. This is the highest level of control in AirSim. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `path`          | [vector3r][vec] | _required_                        | Desired path                         |
| `velocity`      | [float][f] | _required_                      | Desired linear velocity  |
| `timeout_sec`   | [int][i] | _optional_, default=`3e38`          | Travel time, in seconds. Process will end after this time regardless whether vehicle as reached destination  |
| `drivetrain`    | [DrivetrainType][drivetrain] | _optional_, default=`MaxDegreeofFreedom`  |   more information [here][https://microsoft.github.io/AirSim/apis/#drivetrain]              |
| `yaw_mode`    | [YawMode][yawmode] | _optional_, default=`YawMode()`  |   more information [here][https://microsoft.github.io/AirSim/apis/#yaw_mode]               |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [msgpackrpc.future.Future][F] | use `.join()` to make the call blocking/wait to finish—`client.method().join()`  |

---


#### `MultirotorClient.moveToPositionAsync(x, y, z, velocity)` 
> Move vehicle to desired position. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `x`            | [float][f] | _required_                      | Desired velocity in world (NED) X axis            |
| `y`            | [float][f] | _required_                      | Desired velocity in world (NED) Y axis            |
| `z`             | [float][f] | _required_                      | Desired position in world (NED) Z axis            |
| `velocity`      | [float][f] | _required_                      | Desired linear velocity  |
| `timeout_sec`   | [int][i] | _optional_, default=`3e38`          | Travel time, in seconds. Process will end after this time regardless whether vehicle as reached destination  |
| `drivetrain`    | [DrivetrainType][drivetrain] | _optional_, default=`MaxDegreeofFreedom`  |      more information [here][https://microsoft.github.io/AirSim/apis/#drivetrain]           |
| `yaw_mode`    | [YawMode][yawmode] | _optional_, default=`YawMode()`  | more information [here][https://microsoft.github.io/AirSim/apis/#yaw_mode]                 |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [msgpackrpc.future.Future][F] | use `.join()` to make the call blocking/wait to finish—`client.method().join()`  |

---

#### `MultirotorClient.moveToZAsync(z, velocity)` 
> Move vehicle to desired altitude. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `z`             | [float][f] | _required_                      | Desired position in world (NED) Z axis            |
| `velocity`      | [float][f] | _required_                      | Desired linear velocity  |
| `timeout_sec`   | [int][i] | _optional_, default=`3e38`          | Travel time, in seconds. Process will end after this time regardless whether vehicle as reached destination  |
| `yaw_mode`      | [YawMode][yawmode] | _optional_, default=`YawMode()`  |     more information [here][https://microsoft.github.io/AirSim/apis/#yaw_mode]             |
| `lookahead`     | [int][i] | _optional_, default=`-1`          |   more information [here][https://microsoft.github.io/AirSim/apis/#lookahead-and-adaptive_lookahead]                        |
| `adaptive_lookahead`| [int][i]| _optional_, default=`1`        |   more information [here][https://microsoft.github.io/AirSim/apis/#lookahead-and-adaptive_lookahead]                       |    
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [msgpackrpc.future.Future][F] | use `.join()` to make the call blocking/wait to finish—`client.method().join()`  |

---

#### `MultirotorClient.moveByManualAsync(vx_max, vy_max, z_min, duration)` _untested_ 
> Read current RC state and use it to control the vehicles. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `vx_max`        | [float][f] | _required_                      | max velocity allowed in X direction               |
| `vy_max`        | [float][f] | _required_                      | max velocity allowed in Y direction               |
| `vz_max`        | [float][f] | _required_                      | max velocity allowed in Z direction               |
| `z_min`         | [float][f] | _required_                      | min z allowed for vehicle position                |
| `duration`      | [float][f] | _required_                      | after this duration vehicle would switch back to non-manual mode  |
| `drivetrain`    | [DrivetrainType][drivetrain] | _optional_, default=`MaxDegreeofFreedom`  |    more information [here][https://microsoft.github.io/AirSim/apis/#drivetrain]             |
| `yaw_mode`    | [YawMode][yawmode] | _optional_, default=`YawMode()`  |    more information [here][https://microsoft.github.io/AirSim/apis/#yaw_mode]              |
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [msgpackrpc.future.Future][F] | use `.join()` to make the call blocking/wait to finish—`client.method().join()`  |

---

#### `MultirotorClient.rotateToYawAsync(yaw)` 
> Change vehicle yaw angle. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `yaw`           | [float][f]| _required_                       | Desired yaw angle in world (NED) frame, in degrees  | 
| `timeout_sec`   | [int][i] | _optional_, default=`3e38`          | Travel time, in seconds. Process will end after this time regardless whether vehicle as reached destination  |
| `margin`        | [int][i] | _optional_, default=`5`           |                                                   | 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [msgpackrpc.future.Future][F] | use `.join()` to make the call blocking/wait to finish—`client.method().join()`  |

---
         
#### `MultirotorClient.rotateByYawRateAsync(yaw_rate, duration)`
> Change vehicle yaw rate. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `yaw_rate`      |[float][f]| _required_                        | Desired yaw velocity in world (NED) frame, in degrees per second  | 
| `duration`      | [float][f] | _required_                      | after this duration vehicle would switch back to non-manual mode  |
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

            
| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [msgpackrpc.future.Future][F] | use `.join()` to make the call blocking/wait to finish—`client.method().join()`  |

---

       
#### `MultirotorClient.hoverAsync()` 
> Make vehicle hover. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |


| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [msgpackrpc.future.Future][F] | use `.join()` to make the call blocking/wait to finish—`client.method().join()`  |

---

#### `MultirotorClient.moveByRC(rcdata)` _untested_
> Move vehicle with remote control. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `rcdata`        | [RCData][rc]| _required_                     |                                                   | 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [msgpackrpc.future.Future][F] | use `.join()` to make the call blocking/wait to finish—`client.method().join()`  |

---

#### `MultirotorClient.moveByMotorPWMsAsync(front_right_pwm, rear_left_pwm, front_left_pwm, rear_right_pwm, duration)`
> Directly control the motors using PWM values. This is the lowest level of control in AirSim. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `front_right_motor`| [float][f]| _required_                    | PWM value for the front right motor (between 0.0 to 1.0)|
| `rear_left_motor`  | [float][f]| _required_                    | PWM value for the front right motor (between 0.0 to 1.0)|
| `front_left_motor` | [float][f]| _required_                    | PWM value for the front right motor (between 0.0 to 1.0)|
| `rear_right_motor` | [float][f]| _required_                    | PWM value for the front right motor (between 0.0 to 1.0)|
| `duration`      | [float][f] | _required_                      | Send command for this duration, in seconds     |
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [msgpackrpc.future.Future][F] | use `.join()` to make the call blocking/wait to finish—`client.method().join()`  |

---

#### `MultirotorClient.moveByRollPitchYawZAsync(roll, pitch, yaw, z, duration)`
> Move vehicle by rpy angles and altitude, in body FLU frame. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `roll`          | [float][f]| _required_                       | Desired roll angle, in radians.                   | 
| `pitch`         | [float][f]| _required_                       | Desired pitch angle, in radians.                   |
| `yaw`           | [float][f]| _required_                       | Desired yaw angle, in radians.                   |
| `z`             | [float][f] | _required_                      | Desired position in world (NED) Z axis            |
| `duration`      | [float][f] | _required_                      | Send command for this duration, in seconds     |
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |


| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [msgpackrpc.future.Future][F] | use `.join()` to make the call blocking/wait to finish—`client.method().join()`  |

---

#### `MultirotorClient.moveByRollPitchYawThrottleAsync(roll, pitch, yaw, throttle, duration)`
> Move vehicle by rpy angles and throttle, in body FLU frame. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `roll`          | [float][f]| _required_                       | Desired roll angle, in radians.                   | 
| `pitch`         | [float][f]| _required_                       | Desired pitch angle, in radians.                   |
| `yaw`           | [float][f]| _required_                       | Desired yaw angle, in radians.                   |
| `throttle`      | [float][f] | _required_                      | Desired throttle (between 0.0 to 1.0)         |
| `duration`      | [float][f] | _required_                      | Send command for this duration, in seconds     |
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [msgpackrpc.future.Future][F] | use `.join()` to make the call blocking/wait to finish—`client.method().join()`  |

---

#### `MultirotorClient.moveByRollPitchYawrateThrottleAsync(roll, pitch, yaw_rate, throttle, duration)`
> Move vehicle by angular rates and throttle, in body FLU frame. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `roll`          | [float][f]| _required_                       | Desired roll angle, in radians.                   | 
| `pitch`         | [float][f]| _required_                       | Desired pitch angle, in radians.                   |
| `yaw_rate`      | [float][f]| _required_                       | Desired yaw velocity, in radians per second.       |
| `throttle`      | [float][f] | _required_                      | Desired throttle (between 0.0 to 1.0)         |
| `duration`      | [float][f] | _required_                      | Send command for this duration, in seconds     |
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |


| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [msgpackrpc.future.Future][F] | use `.join()` to make the call blocking/wait to finish—`client.method().join()`  |

---

#### `MultirotorClient.moveByRollPitchYawrateZAsync(roll, pitch, yaw_rate, z, duration)`
> Move vehicle by angular rates and altitude, in body FLU frame. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `roll`          | [float][f]| _required_                       | Desired roll angle, in radians.                   | 
| `pitch`         | [float][f]| _required_                       | Desired pitch angle, in radians.                   |
| `yaw_rate`      | [float][f]| _required_                       | Desired yaw velocity, in radians per second.       |
| `z`             | [float][f] | _required_                      | Desired position in world (NED) Z axis            |
| `duration`      | [float][f] | _required_                      | Send command for this duration, in seconds     |
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [msgpackrpc.future.Future][F] | use `.join()` to make the call blocking/wait to finish—`client.method().join()`  |

---

#### `MultirotorClient.moveByAngleRatesZAsync(roll_rate, pitch_rate, yaw_rate, z, duration)`
> Move vehicle by anuglar rates and altitude, in body FLU frame. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `roll_rate`     | [float][f]| _required_                       | Desired roll velocity, in radians per second.       |
| `pitch_rate`    | [float][f]| _required_                       | Desired pitch velocity, in radians per second.       |
| `yaw_rate`      | [float][f]| _required_                       | Desired yaw velocity, in radians per second.       |
| `z`             | [float][f] | _required_                      | Desired position in world (NED) Z axis            |
| `duration`      | [float][f] | _required_                      | Send command for this duration, in seconds     |
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |


| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [msgpackrpc.future.Future][F] | use `.join()` to make the call blocking/wait to finish—`client.method().join()`  |

---

#### `MultirotorClient.moveByAngleRatesThrottleAsync(roll_rate, pitch_rate, yaw_rate, throttle, duration)`
> Move vehicle by angular rates and throttle, in body FLU frame. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `roll_rate`     | [float][f]| _required_                       | Desired roll velocity, in radians per second.       |
| `pitch_rate`    | [float][f]| _required_                       | Desired pitch velocity, in radians per second.       |
| `yaw_rate`      | [float][f]| _required_                       | Desired yaw velocity, in radians per second.       |
| `throttle`      | [float][f] | _required_                      | Desired throttle (between 0.0 to 1.0)         |
| `duration`      | [float][f] | _required_                      | Send command for this duration, in seconds     |
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |


| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [msgpackrpc.future.Future][F] | use `.join()` to make the call blocking/wait to finish—`client.method().join()`  |

---

#### `MultirotorClient.setAngleRateControllerGains()`
> Sets angle gains for ALL move*() APIs.

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `angle_rate_gains`| [AngleRateControllerGains][a]| _optional_, default=`AngleRateControllerGains()`| Correspond to the roll, pitch, yaw axes, defined in the body frame.| 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---

#### `MultirotorClient.setAngleLevelControllerGains()` 
> Sets angle level controller gains (used by any API setting angle references - for ex: moveByRollPitchYawZAsync(), moveByRollPitchYawThrottleAsync(), etc)

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `angle_rate_gains`| [AngleRateControllerGains][a]| _optional_, default=`AngleRateControllerGains()`| Correspond to the roll, pitch, yaw axes, defined in the body frame.| 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---

#### `MultirotorClient.setVelocityControllerGains()` 
> Sets velocity controller gains for moveByVelocityAsync().


| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `velocity_gains`| [VelocityControllerGains][v]| _optional_, default=`VelocityControllerGains()`| Correspond to the world X, Y, Z axes.| 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---

#### `MultirotorClient.setPositionControllerGains()`
> Sets position controller gains for moveByPositionAsync.

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `position_gains`| [PositionControllerGains][p]| _optional_, default=`PositionControllerGains()`| Correspond to the world X, Y, Z axes.| 
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---

#### `MultirotorClient.getMultirotorState()` 
> Gets the current state of vehicle. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `vehicle_name`  | [str][s] | _optional_, default=`''   `       | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorState][state]      | State the of the vehicle.                                                              |

---

[p]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L483
[v]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L464
[a]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L445
[f]: https://docs.python.org/3/library/functions.html#float
[s]: https://docs.python.org/3/library/stdtypes.html#str
[i]: https://docs.python.org/3/library/functions.html#int
[F]: http://msgpack.org/rpc/javadoc/current/org/msgpack/rpc/Future.html
[settings]: https://github.com/microsoft/AirSim/blob/master/docs/multi_vehicle.md
[drivetrain]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L32
[yawmode]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L226
[state]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L341
[vec]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L51
[rc]: https://github.com/microsoft/AirSim/blob/827f1f55df68eb1d026390e6db06c9dd11152ba2/PythonClient/airsim/types.py#L233

# AirSim CPP API Documentation 

## Table of Contents
- [Vehicle Client](#RpcLibClientBase)
- [Car Client](#CarRpcLibClient)
- [Multirotor Client](#MultirotorRpcLibClient)

## `RpcLibClientBase`

#### `RpcLibClientBase::RpcLibClientBase(const string&  ip_address, uint16_t port, float timeout_sec)` 
> Constructor
 
---
 
#### `bool RpcLibClientBase::ping()` 
> If connection is established then this call will return true otherwise it will be blocked until timeout. 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [bool][b]                     | Returns whether call is successful                                                     |

---
 
#### `RpcLibClientBase::ConnectionState RpcLibClientBase::getConnectionState()` 
> Get state of connection 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [ConnectionState][conn]           | Returns state of connection                                                    |

---
 
#### `void RpcLibClientBase::enableApiControl(bool is_enabled, const std::string& vehicle_name)` 
 > Enables or disables API control for vehicle corresponding to vehicle_name. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `is_enabled`    | [bool][b]| _required_                        | Enable or Disable API                 |
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---
 
#### `bool RpcLibClientBase::isApiControlEnabled(const std::string& vehicle_name) const` 
> Return whether API control is enabled

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [bool][b]                     | Returns whether API control is enabled                                                   |

---
 
#### `int RpcLibClientBase::getClientVersion() const` 
> Get client version 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [int][i]                     | Client version                                                 |

---
 
#### `int RpcLibClientBase::getMinRequiredServerVersion() const` 
> Get minimum requared server version 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [int][i]                     | minimum requared server version                                                |

---
 
#### `int RpcLibClientBase::getMinRequiredClientVersion() const` 
> Get minimum requared client version 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [int][i]                     | minimum requared client version                                                |

---
 
#### `int RpcLibClientBase::getServerVersion() const` 
> Get server version 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [int][i]                     | Server version                                                 |

---
 
#### `void RpcLibClientBase::reset()` 
> Reset the vehicle to its original starting state.
 
---
 
#### `void RpcLibClientBase::confirmConnection()` 
 > Checks state of connection every 1 sec and reports it in Console so user can see the progress for connection.

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [bool][b]                     | Whether connection is established                                                 |

---
 
#### `bool RpcLibClientBase::armDisarm(bool arm, const std::string& vehicle_name)` 
 > Arms or disarms vehicle.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `arm`           | [bool][b]| _required_                        | True to arm, False to disarm the vehicle                |
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [bool][b]                     | Whether call was successful                                                    |

---
 
#### `msr::airlib::GeoPoint RpcLibClientBase::getHomeGeoPoint(const std::string& vehicle_name) const` 
 > Get the Home location of the vehicle.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| GeoPoint[geo]                 | Home location of the vehicle |

---
 
#### `msr::airlib::LidarData RpcLibClientBase::getLidarData(const std::string& lidar_name, const std::string& vehicle_name) const` 
 > Get information about LiDAR. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `lidar_name`    | [str][s] | _required_             | Name of LiDAR to get data from, specified in [`settings.json`][settings] | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [LidarData][lidar]            |    more information [here](https://github.com/microsoft/airsim/blob/master/docs/lidar.md)            | 

---
 
#### `msr::airlib::ImuBase::Output RpcLibClientBase::getImuData(const std::string& imu_name, const std::string& vehicle_name) const` 
 > Returns informaton about IMU. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `imu_name`      | [str][s] | _required_             | Name of IMU to get data from, specified in [`settings.json`][settings] | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [ImuBase][imu]                | more information [here](https://github.com/microsoft/airsim/blob/master/docs/sensors.md)      | 

---
 
#### `msr::airlib::BarometerBase::Output RpcLibClientBase::getBarometerData(const std::string& barometer_name, const std::string& vehicle_name) const` 
 > Returns information about barometer. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `barometer_name`| [str][s] | _required_             | Name of Barometer to get data from, specified in [`settings.json`][settings] | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [BarometerBase][baro]         | more information [here][https://github.com/microsoft/airsim/blob/master/docs/sensors.md]         | 

---
 
#### `msr::airlib::MagnetometerBase::Output RpcLibClientBase::getMagnetometerData(const std::string& magnetometer_name, const std::string& vehicle_name) const` 
 > Returns information about magnetometer. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `magnetometer_name`| [str][s] | _required_          | Name of Magnetometer to get data from, specified in [`settings.json`][settings] | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MagnetometerBase][mag]       |   more information [here][https://github.com/microsoft/airsim/blob/master/docs/sensors.md]      | 

---
 
#### `msr::airlib::GpsBase::Output RpcLibClientBase::getGpsData(const std::string& gps_name, const std::string& vehicle_name) const` 
 > Returns information about GPS. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `gps_name`      | [str][s] | _required_             | Name of GPS to get data from, specified in [`settings.json`][settings] | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [GpsBase][gps]                |   more information [here][https://github.com/microsoft/airsim/blob/master/docs/sensors.md]        | 

---
 
#### `msr::airlib::DistanceBase::Output RpcLibClientBase::getDistanceSensorData(const std::string& distance_sensor_name, const std::string& vehicle_name) const` 
 > Returns information about distance sensor. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `distance_sensor_name`| [str][s] | _required_       | Name of distance sensor to get data from, specified in [`settings.json`][settings] | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [DistanceBase][dist]    |    more information [here][https://github.com/microsoft/airsim/blob/master/docs/sensors.md]               | 

---
 
#### `vector<int> RpcLibClientBase::simGetLidarSegmentation(const std::string& lidar_name, const std::string& vehicle_name) const` 
 > Returns Segmentation ID of each point's collided object in the last Lidar update.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `lidar_name`    | [str][s] | _required_             | Name of LiDAR to get data from, specified in [`settings.json`][settings] | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [vector][v] of [int][i]              | Segmentation IDs of the objects | 

---
 
#### `bool RpcLibClientBase::simSetSegmentationObjectID(const std::string& mesh_name, int object_id, bool is_name_regex)` 
 > Set segmentation ID for specific objects. See https://microsoft.github.io/AirSim/image_apis/#segmentation for details. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `mesh_name`     | [str][s] | _required_  | Name of the mesh to set the ID of (supports regex) | 
| `object_id`     | [int][i] |  _required_ | Object ID to be set, range 0-255 | 
| `is_name_regex` | [bool][b] | _required_   | Whether the mesh name is a regex | 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [bool][b]                     | If the mesh was found | 

---
 
#### `int RpcLibClientBase::simGetSegmentationObjectID(const std::string& mesh_name) const` 
 > Returns Object ID for the given mesh name. Mapping of Object IDs to RGB values can be seen at https://microsoft.github.io/AirSim/seg_rgbs.txt. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `mesh_name`     | [str][s] | _required_                        | Name of the mesh to get the ID of | 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [int][i]                     | Returns object ID of the mesh | 

---
 
#### `CollisionInfo RpcLibClientBase::simGetCollisionInfo(const std::string& vehicle_name) const` 
 > Returns information aboout collision with vehicle. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [CollisionInfo][col]          |                       | 

---
 
#### `Pose RpcLibClientBase::simGetVehiclePose(const std::string& vehicle_name) const` 
 > Returns current pose of the vehicle. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [Pose][pose]                  |                            | 

---
 
#### `void RpcLibClientBase::simSetVehiclePose(const Pose& pose, bool ignore_collision, const std::string& vehicle_name)` 
 > Set the pose of the vehicle.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `pose`          | [Pose][pose]| _required_   | Desired Pose pf the vehicle | 
| `ignore_collision`| [bool][b] | _required_ | Whether to ignore any collision or not | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---
 
#### `void RpcLibClientBase::simSetTraceLine(const std::vector<float>& color_rgba, float thickness, const std::string & vehicle_name)` 
 > Modify the color and thickness of the line when Tracing is enabled.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `color_rgba`    | [vector][v] of [float][f]| _required_ | desired RGBA values from 0.0 to 1.0 | 
| `thickness`     | [float][f]| _optional_, default='1.0' | Thickness of the line | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---
 
#### `vector<ImageCaptureBase::ImageResponse> RpcLibClientBase::simGetImages(vector<ImageCaptureBase::ImageRequest> request, const std::string& vehicle_name)` 
 > Get multiple images. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `requests`      | [vector][v] of [ImageRequest][imgreq]| _required_ | Images required | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [vector][v] of [ImageResponse][imgres]|              | 

---
 
#### `vector<uint8_t> RpcLibClientBase::simGetImage(const std::string& camera_name, ImageCaptureBase::ImageType type, const std::string& vehicle_name)` 
 > Get a single image.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `camera_name`   | [str][s] | _required_                        | Name of the camera, for backwards compatibility, ID numbers such as 0,1,etc. can also be used | 
| `image_type`    | [ImageType][imgtype]| _required_                 | Type of image required | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [str][s]                      | Binary string literal of compressed png image | 

---
 
#### `vector<MeshPositionVertexBuffersResponse> RpcLibClientBase::simGetMeshPositionVertexBuffers()` 
 > Returns the static meshes that make up the scene. See https://microsoft.github.io/AirSim/meshes/ for details and how to use this. 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [vector][v] of [MeshPositionVertexBuffersResponse][mesh]|   more information [here][https://github.com/microsoft/AirSim/blob/master/docs/meshes.md]           | 

---
 
#### `void RpcLibClientBase::simPrintLogMessage(const std::string& message, std::string message_param, unsigned char  severity)` 
 > Prints the specified message in the simulator's window.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `message`       | [str][s] | _required_ | Message to be printed | 
| `message_param` | [str][s] | _required_    | Parameter to be printed next to the message | 
| `severity`      | [unsigned char][uchar] | _required_     | Range 0-3, inclusive, corresponding to the severity of the message | 

---
 
#### `void RpcLibClientBase::simFlushPersistentMarkers()` 
 > Clear any persistent markers - those plotted with setting `is_persistent=True`. 

---
 
#### `void RpcLibClientBase::simPlotPoints(const vector<Vector3r>& points, const vector<float>& color_rgba, float size, float duration, bool is_persistent)` 
 > Plot a [vector][v] of 3D points in World NED frame. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `points`        | [vector][v] of [Vector3r][vec]| _required_ | [vector][v] of Vector3r objects | 
| `color_rgba`    | [vector][v] of [float][f] | _required_    | desired RGBA values from 0.0 to 1.0 | 
| `size`          | [float][f] | _required_    | Size of plotted point | 
| `duration`      | [float][f] | _required_    | Duration (seconds) to plot for | 
| `is_persistent` | [bool][b] | _required_    | If set to True, the desired object will be plotted for infinite time. | 

---
 
#### `void RpcLibClientBase::simPlotLineStrip(const vector<Vector3r>& points, const vector<float>& color_rgba, float thickness, float duration, bool is_persistent)` 
 > Plots a line strip in World NED frame, defined from points[0] to points[1], points[1] to points[2], ... , points[n-2] to points[n-1]. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `points`        | [vector][v] of [Vector3r][vec]| _required_ | [vector][v] of Vector3r objects | 
| `color_rgba`    | [vector][v] of [float][f] | _required_    | desired RGBA values from 0.0 to 1.0 | 
| `thickness`     | [float][f] | _required_     | Thickness of line | 
| `duration`      | [float][f] | _required_    | Duration (seconds) to plot for | 
| `is_persistent` | [bool][b] | _required_    | If set to True, the desired object will be plotted for infinite time. | 

---
 
#### `void RpcLibClientBase::simPlotLineList(const vector<Vector3r>& points, const vector<float>& color_rgba, float thickness, float duration, bool is_persistent)` 
 > Plots a line strip in World NED frame, defined from points[0] to points[1], points[2] to points[3], ... , points[n-2] to points[n-1]. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `points`        | [vector][v] of [Vector3r][vec]| _required_ | [vector][v] of Vector3r objects | 
| `color_rgba`    | [vector][v] of [float][f] | _required_    | desired RGBA values from 0.0 to 1.0 | 
| `thickness`     | [float][f] | _required_     | Thickness of line | 
| `duration`      | [float][f] | _required_    | Duration (seconds) to plot for | 
| `is_persistent` | [bool][b] | _required_    | If set to True, the desired object will be plotted for infinite time. | 

---
 
#### `void RpcLibClientBase::simPlotArrows(const vector<Vector3r>& points_start, const vector<Vector3r>& points_end, const vector<float>& color_rgba, float thickness, float arrow_size, float duration, bool is_persistent)` 
 > Plots a [vector][v] of arrows in World NED frame, defined from points_start[0] to points_end[0], points_start[1] to points_end[1], ... , points_start[n-1] to points_end[n-1]. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `points_start`  | [vector][v] of [Vector3r][vec]| _required_ | [vector][v] of 3D start positions of arrow start positions, specified as Vector3r objects | 
| `points_end`    | [vector][v] of [Vector3r][vec]| _required_ | [vector][v] of 3D end positions of arrow start positions, specified as Vector3r objects | 
| `color_rgba`    | [vector][v] of [float][f] | _required_    | desired RGBA values from 0.0 to 1.0 | 
| `thickness`     | [float][f] | _required_     | Thickness of line | 
| `arrow_size`    | [float][f] | _required_     | Size of arrow head | 
| `duration`      | [float][f] | _required_    | Duration (seconds) to plot for | 
| `is_persistent` | [bool][b] | _required_    | If set to True, the desired object will be plotted for infinite time. | 

---
 
#### `void RpcLibClientBase::simPlotStrings(const vector<std::string>& strings, const vector<Vector3r>& positions, float scale, const vector<float>& color_rgba, float duration)` 
 > Plots a [vector][v] of strings at desired positions in World NED frame.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `strings`       | [vector][v] of [str][s] | _required_ | [vector][v] of strings to plot | 
| `positions`    | [vector][v] of [Vector3r][vec]| _required_ | [vector][v] of positions where the strings should be plotted. Should be in one-to-one correspondence with the strings' [vector][v] | 
| `scale`         | [float][f] | _required_    | Font scale of transform name | 
| `color_rgba`    | [vector][v] of [float][f] | _required_    | desired RGBA values from 0.0 to 1.0 | 
| `duration`      | [float][f] | _required_    | Duration (seconds) to plot for | 

---
 
#### `void RpcLibClientBase::simPlotTransforms(const vector<Pose>& poses, float scale, float thickness, float duration, bool is_persistent)` 
 > Plots a [vector][v] of transforms in World NED frame.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `poses`         | [vector][v] of [Pose][pose] | _required_     | [vector][v] of Pose objects representing the transforms to plot | 
| `scale`         | [float][f] | _required_    | Font scale of transform name | 
| `thickness`     | [float][f] | _required_     | Thickness of line | 
| `duration`      | [float][f] | _required_    | Duration (seconds) to plot for | 
| `is_persistent` | [bool][b] | _required_    | If set to True, the desired object will be plotted for infinite time. | 

---
 
#### `void RpcLibClientBase::simPlotTransformsWithNames(const vector<Pose>& poses, const vector<std::string>& names, float tf_scale, float tf_thickness, float text_scale, const vector<float>& text_color_rgba, float duration)` 
 > Plots a [vector][v] of transforms with their names in World NED frame.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `poses`         | [vector][v] of [Pose][pose] | _required_     | [vector][v] of Pose objects representing the transforms to plot | 
| `names`         | [vector][v] of [str][s] | _required_ | [vector][v] of strings with one-to-one correspondence to [vector][v] of poses | 
| `tf_scale`      | [float][f] | _required_    | Length of transforms' axes | 
| `tf_thickness`  | [float][f] | _required_    | Thickness of transforms' axes | 
| `text_scale`    | [float][f] | _required_    | Font scale of transform name | 
| `text_color_rgba` | [vector][v] of [float][f] | _required_    | desired RGBA values from 0.0 to 1.0 | 
| `duration`      | [float][f] | _required_    | Duration (seconds) to plot for | 

---
 
#### `bool RpcLibClientBase::simIsPaused() const` 
 > Returns true if the simulation is paused. 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [bool][b]                     | Whether simulation is paused                                                  |

---
 
#### `void RpcLibClientBase::simPause(bool is_paused)` 
 > Pauses simulation.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `is_paused`     | [bool][b]| _required_                        | True to pause the simulation, False to release |

---
 
#### `void RpcLibClientBase::simContinueForTime(double seconds)` 
 > Continue the simulation for the specified number of seconds.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `seconds`       | [double][d]| _required_                      | Time to run the simulation for |

---
 
#### `void RpcLibClientBase::simEnableWeather(bool enable)` 
 > Enable Weather effects. Needs to be called before using `simSetWeatherParameter` API.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `enable`        | [bool][b]| _required_ | True to enable, False to disable | 

---
 
#### `void RpcLibClientBase::simSetWeatherParameter(WorldSimApiBase::WeatherParameter param, float val)` 
 > Enable various weather effects.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `param`         | [WeatherParameter][wea] | _required_ | Weather effect to be enabled | 
| `val`           | [float][f] | _required_ | Intensity of the effect, Range 0-1 | 

---
 
#### `void RpcLibClientBase::simSetTimeOfDay(bool is_enabled, const string& start_datetime, bool is_start_datetime_dst, float celestial_clock_speed, float update_interval_secs, bool move_sun)` 
 > Control the position of Sun in the environment.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `is_enabled`    | [bool][b]| _required_ | True to enable time-of-day effect, False to reset the position to original | 
| `start_datetime`| [str][s] | _required_    | ate & Time in %Y-%m-%d %H:%M:%S format, e.g. `2018-02-12 15:20:00` | 
| `is_start_datetime_dst`| [bool][b]| _required_    | True to adjust for Daylight Savings Time |
| `celestial_clock_speed`| [float][f]| _required_    | Run celestial clock faster or slower than simulation clock |
| `update_interval_secs` | [float][f]| _required_    | Interval to update the Sun's position |
| `move_sun` | [bool][b] | _required_    |  Whether or not to move the Sun |

---
 
#### `vector<string> RpcLibClientBase::simListSceneObjects(const string& name_regex) const` 
 > [vector][v] the objects present in the environment.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `name_regex`    | [str][s] | _required_           | String to match actor names against, e.g. "Cylinder.*" | 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [vector][v] of [str][s]              | [vector][v] containing all the names | 

---
 
#### `std::vector<std::string> RpcLibClientBase::simSwapTextures(const std::string& tags, int tex_id, int component_id, int material_id)` 
 > Runtime Swap Texture API.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `tags`          | [str][s] | _required_ | string of "," or ", " delimited tags to identify on which actors to perform the swap| 
| `tex_id`        | [int][i] | _required_    | indexes the array of textures assigned to each actor undergoing a swap | 
| `component_id`  | [int][i] | _required_    |               |
| `material_id`   | [int][i] | _required_    |               |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [vector][v] of [str][s]              | [vector][v] of objects which matched the provided tags and had the texture swap perfomed   | 

---
 
#### `msr::airlib::Pose RpcLibClientBase::simGetObjectPose(const std::string& object_name) const` 
 > Returns current pose of the object.  

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `object_name`   | [str][s] | _required_ | Object to get the Pose of | 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [Pose][pose]                  |                     | 

---
 
#### `bool RpcLibClientBase::simSetObjectPose(const std::string& object_name, const msr::airlib::Pose& pose, bool teleport)` 
 > Set the pose of the object(actor) in the environment.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `object_name`   | [str][s] | _required_ | Object to get the Pose of | 
| `pose`          | [Pose][pose]| _required_   | Desired Pose pf the vehicle | 
| `teleport`      | [bool][b] | _required_    | Whether to move the object immediately without affecting their velocity |  

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [bool][b]                     | Whether the move was successful   | 

---
 
#### `CameraInfo RpcLibClientBase::simGetCameraInfo(const std::string& camera_name, const std::string& vehicle_name) const` 
 > Get details about the camera.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `camera_name`   | [str][s] | _required_ | Name of the camera, for backwards compatibility, ID numbers such as 0,1,etc. can also be used | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [CameraInfo][cam]             |      | 

---
 
#### `void RpcLibClientBase::simSetCameraOrientation(const std::string& camera_name, const Quaternionr& orientation, const std::string& vehicle_name)` 
 > Control the orientation of a selected camera.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `camera_name`   | [str][s] | _required_ | Name of the camera to be controlled | 
| `orientation`   | [Quaternionr][quat] | _required_ | Quaternion representing the desired orientation of the camera | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---
 
#### `void RpcLibClientBase::simSetCameraFov(const std::string& camera_name, float fov_degrees, const std::string& vehicle_name)` 
 > Control the field of view of a selected camera.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `camera_name`   | [str][s] | _required_ | Name of the camera to be controlled | 
| `fov_degrees`   | [float][f]| _required_ | Value of field of view in degrees | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---
 
#### `msr::airlib::Kinematics::State RpcLibClientBase::simGetGroundTruthKinematics(const std::string& vehicle_name) const` 
 > Get Ground truth kinematics of the vehicle. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [Kinematics::State][kin]        | Ground truth of the vehicle | 

---
 
#### `msr::airlib::Environment::State RpcLibClientBase::simGetGroundTruthEnvironment(const std::string& vehicle_name) const` 
 > Get ground truth environment state. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [Environment::State][env]       | Ground truth environment state | 

---
 
#### `void RpcLibClientBase::cancelLastTask(const std::string& vehicle_name)` 
 > Cancel previous Async task. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---
 
#### `RpcLibClientBase* RpcLibClientBase::waitOnLastTask(bool* task_result, float timeout_sec)` 
 > Wait for the last Async task to complete. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `task_result`   | [bool*][b]| _required_   |                                | 
| `timeout_sec`   | [float][f] | _required_   | Time for the task to complete | 

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [RpcLibClientBase*][]                     | Result of the last task | 

---
 
#### `void* RpcLibClientBase::getClient()` 
 
---
 
#### `const void* RpcLibClientBase::getClient() const` 
 
---
 

## `CarRpcLibClient`

#### `CarRpcLibClient::CarRpcLibClient(const string&  ip_address, uint16_t port, float timeout_sec)`
> Constructor

---

#### `void CarRpcLibClient::setCarControls(const CarApiBase::CarControls& controls, const std::string& vehicle_name)`
> Control the car using throttle, steering, brake, etc.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `controls`      | [CarControls][Cctl]| _required_              | Struct containing control values      | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---

#### `CarApiBase::CarState CarRpcLibClient::getCarState(const std::string& vehicle_name)`
> Get current state of the vehicle.

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [CarState][Cstate]            | State the of the vehicle.                                                              |

---

#### `CarApiBase::CarControls CarRpcLibClient::getCarControls(const std::string& vehicle_name)` 
> Get current control values of the vehicle. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                       |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------|
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [CarControls][Cctl]           | Struct containing control values of the vehicle.                                       |

---


## `MultirotorRpcLibClient`
 
#### `MultirotorRpcLibClient::MultirotorRpcLibClient(const string&  ip_address, uint16_t port, float timeout_sec)` 
 > Constructor 
 
---
 
#### `MultirotorRpcLibClient* MultirotorRpcLibClient::takeoffAsync(float timeout_sec, const std::string& vehicle_name)` 
 > takeoff vehicle to 3m above ground; vehicle should not be moving when this API is used

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `timeout_sec`   | [float][f] | _required_             | Takeoff time, in seconds.                         |
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorRpcLibClient*][F] |    |

---
 
#### `MultirotorRpcLibClient* MultirotorRpcLibClient::landAsync(float timeout_sec, const std::string& vehicle_name)` 
 > Land the vehicle

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `timeout_sec`   | [float][f] | _required_             | Landing time, in seconds.                         |
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorRpcLibClient*][F] |    |

---
 
#### `MultirotorRpcLibClient* MultirotorRpcLibClient::goHomeAsync(float timeout_sec, const std::string& vehicle_name)` 
 > Return vehicle to Home i.e. Launch location

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `timeout_sec`   | [float][f] | _required_             | Travel time, in seconds. Process will end after this time regardless whether vehicle as reached destination  |
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorRpcLibClient*][F] |    |

---
 
#### `MultirotorRpcLibClient* MultirotorRpcLibClient::moveByMotorPWMsAsync(float front_right_pwm, float rear_left_pwm, float front_left_pwm, float rear_right_pwm, float duration, const std::string& vehicle_name)` 
 > Directly control the motors using PWM values. This is the lowest level of control in AirSim. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `front_right_motor`| [float][f]| _required_                    | PWM value for the front right motor (between 0.0 to 1.0)|
| `rear_left_motor`  | [float][f]| _required_                    | PWM value for the front right motor (between 0.0 to 1.0)|
| `front_left_motor` | [float][f]| _required_                    | PWM value for the front right motor (between 0.0 to 1.0)|
| `rear_right_motor` | [float][f]| _required_                    | PWM value for the front right motor (between 0.0 to 1.0)|
| `duration`      | [float][f] | _required_                      | Send command for this duration, in seconds     |
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorRpcLibClient*][F] |    |

---
 
#### `MultirotorRpcLibClient* MultirotorRpcLibClient::moveByRollPitchYawZAsync(float roll, float pitch, float yaw, float z, float duration, const std::string& vehicle_name)` 
 > Move vehicle by rpy angles and altitude, in body FLU frame. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `roll`          | [float][f]| _required_                       | Desired roll angle, in radians.                   | 
| `pitch`         | [float][f]| _required_                       | Desired pitch angle, in radians.                   |
| `yaw`           | [float][f]| _required_                       | Desired yaw angle, in radians.                   |
| `z`             | [float][f] | _required_                      | Desired position in world (NED) Z axis            |
| `duration`      | [float][f] | _required_                      | Send command for this duration, in seconds     |
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |


| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorRpcLibClient*][F] |    |

---
 
#### `MultirotorRpcLibClient* MultirotorRpcLibClient::moveByRollPitchYawThrottleAsync(float roll, float pitch, float yaw, float throttle, float duration, const std::string& vehicle_name)` 
 > Move vehicle by rpy angles and throttle, in body FLU frame. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `roll`          | [float][f]| _required_                       | Desired roll angle, in radians.                   | 
| `pitch`         | [float][f]| _required_                       | Desired pitch angle, in radians.                   |
| `yaw`           | [float][f]| _required_                       | Desired yaw angle, in radians.                   |
| `throttle`      | [float][f] | _required_                      | Desired throttle (between 0.0 to 1.0)         |
| `duration`      | [float][f] | _required_                      | Send command for this duration, in seconds     |
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorRpcLibClient*][F] |    |

---
 
#### `MultirotorRpcLibClient* MultirotorRpcLibClient::moveByRollPitchYawrateThrottleAsync(float roll, float pitch, float yaw_rate, float throttle, float duration, const std::string& vehicle_name)` 
 > Move vehicle by angular rates and throttle, in body FLU frame. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `roll`          | [float][f]| _required_                       | Desired roll angle, in radians.                   | 
| `pitch`         | [float][f]| _required_                       | Desired pitch angle, in radians.                   |
| `yaw_rate`      | [float][f]| _required_                       | Desired yaw velocity, in radians per second.       |
| `throttle`      | [float][f] | _required_                      | Desired throttle (between 0.0 to 1.0)         |
| `duration`      | [float][f] | _required_                      | Send command for this duration, in seconds     |
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |


| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorRpcLibClient*][F] |    |

---
 
#### `MultirotorRpcLibClient* MultirotorRpcLibClient::moveByRollPitchYawrateZAsync(float roll, float pitch, float yaw_rate, float z, float duration, const std::string& vehicle_name)` 
 > Move vehicle by angular rates and altitude, in body FLU frame. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `roll`          | [float][f]| _required_                       | Desired roll angle, in radians.                   | 
| `pitch`         | [float][f]| _required_                       | Desired pitch angle, in radians.                   |
| `yaw_rate`      | [float][f]| _required_                       | Desired yaw velocity, in radians per second.       |
| `z`             | [float][f] | _required_                      | Desired position in world (NED) Z axis            |
| `duration`      | [float][f] | _required_                      | Send command for this duration, in seconds     |
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorRpcLibClient*][F] |    |

---
 
#### `MultirotorRpcLibClient* MultirotorRpcLibClient::moveByAngleRatesZAsync(float roll_rate, float pitch_rate, float yaw_rate, float z, float duration, const std::string& vehicle_name)` 
 > Move vehicle by anuglar rates and altitude, in body FLU frame. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `roll_rate`     | [float][f]| _required_                       | Desired roll velocity, in radians per second.       |
| `pitch_rate`    | [float][f]| _required_                       | Desired pitch velocity, in radians per second.       |
| `yaw_rate`      | [float][f]| _required_                       | Desired yaw velocity, in radians per second.       |
| `z`             | [float][f] | _required_                      | Desired position in world (NED) Z axis            |
| `duration`      | [float][f] | _required_                      | Send command for this duration, in seconds     |
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |


| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorRpcLibClient*][F] |    |

---
 
#### `MultirotorRpcLibClient* MultirotorRpcLibClient::moveByAngleRatesThrottleAsync(float roll_rate, float pitch_rate, float yaw_rate, float throttle, float duration, const std::string& vehicle_name)` 
 > Move vehicle by angular rates and throttle, in body FLU frame. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `roll_rate`     | [float][f]| _required_                       | Desired roll velocity, in radians per second.       |
| `pitch_rate`    | [float][f]| _required_                       | Desired pitch velocity, in radians per second.       |
| `yaw_rate`      | [float][f]| _required_                       | Desired yaw velocity, in radians per second.       |
| `throttle`      | [float][f] | _required_                      | Desired throttle (between 0.0 to 1.0)         |
| `duration`      | [float][f] | _required_                      | Send command for this duration, in seconds     |
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |


| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorRpcLibClient*][F] |    |

---
 
#### `MultirotorRpcLibClient* MultirotorRpcLibClient::moveByVelocityAsync(float vx, float vy, float vz, float duration, DrivetrainType drivetrain, const YawMode& yaw_mode, const std::string& vehicle_name)` 
 > Move vehicle at desired velocity.AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `vx`            | [float][f] | _required_                      | Desired velocity in world (NED) X axis            |
| `vy`            | [float][f] | _required_                      | Desired velocity in world (NED) Y axis            |
| `vz`            | [float][f] | _required_                      | Desired velocity in world (NED) Z axis            |
| `duration`      | [float][f] | _required_                      | Amount of time to send this command for , in seocnds  |
| `drivetrain`    | [DrivetrainType][drivetrain] | _required_     | more information [here][https://microsoft.github.io/AirSim/apis/#drivetrain]                |
| `yaw_mode`    | [YawMode][yawmode] | _required_     |   more information [here][https://microsoft.github.io/AirSim/apis/#yaw_mode]              |
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorRpcLibClient*][F] |    |

---
 
#### `MultirotorRpcLibClient* MultirotorRpcLibClient::moveByVelocityZAsync(float vx, float vy, float z, float duration, DrivetrainType drivetrain, const YawMode& yaw_mode, const std::string& vehicle_name)` 
 > Move vehicle at desired velocity (XY only). AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `vx`            | [float][f] | _required_                      | Desired velocity in world (NED) X axis            |
| `vy`            | [float][f] | _required_                      | Desired velocity in world (NED) Y axis            |
| `z`             | [float][f] | _required_                      | Desired position in world (NED) Z axis            |
| `duration`      | [float][f] | _required_                      | Amount of time to send this command for , in seocnds  |
| `drivetrain`    | [DrivetrainType][drivetrain] | _required_     |    more information [here][https://microsoft.github.io/AirSim/apis/#drivetrain]             |
| `yaw_mode`    | [YawMode][yawmode] | _required_     |   more information [here][https://microsoft.github.io/AirSim/apis/#yaw_mode]               |
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorRpcLibClient*][F] |    |

---
 
#### `MultirotorRpcLibClient* MultirotorRpcLibClient::moveOnPathAsync(const vector<Vector3r>& path, float velocity, float duration, DrivetrainType drivetrain, const YawMode& yaw_mode, float lookahead, float adaptive_lookahead, const std::string& vehicle_name)` 
 > move vehicle along coordinates. This is the highest level of control in AirSim. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `path`          | [vector][v] of [vector3r][vec] | _required_                        | Desired path                         |
| `velocity`      | [float][f] | _required_                      | Desired linear velocity  |
| `duration`   | [float][f] | _required_             | Travel time, in seconds. Process will end after this time regardless whether vehicle as reached destination  |
| `drivetrain`    | [DrivetrainType][drivetrain] | _required_     |   more information [here][https://microsoft.github.io/AirSim/apis/#drivetrain]              |
| `yaw_mode`    | [YawMode][yawmode] | _required_     |   more information [here][https://microsoft.github.io/AirSim/apis/#yaw_mode]               |
| `lookahead`     | [float][f] | _required_             |   more information [here][https://microsoft.github.io/AirSim/apis/#lookahead-and-adaptive_lookahead]                        |
| `adaptive_lookahead`| [float][f]| _required_           |   more information [here][https://microsoft.github.io/AirSim/apis/#lookahead-and-adaptive_lookahead]                       |    
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorRpcLibClient*][F] |    |

---
 
#### `MultirotorRpcLibClient* MultirotorRpcLibClient::moveToPositionAsync(float x, float y, float z, float velocity, float timeout_sec,  DrivetrainType drivetrain, const YawMode& yaw_mode, float lookahead, float adaptive_lookahead, const std::string& vehicle_name)` 
 > Move vehicle to desired position. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `x`            | [float][f] | _required_                      | Desired velocity in world (NED) X axis            |
| `y`            | [float][f] | _required_                      | Desired velocity in world (NED) Y axis            |
| `z`             | [float][f] | _required_                      | Desired position in world (NED) Z axis            |
| `velocity`      | [float][f] | _required_                      | Desired linear velocity  |
| `timeout_sec`   | [float][f] | _required_             | Travel time, in seconds. Process will end after this time regardless whether vehicle as reached destination  |
| `drivetrain`    | [DrivetrainType][drivetrain] | _required_     |      more information [here][https://microsoft.github.io/AirSim/apis/#drivetrain]           |
| `yaw_mode`    | [YawMode][yawmode] | _required_     | more information [here][https://microsoft.github.io/AirSim/apis/#yaw_mode]                 |
| `lookahead`     | [float][f] | _required_             |   more information [here][https://microsoft.github.io/AirSim/apis/#lookahead-and-adaptive_lookahead]                        |
| `adaptive_lookahead`| [float][f]| _required_           |   more information [here][https://microsoft.github.io/AirSim/apis/#lookahead-and-adaptive_lookahead]                       |    
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorRpcLibClient*][F] |    |

---
 
#### `MultirotorRpcLibClient* MultirotorRpcLibClient::moveToZAsync(float z, float velocity, float timeout_sec, const YawMode& yaw_mode, float lookahead, float adaptive_lookahead, const std::string& vehicle_name)` 
 > Move vehicle to desired altitude. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `z`             | [float][f] | _required_                      | Desired position in world (NED) Z axis            |
| `velocity`      | [float][f] | _required_                      | Desired linear velocity  |
| `timeout_sec`   | [float][f] | _required_             | Travel time, in seconds. Process will end after this time regardless whether vehicle as reached destination  |
| `yaw_mode`      | [YawMode][yawmode] | _required_     |     more information [here][https://microsoft.github.io/AirSim/apis/#yaw_mode]             |
| `lookahead`     | [float][f] | _required_             |   more information [here][https://microsoft.github.io/AirSim/apis/#lookahead-and-adaptive_lookahead]                        |
| `adaptive_lookahead`| [float][f]| _required_           |   more information [here][https://microsoft.github.io/AirSim/apis/#lookahead-and-adaptive_lookahead]                       |    
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorRpcLibClient*][F] |    |

---
 
#### `MultirotorRpcLibClient* MultirotorRpcLibClient::moveByManualAsync(float vx_max, float vy_max, float z_min, float duration, DrivetrainType drivetrain, const YawMode& yaw_mode, const std::string& vehicle_name)` 
 > Read current RC state and use it to control the vehicles. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `vx_max`        | [float][f] | _required_                      | max velocity allowed in X direction               |
| `vy_max`        | [float][f] | _required_                      | max velocity allowed in Y direction               |
| `vz_max`        | [float][f] | _required_                      | max velocity allowed in Z direction               |
| `z_min`         | [float][f] | _required_                      | min z allowed for vehicle position                |
| `duration`      | [float][f] | _required_                      | after this duration vehicle would switch back to non-manual mode  |
| `drivetrain`    | [DrivetrainType][drivetrain] | _required_     |    more information [here][https://microsoft.github.io/AirSim/apis/#drivetrain]             |
| `yaw_mode`    | [YawMode][yawmode] | _required_     |    more information [here][https://microsoft.github.io/AirSim/apis/#yaw_mode]              |
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorRpcLibClient*][F] |    |

---
 
#### `MultirotorRpcLibClient* MultirotorRpcLibClient::rotateToYawAsync(float yaw, float timeout_sec, float margin, const std::string& vehicle_name)` 
 > Change vehicle yaw angle. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `yaw`           | [float][f]| _required_                       | Desired yaw angle in world (NED) frame, in degrees  | 
| `timeout_sec`   | [float][f] | _required_             | Travel time, in seconds. Process will end after this time regardless whether vehicle as reached destination  |
| `margin`        | [float][f] | _required_              |                                                   | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorRpcLibClient*][F] |    |

---
 
#### `MultirotorRpcLibClient* MultirotorRpcLibClient::rotateByYawRateAsync(float yaw_rate, float duration, const std::string& vehicle_name)` 
 > Change vehicle yaw rate. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `yaw_rate`      |[float][f]| _required_                        | Desired yaw velocity in world (NED) frame, in degrees per second  | 
| `duration`      | [float][f] | _required_                      | after this duration vehicle would switch back to non-manual mode  |
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

            
| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorRpcLibClient*][F] |    |

---
 
#### `MultirotorRpcLibClient* MultirotorRpcLibClient::hoverAsync(const std::string& vehicle_name)` 
 > Make vehicle hover. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |


| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorRpcLibClient*][F] |    |

---
 
#### `void MultirotorRpcLibClient::setAngleLevelControllerGains(const vector<float>& kp, const vector<float>& ki, const vector<float>& kd, const std::string& vehicle_name)` 
 > Sets angle level controller gains (used by any API setting angle references - for ex: moveByRollPitchYawZAsync(), moveByRollPitchYawThrottleAsync(), etc)

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `kp`            | [vector][v] of [float][f] | _required_       | proportional gains | 
| `ki`            | [vector][v] of [float][f] | _required_       | integral gains | 
| `kd`            | [vector][v] of [float][f] | _required_       | derivative gains | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---
 
#### `void MultirotorRpcLibClient::setAngleRateControllerGains(const vector<float>& kp, const vector<float>& ki, const vector<float>& kd, const std::string& vehicle_name)` 
 > Sets angle gains for ALL move*() APIs.

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `kp`            | [vector][v] of [float][f] | _required_       | proportional gains | 
| `ki`            | [vector][v] of [float][f] | _required_       | integral gains | 
| `kd`            | [vector][v] of [float][f] | _required_       | derivative gains | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---
 
#### `void MultirotorRpcLibClient::setVelocityControllerGains(const vector<float>& kp, const vector<float>& ki, const vector<float>& kd, const std::string& vehicle_name)` 
 > Sets velocity controller gains for moveByVelocityAsync().


| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `kp`            | [vector][v] of [float][f] | _required_       | proportional gains | 
| `ki`            | [vector][v] of [float][f] | _required_       | integral gains | 
| `kd`            | [vector][v] of [float][f] | _required_       | derivative gains | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---
 
#### `void MultirotorRpcLibClient::setPositionControllerGains(const vector<float>& kp, const vector<float>& ki, const vector<float>& kd, const std::string& vehicle_name)` 
 > Sets position controller gains for moveByPositionAsync.

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `kp`            | [vector][v] of [float][f] | _required_       | proportional gains | 
| `ki`            | [vector][v] of [float][f] | _required_       | integral gains | 
| `kd`            | [vector][v] of [float][f] | _required_       | derivative gains | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---
 
#### `bool MultirotorRpcLibClient::setSafety(SafetyEval::SafetyViolationType enable_reasons, float obs_clearance, SafetyEval::ObsAvoidanceStrategy obs_startegy, float obs_avoidance_vel, const Vector3r& origin, float xy_length, float max_z, float min_z, const std::string& vehicle_name)` 
 
---
 
#### `MultirotorState MultirotorRpcLibClient::getMultirotorState(const std::string& vehicle_name)` 
 > Gets the current state of vehicle. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorState][state]      | State the of the vehicle.                                                              |

---
 
#### `void MultirotorRpcLibClient::moveByRC(const RCData& rc_data, const std::string& vehicle_name)` 
 > Move vehicle with remote control. AirSim uses carrot following algorithm. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `rcdata`        | [RCData][rc]| _required_                     |                                                   | 
| `vehicle_name`  | [str][s] | _required_          | Name of the vehicle, under tag `Vehicles` in [`settings.json`][settings]     |

---
 
#### `MultirotorRpcLibClient* MultirotorRpcLibClient::waitOnLastTask(bool* task_result, float timeout_sec)` 
> Return when the last task is complete. 

| **Args**        | **Type** | **Required or Optional**          | **Description**                                   |
| :-------------- |:--------:| :---------------------------------| :-------------------------------------------------|
| `task_result`   | [bool*][b]| _required_                       | Whether the task is successful                     | 
| `timeout_sec`   | [float][f]| _required_                       | Amount of time to wait                          | 


| **Returns**                   | **Description**                                                                        |
| :---------------------------- | :--------------------------------------------------------------------------------------|
| [MultirotorState][state]      | State the of the vehicle.                                                              |

---
[b]: https://en.cppreference.com/w/cpp/language/bool_literal
[conn]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/api/RpcLibClientBase.hpp#L24
[geo]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/common/CommonStructs.hpp#L148
[wea]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/api/WorldSimApiBase.hpp#L14
[imgtype]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/common/ImageCaptureBase.hpp#L16
[imgreq]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/common/ImageCaptureBase.hpp#L28
[imgres]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/common/ImageCaptureBase.hpp#L46
[mesh]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/common/CommonStructs.hpp#L307
[col]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/common/CommonStructs.hpp#L207
[pose]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/common/VectorMath.hpp#L47
[cam]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/common/CommonStructs.hpp#L233
[quat]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/api/RpcLibAdapatorsBase.hpp#L92
[kin]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/physics/Kinematics.hpp#L13
[env]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/physics/Environment.hpp#L14
[imu]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/sensors/imu/ImuBase.hpp#L13
[baro]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/sensors/barometer/BarometerBase.hpp#L13
[mag]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/sensors/magnetometer/MagnetometerBase.hpp#L13
[gps]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/sensors/gps/GpsBase.hpp#L14
[dist]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/sensors/distance/DistanceBase.hpp#L13
[lidar]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/common/CommonStructs.hpp#L298
[d]: https://en.cppreference.com/w/cpp/language/types
[uchar]: https://en.cppreference.com/w/cpp/language/types
[Cctl]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/vehicles/car/api/CarApiBase.hpp#L19
[Cstate]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/vehicles/car/api/CarApiBase.hpp#L52
[v]: https://en.cppreference.com/w/cpp/container/vector
[f]: https://en.cppreference.com/w/cpp/language/types
[s]: https://en.cppreference.com/w/cpp/string/basic_string
[i]: https://en.cppreference.com/w/cpp/language/types
[i]: https://en.cppreference.com/w/cpp/language/types
[F]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/vehicles/multirotor/api/MultirotorRpcLibClient.hpp#L18
[settings]: https://github.com/microsoft/AirSim/blob/master/docs/multi_vehicle.md
[drivetrain]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/vehicles/multirotor/api/MultirotorCommon.hpp#L10
[yawmode]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/vehicles/multirotor/api/MultirotorCommon.hpp#L21
[state]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/vehicles/multirotor/api/MultirotorCommon.hpp#L70
[vec]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/api/RpcLibAdapatorsBase.hpp#L39
[rc]: https://github.com/microsoft/AirSim/blob/b7a65bb7f7a9471a2ec0ce6f573512b880d3197a/AirLib/include/common/CommonStructs.hpp#L259


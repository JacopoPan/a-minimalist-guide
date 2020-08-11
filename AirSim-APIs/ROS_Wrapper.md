# ROS Wrapper Documentation


## `/airsim_node` node

### Publications
 * `/airsim_node/VEHICLE_NAME/global_gps` [sensor_msgs/NavSatFix](https://docs.ros.org/api/sensor_msgs/html/msg/NavSatFix.html)
 > This the current GPS coordinates of the drone in airsim.
 
 * `/airsim_node/VEHICLE_NAME/odom_local_ned` [nav_msgs/Odometry](https://docs.ros.org/api/nav_msgs/html/msg/Odometry.html)
 > Odometry in NED frame wrt take-off point.
 
 * `/airsim_node/origin_geo_point` [airsim_ros_pkgs/GPSYaw](https://github.com/microsoft/AirSim/blob/master/ros/src/airsim_ros_pkgs/msg/GPSYaw.msg)
 > GPS coordinates corresponding to global NED frame. This is set in the airsim's `settings.json` file under the `OriginGeopoint` key.

 * `/tf` [tf2_msgs/TFMessage](https://docs.ros.org/api/tf2_msgs/html/msg/TFMessage.html)
 
 
### Subcriptions
 * `/airsim_node/VEHICLE_NAME/vel_cmd_body_frame` [airsim_ros_pkgs/VelCmd](https://github.com/microsoft/AirSim/tree/master/ros/src/airsim_ros_pkgs/msg/VelCmd.msg)
 > Commanded velocity in body frame. 
 
 * `/airsim_node/VEHICLE_NAME/vel_cmd_world_frame` [airsim_ros_pkgs/VelCmd](https://github.com/microsoft/AirSim/tree/master/ros/src/airsim_ros_pkgs/msg/VelCmd.msg)
 > Commanded velocity in world frame. 
 
 * `/airsim_node/gimbal_angle_euler_cmd` [airsim_ros_pkgs/GimbalAngleEulerCmd](https://github.com/microsoft/AirSim/blob/master/ros/src/airsim_ros_pkgs/msg/GimbalAngleEulerCmd.msg)
 > Gimbal set point in euler angles.
 
 * `/airsim_node/gimbal_angle_quat_cmd` [airsim_ros_pkgs/GimbalAngleQuatCmd](https://github.com/microsoft/AirSim/blob/master/ros/src/airsim_ros_pkgs/msg/GimbalAngleQuatCmd.msg)
 > Gimbal set point in quaternion.
 
### Services
 * `/airsim_node/VEHICLE_NAME/land`
 > Land drone. 
 
 * `/airsim_node/VEHICLE_NAME/takeoff`
 > Takeoff drone. 
 
 * `/airsim_node/reset`
 > Reset all drones. 
 
### Parameters
 * `/airsim_node/update_airsim_control_every_n_sec` [double]
 > Set in: `$(airsim_ros_pkgs)/launch/airsim_node.launch`
 > Default: 0.01 seconds.
 > Timer callback frequency for updating drone odom and state from airsim, and sending in control commands.
 > The current RPClib interface to unreal engine maxes out at 50 Hz.
 > Timer callbacks in ROS run at maximum rate possible, so it's best to not touch this parameter.
 
 * `/airsim_node/update_airsim_img_response_every_n_sec` [double]
 > Set in: `$(airsim_ros_pkgs)/launch/airsim_node.launch`
 > Default: 0.01 seconds.
 > Timer callback frequency for receiving images from all cameras in airsim.
 > The speed will depend on number of images requested and their resolution.
 > Timer callbacks in ROS run at maximum rate possible, so it's best to not touch this parameter.
 
 * `/airsim_node/update_lidar_every_n_sec` [double]


## `/pid_position_node` node

### Publications
 * `/vel_cmd_world_frame` [airsim_ros_pkgs/VelCmd](https://github.com/microsoft/AirSim/tree/master/ros/src/airsim_ros_pkgs/msg/VelCmd.msg)
 > Sends velocity command to `/airsim_node`.
 
### Subcriptions
 * `/airsim_node/home_geo_point` [airsim_ros_pkgs/GPSYaw](https://github.com/microsoft/AirSim/blob/master/ros/src/airsim_ros_pkgs/msg/GPSYaw.msg)
 > Listens to home geo coordinates published by `/airsim_node`.
 
 * `/airsim_node/odom_local_ned` [nav_msgs/Odometry](https://docs.ros.org/api/nav_msgs/html/msg/Odometry.html)
 > Listens to odometry published by `/airsim_node`.
 
### Services
 * `/airsim_node/gps_goal` [srv/SetGPSPosition](https://github.com/microsoft/AirSim/blob/master/ros/src/airsim_ros_pkgs/srv/SetGPSPosition.srv)
 > Target gps position + yaw. In absolute altitude.
 
 * `/airsim_node/gps_goal/override`
 
 * `/airsim_node/local_position_goal` [srv/SetLocalPosition](https://github.com/microsoft/AirSim/blob/master/ros/src/airsim_ros_pkgs/srv/SetLocalPosition.srv)
 > Target local position + yaw in global NED frame.
 
 * `/airsim_node/local_position_goal/override`

### Parameters
 * `/pid_position_node/kd_x` [double]
 > Derivative gain. 
 
 * `/pid_position_node/kd_y` [double]
 > Derivative gain. 
 
 * `/pid_position_node/kd_yaw` [double]
 > Derivative gain. 
 
 * `/pid_position_node/kd_z` [double]
 > Derivative gain. 
 
 * `/pid_position_node/kp_x` [double]
 > Proportional gain. 
 
 * `/pid_position_node/kp_y` [double]
 > Proportional gain. 
 
 * `/pid_position_node/kp_yaw` [double]
 > Proportional gain. 
 
 * `/pid_position_node/kp_z` [double]
 > Proportional gain. 
 
 * `/pid_position_node/reached_thresh_xyz` [double]
 > Threshold euler distance (meters) from current position to setpoint position

 * `/pid_position_node/reached_yaw_degrees` [double]
 > Threshold yaw distance (degrees) from current position to setpoint position

 * `/pid_position_node/update_control_every_n_sec` [double]
 > Default: 0.01 seconds

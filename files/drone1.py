import airsim                                                            # drone1.py

client = airsim.MultirotorClient()                                       # connect to the simulator
client.confirmConnection()
client.enableApiControl(True, vehicle_name="Drone1")                     # enable API control on Drone1
client.armDisarm(True, vehicle_name="Drone1")                            # arm Drone1

client.takeoffAsync(vehicle_name="Drone1").join()                        # let Drone1 take-off
client.moveToPositionAsync(20, 3, -1, 5, vehicle_name="Drone1").join()   # Drone1 moves to (20, 3, 1) at 5m/s and hovers (note the inverted Z axis)
client.hoverAsync(vehicle_name="Drone1").join()                          # .join() let the script wait for asynchronous (i.e. non-blocking) methods

raw = client.simGetImage("bottom_center", airsim.ImageType.Scene, vehicle_name="Drone1")      # take an image of type "Scene" from the "bottom_center" of "Drone1"
f = open("Drone1a.png", "wb")
f.write(raw)                                                             # save the image as a PNG file
f.close()

client.simSetCameraOrientation("bottom_center", airsim.to_quaternion(1.5, 0, 0), vehicle_name="Drone1")      # modify the orientation (in radians) for camera "bottom_center" of "Drone1"

raw = client.simGetImage("bottom_center", airsim.ImageType.Scene, vehicle_name="Drone1")      # take another image of type "Scene" from the "bottom_center" of "Drone1"
f = open("Drone1b.png", "wb")
f.write(raw)                                                             # save the image as a PNG file
f.close()

airsim.wait_key('Press any key to reset')                                # press any key
client.armDisarm(False, vehicle_name="Drone1")                           # disarm Drone1
client.reset()                                                           # reset the simulation
client.enableApiControl(False, vehicle_name="Drone1")                    # disable API control of Drone1
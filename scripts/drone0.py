import airsim                                                            # drone0.py

client = airsim.MultirotorClient()                                       # connect to the simulator
client.confirmConnection()
client.enableApiControl(True, vehicle_name="Drone0")                     # enable API control on Drone0
client.armDisarm(True, vehicle_name="Drone0")                            # arm Drone0

client.takeoffAsync(vehicle_name="Drone0").join()                        # let Drone0 take-off
client.moveToPositionAsync(15, -3, -4, 5, vehicle_name="Drone0").join()  # Drone0 moves to (15, -3, 4) at 5m/s and hovers (note the inverted Z axis)
client.hoverAsync(vehicle_name="Drone0").join()                          # .join() let the script wait for asynchronous (i.e. non-blocking) methods

raw = client.simGetImage("bottom_center", airsim.ImageType.Scene, vehicle_name="Drone0")           # take an image of type "Scene" from the "bottom_center" of "Drone0"
f = open("Drone0a.png", "wb")
f.write(raw)                                                             # save the image as a PNG file
f.close()

raw = client.simGetImage("bottom_center", airsim.ImageType.Segmentation, vehicle_name="Drone0")    # take an image of type "Segmentation" from the "bottom_center" of "Drone0"
f = open("Drone0b.png", "wb")
f.write(raw)                                                             # save the image as a PNG file
f.close()

airsim.wait_key('Press any key to reset')                                # press any key
client.armDisarm(False, vehicle_name="Drone0")                           # disarm Drone0
client.reset()                                                           # reset the simulation
client.enableApiControl(False, vehicle_name="Drone0")                    # disable API control of Drone0
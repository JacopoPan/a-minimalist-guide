import robomaster
from robomaster import robot


if __name__ == '__main__':

    ep_robot = robot.Robot()

    ep_robot.initialize(conn_type='sta')
    # ep_robot.initialize(conn_type='ap')  # When using the S1's Wi-Fi
    # ep_robot.initialize(conn_type='sta', sn="3JKDH2T001ULTD")  # To specify a serial number

    version = ep_robot.get_version()
    print("Robot version: {0}".format(version))

    ep_chassis = ep_robot.chassis

    x_val = 0.5
    y_val = 0.6
    z_val = 90

    ep_chassis.move(x=x_val, y=0, z=0, xy_speed=0.7).wait_for_completed()
    ep_chassis.move(x=-x_val, y=0, z=0, xy_speed=0.7).wait_for_completed()
    ep_chassis.move(x=0, y=-y_val, z=0, xy_speed=0.7).wait_for_completed()
    ep_chassis.move(x=0, y=y_val, z=0, xy_speed=0.7).wait_for_completed()
    ep_chassis.move(x=0, y=0, z=z_val, z_speed=45).wait_for_completed()
    ep_chassis.move(x=0, y=0, z=-z_val, z_speed=45).wait_for_completed()

    ep_robot.close()

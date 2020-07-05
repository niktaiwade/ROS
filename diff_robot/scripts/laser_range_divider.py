#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

vel_pub = rospy.Publisher("/diff_robot/cmd_vel",Twist,queue_size=10)

def clbk_laser(data):
    vel = Twist()
    laser_range = {"E":min(min(data.ranges[0:143]),5),"NE":min(min(data.ranges[144:287]),5),"N":min(min(data.ranges[288:431]),5),"NW":min(min(data.ranges[432:575]),5),"W":min(min(data.ranges[576:720]),5)}

    global vel_pub
    vel.linear.x = 0.1
    vel.angular.z = 0.0
    vel_pub.publish(vel)
    if laser_range["N"] < 1.5:
        if laser_range["NE"]<0.5:
            c = -0.5
        else:
            c = 0.5
        vel.linear.x = 0.0
        vel.angular.z = c
        vel_pub.publish(vel)
    if laser_range["W"] < 0.5:
        vel.linear.x = 0.0
        vel.angular.z = 0.5
        vel_pub.publish(vel)
    if laser_range["E"] < 0.5:
        vel.linear.x = 0.0
        vel.angular.z = -0.5
        vel_pub.publish(vel)
    if laser_range["NE"] < 1.0:
        if laser_range["E"]<0.5:
            b = 0.5
        else:
            b = -0.5
        vel.linear.x = 0.0
        vel.angular.z = b
        vel_pub.publish(vel)
    if laser_range["NW"] < 1.0:
        if laser_range["N"]<0.5:
            n = -0.5
        else:
            n = 0.5
        vel.linear.x = 0.0
        vel.angular.z = n
        vel_pub.publish(vel)

def main():
    rospy.init_node("laser_range_divider")
    rospy.loginfo("NODE Started")

    sub = rospy.Subscriber("/diff_robot/laser_scan",LaserScan, clbk_laser)

    rospy.spin()

if __name__ == '__main__':
    main()

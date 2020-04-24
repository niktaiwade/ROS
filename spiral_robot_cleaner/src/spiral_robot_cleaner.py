#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

vel_msg = Twist()
pose_msg = Pose()

vel_pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size =10)

def spiral(speed):
    sr = 0
    r = rospy.Rate(speed)

    while (pose_msg.x < 9) and (pose_msg.y < 9):
        sr += 0.5
        vel_msg.linear.x = sr
        vel_msg.angular.z = speed
        vel_pub.publish(vel_msg)
        r.sleep()
    vel_msg.linear.x = 0
    vel_msg.angular.y = 0
    vel_pub.publish(vel_msg)

def poseCallback(msg):
    pose_msg.x = msg.x
    pose_msg.y = msg.y
    pose_msg.theta = msg.theta

if __name__ == '__main__':
    rospy.init_node("robot_cleaner_spiral")

    pose_sub = rospy.Subscriber("/turtle1/pose", Pose, poseCallback)

    while not rospy.is_shutdown():
        try:
            speed = float(input("Enter speed: "))
            spiral(speed)
        except rospy.ROSInterruptException as e:
            rospy.logerr("ERROR: " + str(e))

        rospy.spin()

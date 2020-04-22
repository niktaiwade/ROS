"""
Created by: niktaiwade
Description: A python ROS program to draw a polygon using turtlesim based on user input given side
"""

#!/usr/bin/env python

#import necessary modules
import rospy
import math
from geometry_msgs.msg import Twist
from polygon.srv import Polygon


#This Function moves in straight line along the SideLength Provided
def move_line(side_length, vel_pub):
    distance = side_length
    current_distance = 0
    t0 = abs(rospy.Time.now().to_sec())
    vel_msg = Twist()

    while current_distance < distance:
        speed = 1
        vel_msg.linear.x = speed
        t1 = abs(rospy.Time.now().to_sec())
        vel_pub.publish(vel_msg)
        current_distance = (speed) * (t1 - t0)

    vel_msg.linear.x = 0
    vel_pub.publish(vel_msg)

#This function sets the angle between two sides of a polygon
def move_angle(side_number, vel_pub):
    vel_msg = Twist()
    t2 = abs(rospy.Time.now().to_sec())
    turn = (2*(math.pi))/(side_number)
    current_turn = 0
    while current_turn < turn:
        vel_msg.angular.z = 0.4
        t3 = abs(rospy.Time.now().to_sec())
        vel_pub.publish(vel_msg)
        current_turn = (vel_msg.angular.z) * (t3 - t2)

    vel_msg.angular.z = 0
    vel_pub.publish(vel_msg)

def handlerPolygon(req):
    print("!--MOVING ROBOT--!")
    SideLength = float(req.side_length)
    SideNumber = float(req.side_number)
    vel_pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size = 100)
    current_rotation = 0
    while current_rotation < 1:
        move_line(SideLength, vel_pub)
        move_angle(SideNumber, vel_pub)
        current_rotation += 1/(SideNumber)

    return True

def start_server():
    rospy.init_node("turtlesim_polygon", anonymous=True)
    rospy.loginfo("Service Initiated")
    rospy.Service('/polygon_server', Polygon, handlerPolygon)
    rospy.spin()

if __name__ == '__main__':
    try:
        start_server()
    except rospy.ROSInterruptException as e:
        rospy.log_warn("ERROR: " + str(e))

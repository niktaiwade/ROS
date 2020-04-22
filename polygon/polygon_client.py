"""
Created by: niktaiwade
Description: Client for ROS Polygon Server
"""

#!/usr/bin/env python

#import necessary modules
import rospy
from polygon.srv import Polygon

def start_client():
    rospy.wait_for_service('/polygon_server')

    try:
        rospy.loginfo("Client Started")
        service = rospy.ServiceProxy('/polygon_server', Polygon)
        SideLength = float(input("Enter Polygon SideLength: "))
        SideNumber = float(input("Enter number of sides of polygon: "))
        service(SideLength, SideNumber)
    except rospy.ServiceException as e:
        rospy.logwarn("Service Failed: " + str(e))


if __name__ == '__main__':
    try:
        start_client()
    except rospy.ROSInterruptException as e:
        rospy.log_warn("ERROR: " + str(e))

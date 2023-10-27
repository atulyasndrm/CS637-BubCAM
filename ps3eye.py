#!/usr/bin/env python3
import rospy
import cv2 as cv
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

def main():
    rospy.init_node('ps3eyecam')
    rospy.loginfo('Publishing PS3EYE camera')
    rate = rospy.Rate(10)
    pub = rospy.Publisher('/ps3eyecam', Image, queue_size=10)

    cap = cv.VideoCapture(2)
    bridge = CvBridge()

    while not rospy.is_shutdown():
        ret,frame = cap.read()
        if ret == True:
            rospy.loginfo_once('publishing video')
            pub.publish(bridge.cv2_to_imgmsg(frame))
        rate.sleep()

if __name__ == '__main__':
    main()




































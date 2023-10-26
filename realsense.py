#!/usr/bin/env python3

import rospy
import pyrealsense2 as rs
import cv2 as cv
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main():
    rospy.init_node('realsense_node')
    rospy.loginfo('realsense_launch')
    bridge = CvBridge()
    rate = rospy.Rate(10)

    pub = rospy.Publisher('/realsense_image', Image, queue_size = 10)

    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    config.enable_stream(rs.stream.color, 640, 480, rs.format.rgb8, 30)
    pipe=pipeline.start(config)

    profile = pipeline.get_active_profile()
    depth_profile = rs.video_stream_profile(profile.get_stream(rs.stream.depth))
    depth_intrinsics = depth_profile.get_intrinsics()

    while not rospy.is_shutdown():
        frame = pipeline.wait_for_frames()
        color = frame.get_color_frame()
        depth = frame.get_depth_frame()
        color_data = np.asanyarray(color.get_data())
        if not color:
            continue
        image = cv.cvtColor(color_data, cv.COLOR_BGR2RGB)
        img_msg = bridge.cv2_to_imgmsg(image)
        pub.publish(img_msg)
        rate.sleep()

if __name__ == '__main__':
    main()

































































































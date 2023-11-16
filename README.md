# CS637-BubCAM
Project for CS637

realsense.py -- Init_node for realsense camera. Clone inside your /workspace/package folder. Needs pyrealsense2(https://github.com/IntelRealSense/librealsense) setup, and CvBridge. 


ps3eye.py --publishes videocapture from ps3eye, cannot control the camera params. could not setup ps3eyepy(https://github.com/bensondaled/pseyepy) package for this, probably libusb issue this time. Someone please try doing this once.

The PSPNet implementation used was the original Pytorch implementation cited below {https://github.com/hszhao/PSPNet}[https://github.com/hszhao/PSPNet]. It was pretrained.
Datasets contains the datasets used for training the model in order to segment out the empty area of the coke bottle.

A few dataset images are added in the `dataset` folder.

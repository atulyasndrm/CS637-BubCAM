import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


vidcap = cv.VideoCapture(0)
keyframes = []

while(True):
    ret, image = vidcap.read()
    if(len(keyframes) == 0):
        keyframes.append(image)
        
        print("Hi")
    else:
        image1 = keyframes[len(keyframes)-1]
        image2 = image

        h1,w1 = image1.shape[0],image1.shape[1]
        h2,w2 = image2.shape[0],image2.shape[1]

        minh = min(h1,h2)
        minw = min(w1,w2)

        image1 = image1[0:minh,0:minw]
        image2 = image2[0:minh,0:minw]


        sub = cv.subtract(image1,image2)
        grayed = cv.cvtColor(sub,cv.COLOR_BGR2GRAY)

        ret,thresh = cv.threshold(grayed,80,255,cv.THRESH_BINARY)
        white = np.sum(thresh == 255 )
        black = np.sum(thresh == 0)
        per_change = (white/(white+black))

        if (per_change>0.2):
            keyframes.append(image)

        cv.imshow('image',thresh)

        print(grayed.shape)

        # To close the window 
        cv.waitKey(0) 
        cv.destroyAllWindows() 
        # plt.plot()
    

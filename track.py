# source 1: https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
# source 2: https://stackoverflow.com/questions/63923800/drawing-bounding-rectangles-around-multiple-objects-in-binary-image-in-python
# source 3: https://stackoverflow.com/questions/44588279/find-and-draw-the-largest-contour-in-opencv-on-a-specific-color-python

import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # RGB is the same as original frame
    rgb = frame

    # define range of green color in HSV
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([90, 255, 255])
    
    # Threshold the HSV image to get only blue colors
    thresh_hsv = cv.inRange(hsv, lower_green, upper_green)

    lower_green_rgb = np.array([80, 88, 4])
    upper_green_rgb = np.array([128, 255, 0])
    
    thresh_rgb= cv.inRange(rgb, lower_green_rgb, upper_green_rgb)

    contours = cv.findContours(thresh_hsv, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    

    contours_rgb = cv.findContours(thresh_rgb, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours_rgb = contours_rgb[0] if len(contours_rgb) == 2 else contours_rgb[1]
    

    res_hsv = frame.copy()
    res_rgb = frame.copy()
    if contours:
      c = max(contours, key = cv.contourArea)
      x,y,w,h = cv.boundingRect(c)
      cv.rectangle(res_hsv, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
    if contours_rgb:
      c = max(contours_rgb, key = cv.contourArea)
      x,y,w,h = cv.boundingRect(c)
      cv.rectangle(res_rgb, (x, y), (x+w, y+h), (0, 0, 255), 2)
    # for cntr in contours:
    #   x,y,w,h = cv.boundingRect(cntr)
      
    #   # print("x,y,w,h:",x,y,w,h)
    # # Bitwise-AND mask and original image
    # for cntr in contours_rgb:
    #   x,y,w,h = cv.boundingRect(cntr)
    #   cv.rectangle(res_rgb, (x, y), (x+w, y+h), (0, 0, 255), 2)


    cv.imshow('frame',frame)
    #cv.imshow('mask',mask)
    cv.imshow('res_hsv',res_hsv)
    #cv.imshow('res_rgb', res_rgb)
    #cv.imshow('res_rgb',res_rgb)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()

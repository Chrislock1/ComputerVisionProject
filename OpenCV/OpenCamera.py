#This code requires Python 3.5, as well as Tensorflow and OpenCv2 suitable to that.

import tensorflow as tf
import cv2 as cv
import os

#Define function to release all optained objects
def release_cameras():
    cap.release()
    cv.destroyAllWindows()
    
cap = cv.VideoCapture(0)                                                            #Create VideoCapture object from capturing device '0'

cap.set(3,640)                                                                      #Set width of picture
cap.set(4,480)                                                                      #Set heigth of picure
cap.set(6, 30)                                                                      #Set FPS of picture

it = 1                                                                              #Create iterator for labeling pictures

while True:
    ret, frame = cap.read()                                                         #Readig VidCap-object's information
    
    #Closing loop if camera is busy
    if not ret:
        print('Return value: ', ret)
        release_cameras()
        break
    
    
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)                                     #Cloning picture to grayscale
    
    #Displaying picture
    cv.imshow('Gray',gray)
    cv.imshow('Frame',frame)
    
    #Waits in '1' ms for key input value
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        #Breaks loop if 'Esc' is pressed
        break
        
    if k == 83 or k == 115:
        #Store picture with an 's' or 'S' input from keyboard
        cv.imwrite('Pictures\Pic' + str(it).zfill(3) + '.jpg', frame)
        it = it + 1
        

release_cameras()

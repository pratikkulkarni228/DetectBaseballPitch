'''
# coding: utf-8
@author: Pratik Kulkarni
A program which takes a video as an input and returns the frame number of 
the frame where a ball is released by the baseball pitcher

E-mail: pratikkulkarni228@gmail.com
'''

import cv2
video_input ='data/test3.mp4' #Path to video

def return_frame_num(video_input):
    vidstream = cv2.VideoCapture(video_input)
    frame_counter=0
    while True:
        success,frame = vidstream.read()

        if success==False:
            break
        frame_counter=frame_counter+1

        image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#Color channels not needed
        image = cv2.resize(frame,(0,0),fx=0.20,fy=0.20)#Faster processing       
        image = image[100:,100:] #Cropping the frame to only work with pitcher's area
        
        img_blur = cv2.GaussianBlur(image,(13,13),0) #to denoise

        edged = cv2.Canny(img_blur, 50, 80) #edge detector necessary to find contours
        edged = cv2.dilate(edged, None, iterations=3) #to fuse multiple contours found later
        edged = cv2.erode(edged, None, iterations=1)  #''

        newimg=edged.copy()#Made a copy to be processes on
        
        #Finds a list of contours and saves them per (x,y) tuple as a list in conts
        (_,conts, _) = cv2.findContours(newimg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        #Sort the contours in ascending order 
        contours = sorted(conts, key = cv2.contourArea, reverse = False)[:3]
        
        #The ball is observed to have an area(area of contour) of around 90 to 100
        #The list would show this number(in range 90,100) only when a ball is detected in a fram
        
        if 90<(cv2.contourArea(contours[0]) or cv2.contourArea(contours[1]))<100:
            return frame_counter-3
        


# In[105]:


print('Frame Num is',return_frame_num(video_input))


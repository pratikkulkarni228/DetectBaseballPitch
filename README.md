# DetectBaseballPitch
#### An algorithm that can take any pitch from the camera and detect the frame where the ball was released from the pitcher’s hand.

This mini-project aims at recieving a video input from the videos of Matt Harvey pitching a baseball. Using Python and OpenCV techniques the user can determine in what frame Matt Harvey pitched the ball.


### Requirements:
>##### Python 2.x , 3.x
>##### OpenCV 

### Techniques used:
>1. Video breakdown into frames
>2. Single image channel and cropping to reduce processing time of [4K images](https://en.wikipedia.org/wiki/4K_resolution)
>3. [Gaussian Blur](https://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html) to denoise
>4. [Canny edge](https://docs.opencv.org/3.1.0/da/d22/tutorial_py_canny.html) detector and alongwith [dilation and erosion](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html) techniques
>5. Finding [contours](https://docs.opencv.org/3.4.2/d4/d73/tutorial_py_contours_begin.html) in each frame and the isolating the ball from pitcher after it is released from his hand
>6. Sorting the contours found and returning the frame with a contour area <100 (The obserevd area of the ball/circle)

![alt text](https://github.com/pratikkulkarni228/DetectBaseballPitch/blob/master/img/frame1.png)

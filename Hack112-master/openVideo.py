import numpy
import cv2
"""
#from Vasu Agrawal
#https://github.com/VasuAgrawal/112-opencv-tutorial/blob/master/openingVideo.py
window_name = "Webcam!"
cam_index = 0 # Default camera is at index 0.
# Create a window to display to
cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
cap = cv2.VideoCapture(cam_index) # Video capture object
cap.open(cam_index) # Enable the camera
# Loop indefinitely
while True:
    # Read from the camera, getting the image and some return value
    ret, frame = cap.read()
    # If frame is valid, display the image to our window
    if frame is not None:
        cv2.imshow(window_name, frame)
    # wait for some key with a small timeout.
    # We need the & 0xFF on 64bit systems to strip just the last 8 bits.
    k = cv2.waitKey(1) & 0xFF
    # If we hit the escape key, destroy all windows and release the capture
    # object. If we don't release cleanly, we might still have a lock and
    # no one else could use it, which is bad.
    if k == 27: # Escape key
        cv2.destroyAllWindows()
        cap.release()
        break"""
      
"""
#from Vasu Agrawal
#https://github.com/VasuAgrawal/112-opencv-tutorial/blob/master/openingImagesResize.py
window_name = "Images"
desired_size = 500.0 # we want the max dimension to be 500

# Importantly, images are stored as BGR
# Use the following function to read images.
image = cv2.imread("spaceship.jpg")
# Error checking to make sure that our image actually loaded properly
# Might fail if we have an invalid file name (or otherwise)
if image is not None:

    # Get the size of the image, which is a numpy array
    size = image.shape
    print(size) # Just so that we see what format it's in
    # Notice that it's a 1000 x 1000 x 3 image, where the last
    # dimension is the 3 values, BGR, per pixel.
    
    # We now want to resize the image to fit in our window, while
    # maintaining an aspect ratio
    fx = desired_size / size[0]
    fy = desired_size / size[1]
    scale_factor = min(fx, fy)

    # Get the resized image. The (0,0) parameter is desired size, which we're
    # setting to zero to let OpenCV calculate it from the scale factors instead
    resized = cv2.resize(image, (0,0), fx = scale_factor, fy = scale_factor)

    # Display our loaded image in a window with window_name
    cv2.imshow(window_name, resized)
    # Wait for any key to be pressed
    cv2.waitKey(0)

# Clean up before we exit!
cv2.destroyAllWindows()"""

"""
import cv2
import numpy as np

# This is going to be EXTREMELY slow, since we're using python for loops
def manual_threshold(image):
    # Define some constants
    WHITE = 255
    BLACK = 0
    THRESH = 127

    # Convert our input image to grayscale so that it's easy to threshold
    grey = 
    
    cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    

    # Create a new array of all zeros to store our thresholded image in
    # It will be the same size as our grey image
    thresholded = np.zeros(grey.shape, np.uint8)
    
    # Iterate over the grey image, and store results in thresholded
    for i in xrange(grey.shape[0]):
        for j in xrange(grey.shape[1]):
            # If we're over a certain target value, then saturate to white
            # otherwise, we're under the bar, dilute to black
            thresholded[i][j] = WHITE if grey[i][j] > THRESH else BLACK

    # Return our handiwork
    return thresholded

# We've finally put our code in a function instead!
def main():

    window_name = "Webcam!"

    cam_index = 0
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    cap = cv2.VideoCapture(cam_index)
    cap.open(cam_index)

    while True:

        ret, frame = cap.read()

        if frame is not None:
            # Instead of showing the original image, show the thresholded one
            cv2.imshow(window_name, manual_threshold(frame))
        
        k = cv2.waitKey(1) & 0xFF
        if k == 27: # Escape key
            cv2.destroyAllWindows()
            cap.release()
            break

if __name__ == "__main__":
    main()"""
"""    
import cv2
import numpy as np

window_name = "Webcam!"
cam_index = 0 #my computer's camera is index 1, usually it's 0
cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
cap = cv2.VideoCapture(cam_index)
cap.open(cam_index)

findVertEdges = False
findHorzEdges = False
findAllEdges = False
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.blur(gray, (3,3))
    if frame is not None:
        if findVertEdges:
            frame = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
        if findHorzEdges:
            frame = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
        if findAllEdges:
            frame = cv2.Canny(frame, 100, 200) 
        cv2.imshow(window_name, frame)
    k = cv2.waitKey(10) & 0xFF
    if k == 27: #ESC key quits the program
        cv2.destroyAllWindows()
        cap.release()
        break
    elif k == ord('v'):
        findVertEdges = not findVertEdges
    elif k == ord('h'):
        findHorzEdges = not findHorzEdges
    elif k == ord('a'):
        findAllEdges = not findAllEdges"""
        
# webcam functionality adapted largely from http://cbarker.net/opencv/
# slider setup from: https://botforge.wordpress.com/2016/07/02/basic-color-tracker-using-opencv-python/
# and: http://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html

import cv2
import numpy as np

#dummy callback function for cv2.createTrackbar()
def nothing(temp):
    return

def sliderCam():

    rgbMax = 255
    rgbMin = 0

    sliderWinName = 'Sliders'
    cv2.namedWindow(sliderWinName)

    cam_index = 0 # Default camera is at index 0.
    cap = cv2.VideoCapture(cam_index) # Video capture object

    sliders = ['R_MAX', 'G_MAX', 'B_MAX', 'R_MIN', 'G_MIN', 'B_MIN']

    #initialize sliders
    for slider in sliders:
        cv2.createTrackbar(slider, sliderWinName, rgbMin, rgbMax, nothing)
    for slider in sliders[0:3]:
        cv2.setTrackbarPos(slider, sliderWinName, rgbMax)

    cap.open(cam_index) # Enable the camera
    while True:
        ret, frame = cap.read() # gets one frame from the webcam


        #collect threshold values from sliders (set by user)
        thresholds = []
        for slider in sliders:
            thresholds.append(cv2.getTrackbarPos(slider, sliderWinName))

        upperBound = np.array(thresholds[0:3])
        lowerBound = np.array(thresholds[3:6])

        #read more about hsv here: http://docs.opencv.org/3.2.0/df/d9d/tutorial_py_colorspaces.html
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        threshold = cv2.inRange(hsv, lowerBound, upperBound)
        

        #displays all windows
        #comment out lines as you need if you feel too many windows, only threshold window necessary
        cv2.imshow('Input', frame)
        cv2.imshow('HSV', hsv)
        cv2.imshow('Threshold', threshold)

        #closes all windows and exits when escape key is pressed
        k = cv2.waitKey(10) & 0xFF
        if k == 27: # code for escape key
            cv2.destroyAllWindows()
            cap.release()
            break

sliderCam()

from PIL import ImageGrab
import cv2
import numpy as np
from tkinter import *

def record_screen():
    #Obtain image dimensions
    #Screen capture
    image = ImageGrab.grab()
    #Convert object to numpy array
    img_to_np_arr = np.array(image)
    #Extract and print shape of array
    shape = img_to_np_arr.shape
    print(shape)

    screen_cap_writer = cv2.VideoWriter('screen_recorded.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 50, (shape[1], shape[0]))

    
record_screen()

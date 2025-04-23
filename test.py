import tkinter
import cv2 as cv
img = cv.imread("/Users/lienl/Pictures/20250205_125959.jpg")

cv.imshow("Display window", img)
k = cv.waitKey(0) # Wait for a keystroke in the window
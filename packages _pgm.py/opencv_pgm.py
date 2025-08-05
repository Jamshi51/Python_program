import cv2 as cv
img=cv.imread("218623.jpg") # Read the image
cv.imshow("display window",img)   # Display the image in a window
k=-cv.waitKey(6000)   # Wait for 6000 milliseconds (6 seconds)

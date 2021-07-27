import cv2#main file of openCV
import easygui#a gui module to take the image as input in the program

image = cv2.imread(easygui.fileopenbox())#Imagw file chooser saving the file in image variable

#logic to convert the normal image to sketch
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted_image = 255 - gray_image
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

#displays the image
cv2.imshow("pencil sketch", pencil_sketch)

#waits for any key pressed via keyboard k
k = cv2.waitKey(0)

#if the escape key is pressed program terminates
if(k == 27):
    cv2.destroyAllWindows()

import cv2#main file of openCV

cap =cv2.VideoCapture(0)#capturing the video from the camera

while(True):#The loop is required since only one pic/frame is captured at a time
        ret, frame = cap.read()#reading dthe data from the camera
        
        cv2.imshow('frame', frame)#showing the GUI of video being captured

        if cv2.waitKey(1) & 0xFF == ord('q'):#terminate the program if q is pressed and the single frame in 1seconf time is over
            break

cap.release()#unloads the memmory
cv2.destroyAllWindows()#terminate the capturing frames
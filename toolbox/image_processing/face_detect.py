""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame. Comment out to get faces.
    # ret, frame = cap.read()

    # # Display the resulting frame
    # cv2.imshow('frame',frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

	# Identify faces
	face_cascade = cv2.CascadeClassifier('/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml')
	kernel = np.ones((21,21),'uint8')

	ret, frame = cap.read()
	faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
	# print"getting faces"
	for (x,y,w,h) in faces:
	    frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
	    # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))
	    cv2.circle(frame, (x+(w/3),y+(h/3)), 20, (255,100,0), -1)
	    cv2.circle(frame, (x+2*(w/3),y+(h/3)), 20, (255,100,0), -1)
	    cv2.ellipse(frame, (x+w/2,y+2*(h/3)), (w/3,h/5), 0, 0, 180, (255,100,0), 10)

	# Display the resulting frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

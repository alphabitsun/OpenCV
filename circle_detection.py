'''
    Circle detection
    Create Date:2021/7/15     
    By. Alpha_BIT
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("detect.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.subplot(121),plt.imshow(gray,'gray')
plt.xticks([]),plt.yticks([])

circles1 = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 600,param1=100, param2=45,minRadius=140,maxRadius=200)
'''
    param2: The smaller the value, the more circles are detected.
    minRadius: Minimum radius
    maxRadius: Maximum radius
'''
circles = circles1[0,:,:]
circles = np.uint16(np.around(circles))
font = cv2.FONT_HERSHEY_SIMPLEX

for i in circles[:]:
    cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),5) # center of a circle
    cv2.circle(img,(i[0],i[1]),2,(255,0,255),10) # circle
    cv2.rectangle(img,(i[0]-i[2],i[1]+i[2]),(i[0]+i[2],i[1]-i[2]),(255,255,0),5)
    cv2.putText(img, str(2* i[2]), (i[0]-i[2],i[1]-200), font, 4, (0, 0, 0), 5) # diameter of the circle

print("Center Coordinates",i[0],i[1])
cv2.imwrite("result.jpg", img)
plt.subplot(122),plt.imshow(img)
plt.xticks([]),plt.yticks([])
plt.show()

import numpy as np
import cv2
import cv
from skimage.feature import blob_dog, blob_log, blob_doh

#def mouse_callback(event,x,y,flags,param):
          #if event ==cv2.EVENT_LBUTTONDOWN:
			  #print "xy"
			  #print x, y
			  #imgo=cv2.imread("vettikkad.jpg")
			  #img=imgo[500:1500,500:1500,0:3]
			  #print "val"
			  #print img[y,x,0:3]
             
             
             
             
             
			  
			 



#boundaries = [
#([255,0,0], [230, 20, 20]),
#([0,255,0] ,[20,230,20]),
#([25, 146, 190], [62, 174, 250]),
#]
boundaries = [
([45,150,45], [55,160,55]),
([0,0,250], [0,0,255]),
([0,250,250], [5,255,255]),
([170,90,250], [199,110,255])
]
imgo=cv2.imread("vettikkad.jpg")
img=imgo[500:1500,500:1500,0:3]



#cv2.namedWindow('image',cv2.WINDOW_NORMAL) # Can be resized
#cv2.resizeWindow('image', 1000,1000) #Reasonable size window
#cv2.setMouseCallback('image',mouse_callback) #Mouse callback      
#while True:
	
	#cv2.imshow('image',img)
	#k = cv2.waitKey(4) & 0xFF
       


       
       



cv2.imshow("img",img)

r,g,b = cv2.split(img)

cv2.imshow("red",r)
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True

params.minArea = 20

params.filterByConvexity = False
ver = (cv2.__version__).split('.')

if int(ver[0]) < 3 :

	detector = cv2.SimpleBlobDetector(params)

else : 

	detector = cv2.SimpleBlobDetector_create(params)
print detector
	
for (lower, upper) in boundaries:
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	mask = cv2.inRange(img, lower, upper)
	print mask.shape
	
	
	print max(mask.flatten())
	output = cv2.bitwise_and(img, img, mask = mask)
	cv2.imshow("mask",output)
	keypoints = detector.detect(mask)
	mask=255-mask
	mask = 255 - cv2.erode(mask, np.ones((3,3)), iterations=2)
	print keypoints
	im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	cv2.imshow("Keypoints", im_with_keypoints)
	cv2.waitKey()
	# create NumPy arrays from the boundaries
	
#ret,rt = cv2.threshold(r,250,255,cv2.THRESH_BINARY_INV)
#ret,gt = cv2.threshold(g,250,255,cv2.THRESH_BINARY_INV)

#cv2.imshow("r",rt)

#cv2.imshow("g",gt)


cv2.waitKey()

import cv2
import numpy as np

WINDOW_WIDTH    = 640
WINDOW_HEIGHT   = 480

cap = cv2.VideoCapture(0)
cap.set(3,WINDOW_WIDTH)     #width=640
cap.set(4,WINDOW_HEIGHT)    #height=480

# img = None

# if cap.isOpened():
#     _,img = cap.read()
#     cap.release() #releasing camera immediately after capturing picture
#     if _ and img is not None:
#         cv2.imwrite('img.jpg', img)

# font                   = cv2.FONT_HERSHEY_SIMPLEX
# topRightCorner         = (400,25)
# fontScale              = 1
# fontColor              = (153, 0, 153)
# lineType               = 2

# cv2.putText(img,'Omar Cuenca', 
#     topRightCorner, 
#     font, 
#     fontScale,
#     fontColor,
#     lineType)

# topRightCorner         = (450,60)

# cv2.putText(img,'A01378844', 
#     topRightCorner, 
#     font, 
#     fontScale,
#     fontColor,
#     lineType)

# # #Display the image
# # cv2.imshow("img",img)

# #Save image
# cv2.imwrite("out.jpg", img)

mouseX = 0
mouseY = 0
flag = True

def detectClick(event,x,y,flags,param):
    global mouseX,mouseY,flag
    if event == cv2.EVENT_LBUTTONDOWN:
        mouseX,mouseY = x,y
        flag = False

cv2.namedWindow('video_feed')
cv2.setMouseCallback('video_feed',detectClick)

frame = None

while(cap.isOpened()):
    ret, frame = cap.read()
    if frame is None:
        break
    # Display the resulting frame
    cv2.imshow('video_feed',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if not flag:
        break

targetColor = frame[mouseY,mouseX]

cap.release()

cv2.imwrite("videoProcessedWhole.jpg", frame)

imgCopy = np.array(frame)

# target_pixels = np.all(imgCopy[:,:,:3] == targetColor, axis=-1)
# imgCopy[np.logical_not(target_pixels)] = [0,0,0]
# cv2.imwrite("videoProcessedFiltered.jpg", imgCopy)

RANGE_DEGREE_FREEDOM = 30

lower = np.array([targetColor[0] - RANGE_DEGREE_FREEDOM,targetColor[1] - RANGE_DEGREE_FREEDOM,targetColor[2] - RANGE_DEGREE_FREEDOM])  #-- Lower range --
upper = np.array([targetColor[0] + RANGE_DEGREE_FREEDOM,targetColor[1] + RANGE_DEGREE_FREEDOM,targetColor[2] + RANGE_DEGREE_FREEDOM])  #-- Upper range --
mask = cv2.inRange(imgCopy, lower, upper)
res = cv2.bitwise_and(imgCopy, imgCopy, mask= mask) 

cv2.imwrite("videoProcessedFiltered.jpg", res)

cv2.destroyAllWindows()
import cv2
import numpy as np

WINDOW_WIDTH    = 640
WINDOW_HEIGHT   = 480

cap = cv2.VideoCapture(0)
cap.set(3,WINDOW_WIDTH)     #width=640
cap.set(4,WINDOW_HEIGHT)    #height=480

img = None

if cap.isOpened():
    _,img = cap.read()
    cap.release() #releasing camera immediately after capturing picture
    if _ and img is not None:
        cv2.imwrite('img.jpg', img)

font                   = cv2.FONT_HERSHEY_SIMPLEX
topRightCorner         = (400,25)
fontScale              = 1
fontColor              = (153, 0, 153)
lineType               = 2

cv2.putText(img,'Omar Cuenca', 
    topRightCorner, 
    font, 
    fontScale,
    fontColor,
    lineType)

topRightCorner         = (450,60)

cv2.putText(img,'A01378844', 
    topRightCorner, 
    font, 
    fontScale,
    fontColor,
    lineType)

#Save image
cv2.imwrite("out.jpg", img)

def hconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                      for im in im_list]
    return cv2.hconcat(im_list_resize)

# Write the Photo with the meme attached horizontally
cv2.imwrite("memeOut.png",hconcat_resize_min([img,cv2.imread("meme.png")]))

cap = cv2.VideoCapture(0)
cap.set(3,WINDOW_WIDTH)     #width=640
cap.set(4,WINDOW_HEIGHT)    #height=480

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

cap.release()

cv2.imwrite("videoProcessedWhole.jpg", frame)

targetColor = np.uint8([[frame[mouseY,mouseX]]])
targetColor = cv2.cvtColor(targetColor,cv2.COLOR_BGR2HSV)[0][0][0]

DEGREE_OF_FREEDOM = 5

# define range of blue color in HSV
lower = np.array([targetColor - DEGREE_OF_FREEDOM  ,30 ,30])
upper = np.array([targetColor + DEGREE_OF_FREEDOM  ,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(cv2.cvtColor(frame,cv2.COLOR_BGR2HSV), lower, upper)

cv2.imwrite("videoProcessedFiltered.jpg", cv2.bitwise_and(frame,frame, mask= mask))

cv2.destroyAllWindows()
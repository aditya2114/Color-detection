import cv2
import numpy

vid = cv2.VideoCapture(0)
vid.set(3, 300)
vid.set(4, 300)
vid.set(10, 200)

def none(a):
    pass

cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 400, 300)
cv2.createTrackbar("hue-min", "Trackbar", 0, 179, none)
cv2.createTrackbar("hue-max", "Trackbar", 179, 179, none)
cv2.createTrackbar("sat-min", "Trackbar", 0, 179, none)
cv2.createTrackbar("sat-max", "Trackbar", 255, 255, none)
cv2.createTrackbar("val-min", "Trackbar", 0, 179, none)
cv2.createTrackbar("val-max", "Trackbar", 255, 255, none)

while True: 
    s, img = vid.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("hue-min", "Trackbar")
    h_max = cv2.getTrackbarPos("hue-max", "Trackbar")
    s_min = cv2.getTrackbarPos("sat-min", "Trackbar")
    s_max = cv2.getTrackbarPos("sat-max", "Trackbar")
    v_min = cv2.getTrackbarPos("val-min", "Trackbar")
    v_max = cv2.getTrackbarPos("val-max", "Trackbar")

    lower = numpy.array([h_min, s_min, v_min])
    upper = numpy.array([h_max, s_max, v_max])

    print(h_min, h_max, s_min, s_max, v_min, v_max)

    mask = cv2.inRange(imgHsv, lower, upper)
    imgRes = cv2.bitwise_and(img, img, mask=mask)

    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        print(area)
        if(area > 400): 
            x, y, w, h = cv2.boundingRect(contour) 
            imageFrame = cv2.rectangle(imgRes, (x, y),(x + w, y + h),(0, 0, 255), 2) 
                                            
                                           
    cv2.imshow("resultimg",imgRes)
    if cv2.waitKey(1) and '0xFF' == 'q':
        break


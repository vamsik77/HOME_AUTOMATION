import cv2
import pyttsx3
from time import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def say(audio):
    engine.say(audio)
    engine.runAndWait()


image = cv2.imread("shape.png")


gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

_, thresh_image = cv2.threshold(gray_image,220,255,cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh_image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


for i,contour in enumerate(contours):
    if i == 0:
        continue

    epsilon = 0.01*cv2.arcLength(contour,True)
    approx = cv2.approxPolyDP(contour,epsilon,True)

    cv2.drawContours(image,contour,0,(0,0,255),4)

    x,y,w,h = cv2.boundingRect(approx)

    x_mid = int(x+w/3)
    y_mid = int(y+h/1.5)

    coords = (x_mid,y_mid)
    colour = (0,0,255)
    font = cv2.FONT_HERSHEY_DUPLEX

    print(len(approx))
    cv2.imshow("window",image)

    if len(approx) == 11:
        cv2.putText(image,"HEART",coords,font,0.5,colour,1) 
    # elif len(approx) == 10:
    #     cv2.putText(image,"Heart",coords,font,0.5,colour,1)
    # elif len(approx) == 17:
    #     cv2.putText(image,"LIKEuu",coords,font,0.5,colour,1)
    # elif len(approx) == 12:
    #     cv2.putText(image,"Heart",coords,font,0.5,colour,1)
    elif len(approx) == 3:
        cv2.putText(image,"TRIANGLE",coords,font,0.5,colour,1)
        say("TRIANGLE")
        sleep(1)
    elif len(approx) == 4:
        cv2.putText(image,"RECTANGLE",coords,font,0.5,colour,1)
        say("RECTANGLE")
        sleep(1)
    elif len(approx) == 5:
        cv2.putText(image,"PENTAGON",coords,font,0.5,colour,1)
        say("PENTAGON")
        sleep(1)
    elif len(approx) == 6:
        cv2.putText(image,"HEXAGON",coords,font,0.5,colour,1)
        say("HEXAGON")
        sleep(1)
    else:
        cv2.putText(image,"CIRCLE",coords,font,0.5,colour,1)
        say("CIRCLE")
        sleep(1)

cv2.waitKey(0)



import cv2 as cv
import numpy as np

#직선 그리기
img = np.full((400,400,3), 255, np.uint8)
cv.line(img, (50, 50), (200,50), (0,0,255), 3, cv.LINE_AA) # 색상이랑 두께네, 마지막은 안티얼라이어싱
cv.imshow('img', img)

cap = cv.VideoCapture('test.avi')

if not cap.isOpened():
    print('Could not open video file')
    exit()

w = round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv.CAP_PROP_FPS)

fourcc = cv.VideoWriter_fourcc(*'DIVX')
delay = round(1000 / fps)

outputVideo = cv.VideoWriter('output.avi', fourcc, delay, (w, h))
if not outputVideo.isOpened():
    print('Could not open video file')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    inversed = ~frame
    outputVideo.write(inversed)

    cv.imshow('frame', frame)
    cv.imshow('inversed', inversed)

    if cv.waitKey(delay) == 27:
        break



cv.destroyAllWindows()


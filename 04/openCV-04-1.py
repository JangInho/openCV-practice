import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

print('Frame width:', int(cap.get(cv.CAP_PROP_FRAME_WIDTH))) # cap.get()이 영상 정보를 다 내려줌
print('Frame height:', int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))



import cv2 as cv

cap = cv.VideoCapture('test.avi')
if not cap.isOpened():
    print('Could not open video file')
    exit()

print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv.CAP_PROP_FRAME_COUNT))

fps = cap.get(cv.CAP_PROP_FPS)
print('FPS: ', fps)
delay = round( 1000 / fps)
print('delay: ', delay)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    inversed = ~frame

    cv.imshow('frame', frame)
    cv.imshow('inversed', inversed)

    if cv.waitKey(delay) == 27:
        break

cv.destroyAllWindows()
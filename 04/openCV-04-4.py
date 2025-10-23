import numpy as np
import cv2 as cv

img = np.full((200,640, 3), 255, np.uint8)

print(img.shape)

text  = "Hello, openCV"
fontFace = cv.FONT_HERSHEY_SIMPLEX
fontScale = 1
thickness = 2

sizeText, _ = cv.getTextSize(text, fontFace, fontScale, thickness)

org = ((img.shape[1] - sizeText[0]) // 2, (img.shape[0] - sizeText[1]) // 2)
cv.putText(img, text, org, fontFace, fontScale, thickness, cv.LINE_AA)
cv.rectangle(img, org, org, color=(255, 0, 0), thickness=2)
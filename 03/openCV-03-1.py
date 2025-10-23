
import cv2 as cv

# 두번째 인자 디폴트는  컬러영상
img = cv.imread('lenna.png', cv.IMREAD_REDUCED_COLOR_2)

if img is None:
    print('no image')
    exit()

# 화면에 띄우기 -> 경로 과제 제출할 때 중요함 하드코딩 되었으면 이미지 잘못불러올수있으니까
cv.imshow('lenna', img)
cv.waitKey()
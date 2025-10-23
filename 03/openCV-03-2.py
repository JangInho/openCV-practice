import numpy as np
import cv2 as cv

def func1():
    img1 = cv.imread('lenna.png')

    if img1 is None:
        print('no image')
        return

    print('type(img1):', type(img1))
    print('img1.shape:', img1.shape)

    # 여기서 shape이 2라는데 grayscale은 (500,500) 나오고 truecolor는 ((500,500) ,2)와 같이차원도 나옴
    if len(img1.shape) == 2:
        print('img1 is grayscale image', img1.shape)
    elif len(img1.shape) == 3:
        print('img1 is a truecolor image', img1.shape)

    cv.imshow('lenna', img1)
    cv.waitKey()
    cv.destroyAllWindows()

# func1()

def func2():
    img1 = np.empty((480, 640), np.uint8) # grayscale image
    img2 = np.zeros((480, 640, 3), np.uint8) # color scale image
    img3 = np.ones((480, 640), np.uint32)  # 1's matrix
    img4 = np.full((480, 640), 0, np.uint8) # fill 0.0

    mat1 = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]).astype(np.uint8)


    # 0행 1열
    mat1[0,1] = 100
    # :는 전체를 말하나봄
    mat1[2,:] = 200
    print(mat1)
    print(img2)

# func2()


# 얕은 복사 예제
nums = np.array([1, 4, 2, 5, 3])
ref = nums[1:4]
cpy = nums[1:4].copy() # 이건 깊은 복사인거같은데
# print(ref)
# print(cpy)

def func3():
    img1 = cv.imread('lenna.png')
    img2 = img1
    img3 = img1.copy()

    img1[:, :] = (0, 255, 255) # yellow 싹다 옐로우로 채워버려라 이건가
    print(img1)

    cv.imshow('lenna1', img1)
    cv.imshow('lenna2', img2)
    cv.imshow('lenna3', img3)
    cv.waitKey()
    cv.destroyAllWindows()

# func3()


def func4():
    img1 = cv.imread('lenna.png', cv.IMREAD_GRAYSCALE)
    img2 = img1[200:400, 200:400]
    img3 = img1[200:400, 200:400].copy()

    img2 += 20 # 1,2 만 바뀐다

    cv.imshow('img1', img1)
    cv.imshow('img2', img2)
    cv.imshow('img3', img3)
    cv.waitKey()
    cv.destroyAllWindows()

# func4()


def func6():
    mat1 = np.ones((3,4), np.uint32)
    print(mat1)
    mat2 = np.arange(12).reshape(3,4) # 0~11수를 3x4 행렬로 다시 만듦
    print(mat2)
    mat3 = mat1 + mat2
    mat4 = mat2 * 2
    print(mat3)
    print(mat4)

func6()



import numpy as np
import cv2
import os
from cv2 import Stitcher

if __name__ == "__main__":
    filepath = 'test_img'
    imgs = []

    for item in os.listdir(filepath):
        img = cv2.imread(os.path.join(filepath, item))
        imgs.append(img)

    # img0 = cv2.imread('result/pano1.jpg')
    # img1 = cv2.imread('result/pano6.jpg')
    # img2 = cv2.imread('img/FLIR1982.jpg')
    # img3 = cv2.imread('img/FLIR1979.jpg')

    stitcher = cv2.Stitcher.create()
    #stitcher = cv2.Stitcher.create(cv2.Stitcher_PANORAMA), 根据不同的OpenCV版本来调用
    (_result, pano) = stitcher.stitch(imgs)

    cv2.imwrite('result/pano9.jpg', pano)

    cv2.namedWindow('pano', 0)
    cv2.imshow('pano', pano)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

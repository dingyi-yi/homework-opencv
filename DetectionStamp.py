import cv2
import numpy as np
'''
Created on 2020年10月14日
检测红色盖章
因为印章是红色的，故利用掩模的方式获取所需印章
@author: dingxinlong
'''
class DetectionStamp():

    def __init__(self):
        pass

    def start(self,img,bool):
        '''
        获取图像中红色区域
        :param img: 原始图像
        :param bool: true保留红色区域（false去除红色区域
        :return: 图像
        '''
        # BGR转HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        low_hsv = np.array([150, 103, 100])
        high_hsv = np.array([180, 255, 255])
        # 提取掩膜
        mask = cv2.inRange(hsv, lowerb=low_hsv, upperb=high_hsv)
        if bool==True:
            index1 = mask == 255
        else:
            index1 = mask != 255

        dst = np.zeros(img.shape, np.uint8)
        dst[:, :] = (255, 255, 255)
        dst[index1] = img[index1]  # (0,0,255

        return dst





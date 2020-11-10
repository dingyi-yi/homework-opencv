import cv2
import numpy as np
'''
Created on 2020年10月14日
对图片进形矫正
cv2.HoughLinesP对直线进行提取
通过平均计算直线平均斜率来矫正图片
@author: dingxinlong
'''


class Correct():

    def __init__(self):
        pass;


    def getlines(self,img):
        '''
        获取图片直线
        :param img:图片数据（type=numpy
        :return:直线列表
        '''
        #转换为灰度图片
        cvt= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #边缘检测
        can = cv2.Canny(cvt, threshold1=50, threshold2=150)
        #直线检测
        lines = cv2.HoughLinesP(can, 1, np.pi / 180, 100, minLineLength=500, maxLineGap=20)

        return lines

    def getangle(self,lines):
        '''
        根据直线，计算角度
        :param lines: 检测直线列表
        :return: 角度
        '''
        sum=0
        count=0
        num=0
        for line in lines:
            num=num+1
            for x1, y1, x2, y2 in line:
                #仅计算倾斜的直线
                if x1!=x2 and y1!=y2:
                    #计算斜率
                    k = (y2 - y1) / (x2 - x1)
                    #计算角度
                    result = np.arctan(k) * 57.29577
                    if result >-20 and result <20:
                        sum = sum + result;
                        count = count + 1;
        #如果倾斜的直线不超过1/5条，则认为不需要旋转
        if count<len(lines)/5:
            s=0
        else:
            s=(sum)/count
        return  s

    def rotateimg(self,img,angle):
        '''
        旋转图片
        :param img: 图片
        :param angle: 角度
        :return: 返回图片
        '''
        #图片尺寸
        (height, width) = img.shape[:2]
        #旋转核，旋转点：图片中心点。缩放比例：1
        matRotate = cv2.getRotationMatrix2D((height * 0.5, width * 0.5), angle, 1)
        #进行旋转，旁边补白色
        dst = cv2.warpAffine(img, matRotate, (width, height), borderValue=(255, 255, 255))
        return dst


    def start(self,img):
        '''
        开始执行
        :param img: 传入图片
        :return: 返回矫正图片
        '''
        lines=self.getlines(img=img)
        angle=self.getangle(lines=lines)
        dst=self.rotateimg(img=img,angle=angle)

        return dst









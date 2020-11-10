import pytesseract
import cv2
import numpy as np
'''
Created on 2020年10月14日
识别第一行文字
使用ocr识别图像
利用掩模的方式获取要识别的图像
@author: dingxinlong
'''


class EetractCharacter():
    def __init__(self):
        pass


    def getpoint(self,lines):
        '''
        获取要识别区域的点位
        :param lines: 识别图片中的线
        :return: 四个点（type=list
        '''
        list = None
        min = [0, 0, 0, 0]
        a = 3000
        #获取最上方的直线
        for line in lines:
            for x1, y1, x2, y2 in line:
                #获取y最小且大于100的横线
                if y1 < a and y1 > 100 and abs(x2-x1)>abs(y2-y1):
                    a = y1
                    min[0] = x1
                    min[1] = y1
                    min[2] = x2
                    min[3] = y2
        #计算k和b
        k = (min[3] - min[1]) / (min[2] - min[0])
        b = min[1] - k * min[0]
        #四个点
        list = np.array([[(0, b), (2550, 2550 * k + b), (2550, 2550 * k + b + 150),(0, b + 150)]],dtype=np.int32)

        return list




    def getarea(self,orimg,list):
        '''
        获取要识别区域图形
        :param orimg: 原始图像
        :param list: 需要获取的四个点位
        :return: 返回需要识别的图像
        '''
        #创建与图像大小一致的图像（全0，黑色）
        mask = np.zeros(orimg.shape,dtype=np.uint8)
        #颜色全白（255）
        ignore_mask_color = (255,) * orimg.shape[2]
        # 创建mask层,获取掩模
        cv2.fillPoly(mask, list, ignore_mask_color)
        #与操作，获取需要图像
        mask_img = cv2.bitwise_and(orimg, mask)
        return mask_img


    def Orcimg(self,img):
        '''
        识别文字
        :param img: 要识别的区域
        :return:
        '''
        import DetectionStamp as De
        import correct as Correct
        det = De.DetectionStamp()
        cor = Correct.Correct()
        #去除红色印章
        img=det.start(img=img,bool=False)
        # 对图片矫正
        img = cor.start(img)
        # 识别文字
        text = pytesseract.image_to_string((img), lang='chi_sim')
        return text,img


    def start(self,orimg,lines):
        '''
        执行操作
        :param orimg: 原始图像
        :param lines: 图像上已经检测的线
        :return: 识别的文字和识别的区域
        '''
        point=self.getpoint(lines=lines)
        img=self.getarea(orimg=orimg,list=point)
        text,img=self.Orcimg(img=img)
        return text,img









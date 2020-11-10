import cv2
import correct as Correct
import ExtractCharacter as EC
import  DetectionStamp as De
'''
Created on 2020年10月14日
矫正图片，提取印章，识别第一行文字
@author: dingxinlong
'''
#原始图像
orimg = cv2.imread("30001.JPG")

def imgshow(img):
    '''
    显示图片
    :param img:
    :return:
    '''
    cv2.namedWindow("orimg", cv2.WINDOW_FREERATIO)
    cv2.imshow("orimg", orimg)

    cv2.namedWindow("img", cv2.WINDOW_FREERATIO)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def correctimg():
    '''
    矫正图片
    :return:
    '''
    cor=Correct.Correct()
    #获取已经矫正的图像
    img=cor.start(orimg)

    #画出标定线
    cv2.putText(img,"vertical line",(165,200),cv2.FONT_HERSHEY_SIMPLEX,2.5,(0,0,255),5)
    cv2.putText(img,"horizontal line", (1500, 290), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 255, 0), 5)
    cv2.line(img,(0,300),(2550,300),(0,255,0),10)
    cv2.line(img,(162,0),(162,3500),(0,0,255),10)
    imgshow(img)



def getStamp():
    '''
    矫正图片
    :return:
    '''
    det=De.DetectionStamp()
    img=det.start(img=orimg,bool=True)
    imgshow(img)

def getworld():
    '''
    获取文字
    :return:
    '''
    ect=EC.EetractCharacter()
    cor = Correct.Correct()
    lines=cor.getlines(img=orimg)
    text,img=ect.start(orimg=orimg,lines=lines)
    print("识别文字:",text)
    imgshow(img)




if __name__=='__main__':

    #getworld()  #识别文字
    #correctimg() #矫正图片
    getStamp()  #获取印章





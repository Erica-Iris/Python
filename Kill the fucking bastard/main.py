
# import cv2
# import  time
# #定义摄像头类
# class cameraComput(object):
#     def __init__(self):
#         #获取摄像头对象，0 系统默认摄像头
#         self.cap = cv2.VideoCapture(0)
#         #判断摄像头是否打开，没有则打开
#         if not self.cap.isOpened():
#             self.cap.open()

#     def getFrame(self):
#         ret,frame = self.cap.read()
#         if ret:
#             cv2.imshow("frame",frame)
#             time.sleep(5)
#         return frame

#     #录制一段时长的
#     def saveVideo(self,filepath,delays):
#         # Define the codec and create VideoWriter object
#         #视频编码
#         fourcc = cv2.VideoWriter_fourcc(*'XVID')
#         outputPath=filepath
#         # 20fps ,640*480size
#         out = cv2.VideoWriter(outputPath,fourcc, 20.0, (640,480))
#         startTime = time.time()
#         while(self.cap.isOpened):
#             ret,frame = self.cap.read()
#             if ret:
#                 #翻转图片
#                 # frame = cv2.flip(frame,0)
#                 # write the flipped frame
#                 out.write(frame)
#                 cv2.imshow('frame',frame)
#                 if cv2.waitKey(1) & 0xFF == ord('q'):
#                     break
#             else:
#                 break
#             if time.time() - startTime > delays :
#                 break
#         out.release()
#         cv2.destroyAllWindows()
#         return True

#     #保存一个快照
#     def saveSnapshot(self,filepath):
#         if self.cap.isOpened :
#             ret,frame = self.cap.read()
#             if ret:
#                 cv2.imwrite(filepath,frame)
#             else:
#                 print("save snapshot fail")
#                 return False
#         return True

#     def releaseDevice(self):
#         #释放设备
#         self.cap.release()


#     def reOpen(self):
#         if not self.cap.isOpened():
#             print("re opened device")
#             self.cap = cv2.VideoCapture(0)
#             if not self.cap.isOpened():
#                 self.cap.open()


import cv2
import send_error_message_by_email


def CatchPICFromVideo(camera_idx):
    cv2.namedWindow("image",0) #可调节大小
    #qcv2.resizeWindow("image", 1600, 900)  # 设置长和宽
    # 视频来源，可以来自一段已存好的视频，也可以直接来自USB摄像头
    # cap = cv2.VideoCapture(camera_idx)
    cap = cv2.VideoCapture(0)

    # 告诉OpenCV使用人脸识别分类器
    data_path = "E:\haarcascade_frontalface_default.xml" #自己电脑模型地址 不要有中文
    classfier = cv2.CascadeClassifier(data_path)

    # 识别出人脸后要画的边框的颜色，RGB格式
    color = (0, 255, 0)

    num = 0
    
    send_email=False
    
    while cap.isOpened():
        ok, frame1 = cap.read()  # 读取一帧数据
        # frame1 = cv2.transpose(frame1)
        # frame1 = cv2.flip(frame1,1)
        scale_percent = 50  # percent of original size   缩小到原来50%
        width = int(frame1.shape[1] * scale_percent / 100)
        height = int(frame1.shape[0] * scale_percent / 100)
        dim = (width, height)
        frame = cv2.resize(frame1, dim, interpolation=cv2.INTER_AREA)
        if not ok:
            break
        # 将当前桢图像转换成灰度图像
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
        # 人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        if len(faceRects) > 0:  # 大于0则检测到人脸
            send_error_message_by_email.Sendmail(send_to='1758797550@qq.com')
            for faceRect in faceRects:  # 单独框出每一张人脸
                x, y, w, h = faceRect

                # 将当前帧保存为图片
                #img_name = '%s/%d.jpg ' %(path_name, num)
                #image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                #cv2.imwrite(img_name, image)
                num += 1
                #if num > catch_pic_num:  # 如果超过指定最大保存数量退出循环
                    #break

                # 画出矩形框
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)

                # 显示当前捕捉到了多少人脸图片了，这样站在那里被拍摄时心里有个数，不用两眼一抹黑傻等着
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame ,'num:%d' % (num) ,(x + 30, y + 30), font, 1, (255 ,0 ,255) ,4)

                # 超过指定最大保存数量结束程序
        #if num > catch_pic_num:
            #break

        # 显示图像q
        cv2.imshow("image", frame)
        c = cv2.waitKey(1)
        if c & 0xFF == ord('q'):
            break
    # 释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    CatchPICFromVideo(r'E:\a.MP4')



#print(CatchPICFromVideo(r'H:\renwu__opencv\zhaopian\IMG_3849.MOV'))  #0表示笔记本自带的摄像头  否则就是视频地址 不要有中文
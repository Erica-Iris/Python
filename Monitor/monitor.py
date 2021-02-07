
import cv2
import os
from send_QQ_msg import *
import random
# 获取本地摄像头
# folder_path 截取图片的存储目录
def get_img_from_camera_local(folder_path):
    cap = cv2.VideoCapture(0)
    i = 1
    while True:
        ret, frame = cap.read()
        cv2.imshow("capture", frame)
        # print(str(i))
        cv2.imwrite(folder_path + str(i) + '.jpg', frame)# 存储为图像
        sendByUser('NULL')
        setImage(folder_path + str(i) + '.jpg')
        sendByUser('NULL')
        time.sleep(random.randint(1,8))
        if os.path.exists(folder_path + str(i) + '.jpg'):
            os.remove(folder_path + str(i) + '.jpg')
            print('已删除: '+(folder_path + str(i) + '.jpg'))
        else:
            print('文件不存在: '+ (folder_path + str(i) + '.jpg'))
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        i += 1
    cap.release()
    cv2.destroyAllWindows()
# 测试
if __name__ == '__main__':
 
    folder_path = 'E:\\img_from_camera\\'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    get_img_from_camera_local(folder_path)


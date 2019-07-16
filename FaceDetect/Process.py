import os
from PIL import  Image
import numpy as np
import cv2


class FaceProcess(object):
    """
    为每一个学生训练单独的数据,生成100张的图片数据,
    训练成功后删除人脸数据,保留人脸模型
    """
    def __init__(self,_id,is_teacher=False):
        self._id=_id       # 学号或者工号
        self.is_teacher=is_teacher    # 是否为老师
        self.data_folder=None
        self.model=None

    def prepare_train_data(self):
        if self.is_teacher:
            self.data_folder='Teacher_'+self._id
        else:
            self.data_folder='Stu_'+self._id
        self.model = '../DataSet/MODELS/' + self.data_folder + '.yml'
        self.data_folder='../DataSet/PICS/'+self.data_folder
        faces = []
        labels = []
        for image_name in os.listdir(self.data_folder):
            # data_folder_path 类似于DataSet/PICS/stu_20164859
            image = Image.open(os.path.join(self.data_folder,image_name)).convert('L')
            image = np.array(image, 'uint8')
            faces.append(image)
            labels.append(int(self._id))
        print(labels)
        return faces, labels

    def train(self):
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        faces, labels = self.prepare_train_data()
        face_recognizer.train(faces, np.array(labels))
        face_recognizer.save(self.model)  # 保存


if __name__ == '__main__':
    p=FaceProcess('20164859',False)
    p.train()
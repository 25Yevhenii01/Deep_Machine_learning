from imageai.Detection import ObjectDetection
import os

#variable which can get path for project
exec_path = os.getcwd()


detector = ObjectDetection()#create object
detector.setModelTypeAsRetinaNet()#use model RetinaNet
detector.setModelPath(
    os.path.join(exec_path, "resnet50_coco_best_v2.0.1.h5")
)#set model path
detector.loadModel()

list = detector.detectObjectsFromImage(
    input_image=os.path.join(exec_path, "objects.jpg"),
    output_image_path=os.path.join(exec_path, "recognize_objects.jpg")
)
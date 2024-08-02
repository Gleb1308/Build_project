import numpy as np
import os
from constants import classes
from helper_funcs import *


def get_boxes(image, use_int=False):
    with open(f'kitti_dataset/label_2_orig/{image}'[:-3]+'txt', 'r') as file:
        lines = file.readlines()
        cls = [np.arange(classes.size)[classes == line.split()[0]][0] for line in lines if line.split()[0] != 'DontCare']
        if use_int:
            boxes = [[int(float(el)) for el in line.split()[4:8]] for line in lines if line.split()[0] != 'DontCare']
        else:
            boxes = [[float(el) for el in line.split()[4:8]] for line in lines if line.split()[0] != 'DontCare']
    return cls, boxes


# label = '000001.txt'
# frame = cv.imread(f'kitti_dataset/image_2/{label}'[:-3]+'png')
# cls, boxes = get_boxes(label[:-3]+'png', use_int=True)
# cls = classes[cls]
# frame_trans = frame_plot(boxes, cls, frame)
# cv.imshow('trans_frame', frame_trans)
# cv.waitKey(0)

images = os.listdir('kitti_dataset/image_2')
for image in images:
    cls, boxes = get_boxes(image)
    im_shape = cv.imread('kitti_dataset/image_2/' + image).shape
    with open(f'kitti_dataset/label_2_xyxyn/{image}'[:-3]+'txt', 'w') as file:
        for box, cl in zip(boxes, cls):
            # box = np.round(box1_to_box2("xyxy", "xywh", box, im_shape), 5)
            box = np.array(box)
            box[::2] = box[::2] / im_shape[1]
            box[1::2] = box[1::2] / im_shape[0]
            box = np.round(box, 5)
            line = ' '.join([str(cl)] + [str(el) for el in box] + ['\n'])
            file.write(line)

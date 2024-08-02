import cv2 as cv
from constants import rel_width_base


def box1_to_box2(type1, type2, box, image_shape=None):  # box of type1; return box of type2
    if type1 == type2:
        return box
    elif type1 == "xyxy" and type2 == "xywh":
        width, height = box[2] - box[0], box[3] - box[1]
        cx, cy = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2
        new_box = [cx, cy, width, height]
        if image_shape is None:
            return new_box
        new_box = [cx/image_shape[1], cy/image_shape[0], width/image_shape[1], height/image_shape[0]]
        return new_box
    elif type1 == "xywh" and type2 == "xyxy":
        x_min, y_min = box[0]-box[2]/2, box[1]-box[3]/2
        x_max, y_max = box[0]+box[2]/2, box[1]+box[3]/2
        new_box = [x_min, y_min, x_max, y_max]
        if image_shape is None:
            return new_box
        new_box = [x_min*image_shape[1], y_min*image_shape[0], x_max*image_shape[1], y_max*image_shape[0]]
        return new_box


def frame_plot(boxes, obj_cls, frame):
    for box, cls in zip(boxes, obj_cls):
        rel_width = (box[2]-box[0])/frame.shape[1]
        cv.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 0, 255), thickness=2)
        cv.putText(frame, cls, (box[0], box[1]-3), cv.FONT_HERSHEY_TRIPLEX, rel_width/rel_width_base, (0, 255, 0))
    return frame

import cv2 as cv


def box1_to_box2(type1, type2, box, image_shape=None):  # box of type1; return box of type2
    if type1 == type2:
        return box
    elif type1 == "AABB" and type2 == "YOLO":
        width, height = box[2] - box[0], box[3] - box[1]
        cx, cy = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2
        new_box = [cx, cy, width, height]
        if image_shape is None:
            return new_box
        new_box = [cx/image_shape[1], cy/image_shape[0], width/image_shape[1], height/image_shape[0]]
        return new_box
    elif type1 == "YOLO" and type2 == "AABB":
        x_min, y_min = box[0]-box[2]/2, box[1]-box[3]/2
        x_max, y_max = box[0]+box[2]/2, box[1]+box[3]/2
        new_box = [x_min, y_min, x_max, y_max]
        if image_shape is None:
            return new_box
        new_box = [x_min*image_shape[1], y_min*image_shape[0], x_max*image_shape[1], y_max*image_shape[0]]
        return new_box


def frame_plot(boxes, obj_cls, frame):
    for box, cls in zip(boxes, obj_cls):
        cv.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), thickness=2)
        cv.putText(frame, cls, (box[0], box[1]-3), cv.FONT_HERSHEY_TRIPLEX, 0.75, (0, 255, 0))
    return frame

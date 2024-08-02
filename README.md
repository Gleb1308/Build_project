# Project description
<p>First step in building autonomous driving system - object detection system. It will distinguish such objects as people, cars, roads and so on. 
This would help further training the whole system to take right actions during driving process. 
Moreover such detection system should be very effective so that it can process images in real time.</p>

<p>Our detection system uses yolo-detectors from ultralytics. During this project were tested and different yolo models on the kitti-dataset (you can check this dataset on kaggle - ...). Test results of the pretrained and finetuned models you can check in such csv-tables: ... .</p>

If you would like to test detector with some yolo-model you can use file infer.py (it is compatible both with images and videos):
...

If you would like to train detector on your own dataset you can file train.py:
...

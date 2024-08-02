# Project description
<p>First step in building autonomous driving system - object detection system. It will distinguish such objects as people, cars, roads and so on. 
This would help further training the whole system to take right actions during driving process. 
Moreover such detection system should be very effective so that it can process images in real time.</p>

<p>Our detection system uses yolo-detectors from ultralytics. During this project were tested and different yolo models on the kitti-dataset (you can check this dataset on kaggle - https://www.kaggle.com/datasets/glebsukhomlyn/kitti-dataset). Test results of the pretrained and finetuned models you can check in the 'tables' folder: 
  pretr_models_eval.csv - quality of the pretrained models measured on the test part of the kitti-dataset;
  models_training.csv - best pretrained models;
  finetuned_models.csv - quality of the best models after fine-tuning (you can upload theses weights via such link - https://drive.google.com/file/d/1U7bRLXEgh4Am4qIQ0uQgfi4koRGvK8NN/view?usp=drive_link);
  opt_params.csv - optimal hyperparameters for finituned models.</p>

If you would like to test detector with some yolo-model you can use file infer.py (it is compatible both with images and videos):
...

If you would like to train detector on your own dataset you can file train.py:
...

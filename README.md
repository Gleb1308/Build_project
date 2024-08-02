# Project description
<p>First step in building autonomous driving system - object detection system. It will distinguish such objects as people, cars, roads and so on. 
This would help further training the whole system to take right actions during driving process. 
Moreover such detection system should be very effective so that it can process images in real time.</p>

<p>Our detection system uses yolo-detectors from ultralytics. During this project were tested and different yolo models on the kitti-dataset (you can check this dataset on kaggle - https://www.kaggle.com/datasets/glebsukhomlyn/kitti-dataset). Test results of the pretrained and finetuned models you can check in the 'tables' folder: 
<br> - pretr_models_eval.csv - quality of the pretrained models measured on the test part of the kitti-dataset;
<br> - models_training.csv - best pretrained models;
<br> - finetuned_models.csv - quality of the best models after fine-tuning (you can upload theses weights via such link - https://drive.google.com/file/d/1U7bRLXEgh4Am4qIQ0uQgfi4koRGvK8NN/view?usp=drive_link);
<br> - opt_params.csv - optimal hyperparameters for finetuned models.</p>

If you would like to test detector with some yolo-model you can use file infer.py (it is compatible both with images and videos):
```bash
!python infer.py --use_opt_params --to_save --model_path /content/weights/best_yolov8m.pt \
--source Cars_in_Highway_Traffic_FREE-STOCK_VIDEO.mp4 --source_path /content/
```
Detailed information you can get by such command - python infer.py --help

If you would like to train detector on your own dataset you can file train.py:
```bash
python train.py --data_path <path to data> --model_path <path to model config file> --epochs <num epochs to train> \
--n_freeze <number of first layers to ynbfreeze during training>
```
Detailed information you can get by such command - python train.py --help
<br>Also you can review all training\testing process in the jupyter notebook - 'train\test_notebook.ipynb'.

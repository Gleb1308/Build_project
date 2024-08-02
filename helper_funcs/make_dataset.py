import os
import numpy as np
from shutil import copy


tr_split = 0.8
ts_split = 0.15
vl_split = 0.05
os.makedirs('train', exist_ok=True)
os.makedirs('test', exist_ok=True)
os.makedirs('val', exist_ok=True)

folds = os.listdir('kitti_dataset')

images = [im[:-4] for im in os.listdir('kitti_dataset/image_2')]
np.random.shuffle(images)

imgs_train = images[:int(tr_split*len(images))]
imgs_test = images[int(tr_split*len(images)):int((tr_split+ts_split)*len(images))]
imgs_val = images[int((tr_split+ts_split)*len(images)):int((tr_split+ts_split+vl_split)*len(images))]
d = {'train': imgs_train, 'test': imgs_test, 'val': imgs_val}

for n in ['train', 'test', 'val']:
    for img in d[n]:
        for fold in folds:
            if fold == '.DS_Store':
                continue
            os.makedirs(f'{n}/{fold}', exist_ok=True)
            ext = '.png' if fold == 'image_2' else '.txt'
            src = f'kitti_dataset/{fold}/{img}{ext}'
            copy(src, f'{n}/{fold}/')

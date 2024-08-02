from ultralytics import YOLO
import numpy as np
import pandas as pd
import os
import gdown
import argparse

def train_model(model_path, data_path, epochs, n_freeze):
  model = YOLO(model_path)
  results = model.train(data=data_path, epochs=epochs, freeze=n_freeze, project='runs', name=f'train_{model_path[:-3]}')
  return (model, results)

if __name__=="__main__":
  # reading arguments from the command line
  parser = argparse.ArgumentParser()

  parser.add_argument('--data_path', type=str, default="kitti/kitti.yaml", help='path to training data')
  parser.add_argument('--model_path', type=str, default="/content/weights/best_yolov8x.pt", help='path to the model`s weights')
  parser.add_argument('--epochs', type=int, default=40, help='numbers of training epochs')
  parser.add_argument('--n_freeze', type=int, default=10, help='number of first layers to freeze during training')

  args = parser.parse_args()
  model, res = train_model(**args.__dict__)

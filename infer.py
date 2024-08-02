from ultralytics import YOLO
import numpy as np
import pandas as pd
import os
import gdown
import argparse

def infer(source, source_path, comma_sep, model_path, to_show, to_save,
          use_opt_params, conf_opt, iou_opt):

  if comma_sep:
    source = source.split(',')
    source = [f"{source_path}{img}" for img in source]
  else:
    try:
      source = os.listdir(source_path + source)
      source = [f"{source_path}{img}" for img in source]
    except NotADirectoryError:
      source = source_path + source

  model = YOLO(model_path)
  try:
    opt_params = pd.read_csv('opt_params.csv')
  except FileNotFoundError:
    file_id = '1VxZWLpMaKtpbJN11fHqjXCL3tLd5Ru5U'
    gdown.download(f"https://drive.google.com/uc?id={file_id}", 'opt_params.csv')
    opt_params = pd.read_csv('opt_params.csv')

  if use_opt_params:
    conf_opt = opt_params['conf_opt'].iloc[0]
    iou_opt = opt_params['iou_opt'].iloc[0]
  model_name = model_path.split('/')[-1]
  opt_params = opt_params[opt_params['model']==model_name]
  preds = model.predict(source, save=to_save, conf=conf_opt, iou=iou_opt, show=to_show)

if __name__=="__main__":
  # reading arguments from the command line
  parser = argparse.ArgumentParser()

  parser.add_argument('--source', type=str, default='000037.png', help='names of the images or video')
  parser.add_argument('--source_path', type=str, default='/content/kitti/images/test/',
                      help='path to the images or video')
  parser.add_argument('--comma_sep', action='store_true', help='whether img names are separated by comma')
  parser.add_argument('--model_path', type=str, default="/content/weights/best_yolov8x.pt", help='path to the model`s weights')
  parser.add_argument('--to_show', action='store_true', help='whether to visualize results on the display')
  parser.add_argument('--to_save', action='store_true', help='whether to save results')
  parser.add_argument('--use_opt_params', action='store_true', help='whether to use optimal hyperparameters')
  parser.add_argument('--conf_opt', type=float, default=0.5, help='custom cofidence threshold')
  parser.add_argument('--iou_opt', type=float, default=0.5, help='custom iou threshold')

  args = parser.parse_args()
  preds = infer(**args.__dict__)

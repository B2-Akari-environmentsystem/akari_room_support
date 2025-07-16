#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import os
import sys
import glob
import shutil
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--dir", "-d", required=True, help="変換したい画像のディレクトリパスを入力します。")
parser.add_argument("--name", "-n", required=True, help="変換する画像のタグ名を入力します。")
args = parser.parse_args()
tag = args.name + '_'
path = os.getcwd() + '/' + args.dir
os.makedirs(path, exist_ok=True)
output_path = path + '/tmp/'
os.makedirs(output_path, exist_ok=True)
print((args.dir + "/"))
#files = glob.glob((args.dir + "/" + '*.jpeg') or (args.dir + "/" + '*.JPG')
#                  or (args.dir + "/" + '*.png') or (args.dir + "/" + '*.PNG'))
files = glob.glob(args.dir + "/" + '*.png')
files.extend(glob.glob(args.dir + "/" + '*.PNG'))
files.extend(glob.glob(args.dir + "/" + '*.jpg'))
files.extend(glob.glob(args.dir + "/" + '*.jpeg'))
files.extend(glob.glob(args.dir + "/" + '*.JPG'))
files.extend(glob.glob(args.dir + "/" + '*.gif'))
files.extend(glob.glob(args.dir + "/" + '*.GIF'))
print(files)
num = 0
for file in files:
    try:
        img = cv2.imread(file)
        # numを3桁に0埋めして保存。
        file_path = output_path +  tag + str(num).zfill(3) + '.jpg'
        cv2.imwrite(file_path, img)
        os.remove(file)
        print('convert ' + file + ' to ' + file_path)
        num +=1
    except:
        print('convert ' + file + 'failed')

list_file_name = os.listdir(output_path)

for i_file_name in list_file_name:

    join_path = os.path.join(output_path, i_file_name)

    if os.path.isfile(join_path):
        shutil.move(join_path, path)
shutil.rmtree(output_path)

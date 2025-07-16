#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import os
import sys
import glob
import argparse
from pathlib import Path
import cv2
import depthai as dai
import time


def main(args=None) -> None:
    """
    メイン関数
    """
    # OAK-Dのパイプライン作成
    pipeline = dai.Pipeline()
    # ソースとアウトプットの設定
    cam_rgb = pipeline.create(dai.node.ColorCamera)
    xout_video = pipeline.create(dai.node.XLinkOut)

    # RGBのカメラ、1080Pを指定
    cam_rgb.setBoardSocket(dai.CameraBoardSocket.RGB)
    cam_rgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
    # ソースとアウトプットを接続
    cam_rgb.video.link(xout_video.input)

    # キューのブロッキングなし、キューサイズ１を指定
    xout_video.input.setBlocking(False)
    xout_video.input.setQueueSize(1)
    # ストリーミング名設定
    xout_video.setStreamName("video")
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", "-n", type=str, required=True, help="撮影する物のタグ名を入力します。")
    parser.add_argument("--auto_fps", "-a", type=int, required=False, help="指定のFPSで自動撮影します。")
    args = parser.parse_args()
    auto_mode = False
    interval = 0
    if(args.auto_fps):
        auto_mode = True
        interval = 1 / args.auto_fps
    tag = args.name + '_'
    path = os.getcwd() + '/' + args.name
    os.makedirs(path, exist_ok=True)
    files = glob.glob(os.getcwd() + '/' + args.name + '/*')
    name_list = []
    # 既存のファイルがある場合は、ファイル名の通し番号の一番大きいものを取得する。
    num = 0
    for file in files:
        file_name = Path(file).stem
        file_name = file_name.replace(tag, '')
        try:
            file_num = int(file_name)
            if(file_num >= num):
                num = file_num + 1
        except:
            pass
    if(not auto_mode):
        print('cを押すと写真を撮影します。')
        print('qを押すと終了します。')
    # デバイスをパイプラインに接続
    with dai.Device(pipeline) as device:
        video = device.getOutputQueue(name="video", maxSize=1, blocking=False)  # type: ignore

        # 画像を取得しウィンドウに描画
        while True:
            start_time = time.monotonic_ns() / 1000000000
            videoIn = video.get()
            cv2.imshow("video", videoIn.getCvFrame())
            is_capture = False
            input = cv2.waitKey(10) & 0xff
            # q キーを押したら終了
            if input == ord('q'):
                break
            elif input == ord('c') or auto_mode:
                is_capture = True
            if(is_capture):
                # numを3桁に0埋めして保存。
                file_path = path + '/' + tag + str(num).zfill(3) + '.jpg'
                cv2.imwrite(file_path, videoIn.getCvFrame())
                print(file_path + 'を保存しました。')
                # 写真を撮ったらnumを+1する。
                num += 1
            if(auto_mode):
                end_time = time.monotonic_ns() / 1000000000
                remining = interval - (end_time - start_time)
                if(remining) >= 0:
                    time.sleep(remining)


if __name__ == '__main__':
    main()

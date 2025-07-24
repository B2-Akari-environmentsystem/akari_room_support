#main.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sleep
import face_tracking

from akari_client import AkariClient

from akari_client.config import (
   AkariClientConfig,
   JointManagerGrpcConfig,
   M5StackGrpcConfig,
)

from datetime import datetime

# akari_client_configを引数にしてAkariClientを作成する。
akari = AkariClient()

joints = akari.joints
m5 = akari.m5stack
# サーボトルクをONする。
joints.enable_all_servo()

#AkariClient、m5stackのインスタンスを取得する

isSleep = False
count = 0

Now_time = datetime.now()

while(1):
    #ボタン、センサ全般の情報を取得
    data = m5.get()

    if(data["brightness"]>3500):#寝る動作
        sleep.sleep(m5,joints,isSleep)

        count += 1
        if count >= 1:
            isSleep = True

        time.sleep(1)

    else:#起きる動作
        isSleep = False
        face_tracking.face_tracking(m5,joints,Now_time)

        time.sleep(1)
    
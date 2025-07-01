#main.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sleep
import getup

from akari_client import AkariClient
#ディスプレイ上の文字の位置を指定する際に使うPositionsのインポート
from akari_client.position import Positions
#ディスプレイに関する色を指定する際に使うColors,Colorのインポート
from akari_client.color import Colors, Color

from akari_client.config import (
   AkariClientConfig,
   JointManagerGrpcConfig,
   M5StackGrpcConfig,
)

# akari_client_configを引数にしてAkariClientを作成する。
akari = AkariClient()

joints = akari.joints
m5 = akari.m5stack
# サーボトルクをONする。
joints.enable_all_servo()

#AkariClient、m5stackのインスタンスを取得する


while(1):
    #ボタン、センサ全般の情報を取得
    data = m5.get()

    if(data["brightness"]>3500):#寝る動作
        sleep.sleep(m5,joints)

    else:#起きる動作
        face_tracking.face_tracking(m5,joints)
    
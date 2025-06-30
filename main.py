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

"""
メイン関数
"""
# AKARI本体のIPアドレスを指定する。
# 実際のAKARIのIPアドレスに合わせて変更すること。
akari_ip = "172.31.14.13"
# portは初期設定のままであれば51001固定
akari_port = "51001"
akari_endpoint = f"{akari_ip}:{akari_port}"

joint_config: JointManagerGrpcConfig = JointManagerGrpcConfig(
    type="grpc", endpoint=akari_endpoint
)
m5_config: M5StackGrpcConfig = M5StackGrpcConfig(
    type="grpc", endpoint=akari_endpoint
)
akari_client_config = AkariClientConfig(
    joint_manager=joint_config, m5stack=m5_config
)
# akari_client_configを引数にしてAkariClientを作成する。
akari = AkariClient(akari_client_config)

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
        getup.getup(joints)
    
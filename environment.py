from akari_client import AkariClient
#ディスプレイ上の文字の位置を指定する際に使うPositionsのインポート
from akari_client.position import Positions
#ディスプレイに関する色を指定する際に使うColors,Colorのインポート
from akari_client.color import Colors, Color

from datetime import datetime

import psutil

from play_sound import play_sound

import random

def environment(m5,Now_time) -> None:
    data = m5.get()

    boot_time = psutil.boot_time()
    boot_datetime = datetime.fromtimestamp(boot_time)

    difference = Now_time - boot_datetime

    total_seconds = int(difference.total_seconds())

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60



    temp = int(data["temperature"])

    if hours > 0:
        temp -= 6
    elif minutes < 28:
        temp -= 5
    elif minutes < 22:
        temp -= 4
    elif minutes < 16:
        temp -= 3
    elif minutes < 12:
        temp -= 2
    elif minutes < 8:
        temp -= 1



    press = int(data["pressure"] / 100)

    if data["button_a"] == True:

        m5.set_pwmout(pin_id=0,value=False)
        m5.set_dout(pin_id=0,value=False)
        m5.set_dout(pin_id=1,value=False)

        m5.set_display_text(str(Now_time.year) + "年 " + str(Now_time.month) + "月 " + str(Now_time.day)+ "日", pos_x=Positions.CENTER,pos_y=Positions.TOP, size=3)
        m5.set_display_text("気温",pos_x=Positions.CENTER,pos_y=Positions.CENTER, refresh=False, size=7)
        m5.set_display_text(str(temp) + "度",pos_x=Positions.CENTER,pos_y=Positions.BOTTOM,refresh=False, size=7)

        if 18 <= temp and temp <= 25:
            #ちょうど良い

            random_number = random.randint(1,41)

            m5.set_dout(pin_id=1,value=False)
            m5.set_dout(pin_id=0,value=False)

            m5.set_pwmout(pin_id=0,value=100)

            if 1 <= random_number and random_number <= 20:
                play_sound("./voice/ちょうど良い気温ですね！勉強や作業にも適した環境になってます！.wav")
            if 21 <= random_number and random_number <= 40:
                play_sound("./voice/とても良い環境ですね、リラックスするのにもちょうど良い気温になっています！.wav")
            if random_number = 41:
                play_sound("./voice/リモコンという名の聖剣を手にし、私はついにこの部屋の温度を統べる王となったのだあああ.wav")
        
        if 13 <= temp and temp < 18:
            #LED 黄色　少し寒い

            random_number = random.randint(1,3)

            m5.set_pwmout(pin_id=0,value=False)
            m5.set_dout(pin_id=0,value=False)

            m5.set_dout(pin_id=1,value=True)

            if random_number = 1:
                play_sound("./voice/少し肌寒いですね、足先が冷えないように暖かい靴下を履きましょう.wav")
            if random_number = 2:
                play_sound("./voice/少し肌寒いですね、暖かい飲み物を飲んで体を労ってあげましょう.wav")
            if random_number = 3:
                play_sound("./voice/少し肌寒いですね、湯たんぽや膝掛けがあると良いかもしれません.wav")


        if temp < 13:
            #LED 黄色二つ　寒い

            random_number = random.randint(1,11)

            m5.set_pwmout(pin_id=0,value=False)

            m5.set_dout(pin_id=1,value=True)
            m5.set_dout(pin_id=0,value=True)

            if 1 <= random_number and random_number <= 5:
                play_sound("./voice/かなり冷え込んでますね、ストーブやこたつで暖まりましょう.wav")
            if 6 <= random_number and random_number <= 10:
                play_sound("./voice/かなり冷え込んでますね、エアコンをつけて部屋を温めましょう.wav")
            if random_number = 11:
                play_sound("./voice/samuikogoeru.wav")

        if 25 < temp and temp <= 30:
            #LED 黄色　少し暑い

            random_number = random.randint(1,3)

            m5.set_pwmout(pin_id=0,value=False)
            m5.set_dout(pin_id=0,value=False)

            m5.set_dout(pin_id=1,value=True)

            if random_number = 1:
                play_sound("./voice/少し暑いですね、レースカーテンなどで日差しを遮断してもいいかもしれませんね。.wav")
            if random_number = 2:
                play_sound("./voice/少し暑いですね、扇風機をつけてみてはいかがでしょうか？.wav")
            if random_number = 3:
                play_sound("./voice/少し暑いですね、窓を開けて風通しをよくしましょう.wav")



        if 30 < temp:
            #LED 黄色二つ　暑い

            random_number = random.randint(1,11)

            m5.set_pwmout(pin_id=0,value=False)

            m5.set_dout(pin_id=1,value=True)
            m5.set_dout(pin_id=0,value=True)

            if 1 <= random_number and random_number <= 5:
                play_sound("./voice/大変危険な温度となっております。　一刻も早く冷房をつけましょう。.wav")
            if 6 <= random_number and random_number <= 10:
                play_sound("./voice/大変危険な温度となっております。　水分をとり、熱中症に気をつけましょう。.wav")
            if random_number = 11:
                play_sound("./voice/危ないよーーーーんんん、死ぬぞおおおおおおおおお.wav")

    if data["button_c"] == True:

        m5.set_pwmout(pin_id=0,value=False)
        m5.set_dout(pin_id=0,value=False)
        m5.set_dout(pin_id=1,value=False)

        m5.set_display_text(str(Now_time.year) + "年 " + str(Now_time.month) + "月 " + str(Now_time.day)+ "日", pos_x=Positions.CENTER,pos_y=Positions.TOP, size=3)

        m5.set_display_text("気圧",pos_x=Positions.CENTER,pos_y=Positions.CENTER, refresh=False, size=7)
        m5.set_display_text(str(press) + "hPa",pos_x=Positions.CENTER,pos_y=Positions.BOTTOM, refresh=False, size=7)

    if data["button_b"] == True:

        m5.set_pwmout(pin_id=0,value=False)
        m5.set_dout(pin_id=0,value=False)
        m5.set_dout(pin_id=1,value=False)

        m5.set_display_text(str(Now_time.year) + "年 " + str(Now_time.month) + "月 " + str(Now_time.day)+ "日", pos_x=Positions.CENTER,pos_y=Positions.TOP, size=3)

        m5.set_display_text("気温",pos_x=Positions.LEFT,pos_y=Positions.CENTER, refresh=False, size=7)
        m5.set_display_text(str(temp) + "度",pos_x=Positions.LEFT,pos_y=Positions.BOTTOM, refresh=False, size=5)

        m5.set_display_text("気圧",pos_x=Positions.RIGHT,pos_y=Positions.CENTER, refresh=False, size=7)
        m5.set_display_text(str(press) + "hPa",pos_x=Positions.RIGHT,pos_y=Positions.BOTTOM, refresh=False, size=5)
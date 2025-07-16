from akari_client import AkariClient
#ディスプレイ上の文字の位置を指定する際に使うPositionsのインポート
from akari_client.position import Positions
#ディスプレイに関する色を指定する際に使うColors,Colorのインポート
from akari_client.color import Colors, Color

from datetime import datetime

def environment(m5,Startup_time) -> None:
    data = m5.get()



    temp = int(data["temperature"])
    press = int(data["pressure"] / 100)

    if data["button_a"] == True:

        m5.set_display_text(str(Startup_time.year) + "年 " + str(Startup_time.month) + "月 " + str(Startup_time.day)+ "日", pos_x=Positions.CENTER,pos_y=Positions.TOP, size=4)
        m5.set_display_text("気温",pos_x=Positions.CENTER,pos_y=Positions.CENTER, refresh=False, size=7)
        m5.set_display_text(str(temp) + "度",pos_x=Positions.CENTER,pos_y=Positions.BOTTOM,refresh=False, size=7)

        if 18 <= data["temperature"] and data["temperature"] <= 25:

            m5.set_dout(pin_id=1,value=False)
            m5.set_dout(pin_id=0,value=False)

            m5.set_pwmout(pin_id=0,value=100)
        
        if 13 <= data["temperature"] and data["temperature"] < 18:
            #LED 黄色　少し寒い

            m5.set_pwmout(pin_id=0,value=False)
            m5.set_dout(pin_id=0,value=False)

            m5.set_dout(pin_id=1,value=True)

        if data["temperature"] < 13:
            #LED 黄色二つ　寒い
            m5.set_pwmout(pin_id=0,value=False)

            m5.set_dout(pin_id=1,value=True)
            m5.set_dout(pin_id=0,value=True)

        if 25 < data["temperature"] and data["temperature"] <= 30:
            #LED 黄色　少し暑い

            m5.set_pwmout(pin_id=0,value=False)
            m5.set_dout(pin_id=0,value=False)

            m5.set_dout(pin_id=1,value=True)

        if 30 < data["temperature"]:
            #LED 黄色二つ　暑い

            m5.set_pwmout(pin_id=0,value=False)

            m5.set_dout(pin_id=1,value=True)
            m5.set_dout(pin_id=0,value=True)

    if data["button_c"] == True:

        m5.set_pwmout(pin_id=0,value=False)
        m5.set_dout(pin_id=0,value=False)
        m5.set_dout(pin_id=1,value=False)

        m5.set_display_text(str(Startup_time.year) + "年 " + str(Startup_time.month) + "月 " + str(Startup_time.day)+ "日", pos_x=Positions.CENTER,pos_y=Positions.TOP, size=4)

        m5.set_display_text("気圧",pos_x=Positions.CENTER,pos_y=Positions.CENTER, refresh=False size=7)
        m5.set_display_text(str(press) + "hPa",pos_x=Positions.CENTER,pos_y=Positions.BOTTOM, refresh=False, size=7)

    if data["button_b"] == True:

        m5.set_pwmout(pin_id=0,value=False)
        m5.set_dout(pin_id=0,value=False)
        m5.set_dout(pin_id=1,value=False)

        m5.set_display_text(str(Startup_time.year) + "年 " + str(Startup_time.month) + "月 " + str(Startup_time.day)+ "日", pos_x=Positions.CENTER,pos_y=Positions.TOP, size=4)

        m5.set_display_text("気温",pos_x=Positions.LEFT,pos_y=Positions.CENTER, refresh=False, size=7)
        m5.set_display_text(str(temp) + "度",pos_x=Positions.LEFT,pos_y=Positions.BOTTOM, refresh=False, size=5)

        m5.set_display_text("気圧",pos_x=Positions.RIGHT,pos_y=Positions.CENTER, refresh=False, size=7)
        m5.set_display_text(str(press) + "hPa",pos_x=Positions.RIGHT,pos_y=Positions.BOTTOM, refresh=False, size=5)
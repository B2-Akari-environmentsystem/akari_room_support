#sleep.py
#AkariClientのインポート
from akari_client import AkariClient
#ディスプレイ上の文字の位置を指定する際に使うPositionsのインポート
from akari_client.position import Positions
#ディスプレイに関する色を指定する際に使うColors,Colorのインポート
from akari_client.color import Colors, Color
#音声
from play_sound import play_sound

def sleep(m5,joints,isSleep) -> None:

    #寝る動作
    #ディスプレイを黒くする
    m5.set_display_color(Colors.BLACK)
    m5.set_pwmout(pin_id=0,value=False)
    m5.set_dout(pin_id=0,value=False)
    m5.set_dout(pin_id=1,value=False)

    m5.set_display_text("Z",pos_x=Positions.LEFT,pos_y=Positions.TOP, text_color=Colors.BLUE, size=9)
    m5.set_display_text("Z",pos_x=Positions.CENTER,pos_y=Positions.CENTER, text_color=Colors.BLUE, refresh=False, size=7)
    m5.set_display_text("Z",pos_x=Positions.RIGHT,pos_y=Positions.BOTTOM, text_color=Colors.BLUE, refresh=False, size=5)

    if not isSleep:
        play_sound("./voice/おやすみなさい.wav")



    #首動かす速度を縦方向、横方向に3rad/s
    joints.set_joint_velocities(pan=3,tilt=3)
    #首の位置を寝てる状態にする
    joints.move_joint_positions(pan=0,tilt=-0.5)

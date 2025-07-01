#AkariClientのインポート
from akari_client import AkariClient
#ディスプレイ上の文字の位置を指定する際に使うPositionsのインポート
from akari_client.position import Positions
#ディスプレイに関する色を指定する際に使うColors,Colorのインポート
from akari_client.color import Colors, Color

def sleep(m5,joints) -> None:

    #寝る動作
    #ディスプレイを黒くする
    m5.set_display_color(Colors.BLACK)
    #首動かす速度を縦方向、横方向に3rad/s
    joints.set_joint_velocities(pan=3,tilt=3)
    #首の位置を寝てる状態にする
    joints.move_joint_positions(pan=0,tilt=-0.5)

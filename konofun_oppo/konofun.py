# This Python file uses the following encoding: utf-8
# pip install android-auto-play-opencv
import android_auto_play_opencv as am
import subprocess
from numpy import imag

from pkg_resources import to_filename
# adbpath = 'C:\\Users\\higik\\OneDrive\\ドキュメント\\platform-tools\\'
adbpath = "/Applications/platform-tools/"
imgpath = "konofun_oppo/img/"
def main():
    aapo = am.AapoManager(adbpath)
    aapo.touchPos(1840, 360)
    aapo.sleep(2)
    aapo.touchPos(1160, 540)
    aapo.sleep(3)
    aapo.touchPos(1600, 370)
    aapo.sleep(3)
    aapo.touchPos(1928, 740)
    aapo.touchPos(1928, 740)
    while True:
        # 画面キャプチャ
        aapo.screencap()
        # イベントの挑戦準備をおしたら
        if aapo.touchImg(imgpath + "chosen.png"):
            aapo.sleep(2.5)
            # aapo.screencap()
            # aapo.touchImg(imgpath + "enterroom.png")
            aapo.touchPos(1800, 1020)
            print("sleep 40 second")
            aapo.sleep(40)
        if aapo.touchImg(imgpath + "next.png"):
            aapo.sleep(5)
            # aapo.screencap()
            # aapo.touchImg(imgpath + "backroom.png")
            aapo.touchPos(1400, 975)
            aapo.sleep(1)
            # aapo.screencap()
            # aapo.touchImg(imgpath + "ok.png")
            aapo.touchPos(1400, 740)
            aapo.sleep(12)
            aapo.screencap()
            if aapo.touchImg(imgpath + "boshu.png"):
                print("sleep 40 second")
                aapo.sleep(40)
            # ルームが解散した時
            elif aapo.touchImg(imgpath + "ok.png"):
                aapo.sleep(5)
                aapo.touchPos(1840, 360)
                aapo.sleep(2)
                aapo.touchPos(1160, 540)
                aapo.sleep(3)
                aapo.touchPos(1600, 370)
                aapo.sleep(3)
                aapo.touchPos(1928, 740)
                aapo.touchPos(1928, 740)
                # aapo.touchImg(imgpath + "chosen.png")

        aapo.sleep(3)

if __name__ == '__main__':
    main()
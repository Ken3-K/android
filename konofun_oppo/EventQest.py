# This Python file uses the following encoding: utf-8
# pip install android-auto-play-opencv
import android_auto_play_opencv as am
import subprocess
from random import random

# adbpath = 'C:\\Users\\higik\\OneDrive\\ドキュメント\\platform-tools\\'
adbpath = "/Users/kenzaburo/Library/Android/sdk/platform-tools/"
imgpath = "konofun_oppo/img/"
def main():
    aapo = am.AapoManager(adbpath)
    aapo.touchPos(750 + (round((random() - 0.5) * 10, 3)), 1020 + (round((random() - 0.5) * 10, 3))) # tap quest
    aapo.sleep(2)
    aapo.touchPos(1560 + (round((random() - 0.5) * 10, 3)), 400 + (round((random() - 0.5) * 10, 3))) # tap event
    aapo.sleep(3)
    aapo.touchPos(1450 + (round((random() - 0.5) * 10, 3)), 360 + (round((random() - 0.5) * 10, 3))) # tap quest
    aapo.sleep(3)
    aapo.touchPos(1600 + (round((random() - 0.5) * 10, 3)), 340 + (round((random() - 0.5) * 10, 3))) # select normal 12
    aapo.sleep(2)
    aapo.touchPos(1820 + (round((random() - 0.5) * 10, 3)), 840 + (round((random() - 0.5) * 10, 3))) # 挑戦準備
    aapo.sleep(2)
    aapo.touchPos(1850 + (round((random() - 0.5) * 10, 3)), 1000 + (round((random() - 0.5) * 10, 3))) # 挑戦する
    while True:
        aapo.sleep(round(random(), 2) +30)
        while True:
            aapo.screencap()
            if aapo.touchImg(imgpath + "next.png"):
                break
            else:
                aapo.touchPos(1000 + (round((random() - 0.5) * 10, 3)), 870 + (round((random() - 0.5) * 10, 3))) # わきみち対策
                aapo.sleep(round(random(), 2) +1)
        aapo.sleep(round(random(), 2) +2.5)
        aapo.touchPos(1200 + (round((random() - 0.5) * 10, 3)), 970 + (round((random() - 0.5) * 10, 3))) # 再選する
        aapo.sleep(round(random(), 2) +1)
        aapo.touchPos(1400 + (round((random() - 0.5) * 10, 3)), 740 + (round((random() - 0.5) * 10, 3))) # OK
        aapo.sleep(round(random(), 2) +1)
        aapo.touchPos(1200 + (round((random() - 0.5) * 10, 3)), 970 + (round((random() - 0.5) * 10, 3))) # 念のためもう一回　再戦する
        aapo.sleep(round(random(), 2) +1)
        aapo.touchPos(1400 + (round((random() - 0.5) * 10, 3)), 740 + (round((random() - 0.5) * 10, 3))) # OK
        aapo.sleep(round(random(), 2) +1) 

# 1000 870

if __name__ == '__main__':
    main()
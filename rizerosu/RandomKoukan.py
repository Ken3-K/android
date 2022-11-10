# ランダム交換所のコード
# 20ステップ以降はうまくいかない

import android_auto_play_opencv as am
import subprocess
from random import random
import os

if os.name == 'nt':
    adbpath = 'C:\\Users\\higik\\OneDrive\\ドキュメント\\platform-tools\\'
elif os.name == 'posix':
    adbpath = "/Users/kenzaburo/Library/Android/sdk/platform-tools/"
imgpath = "rizerosu/img/"
aapo = am.AapoManager(adbpath)

def TouchRandomPos(x, y, xcoef=20, ycoef=20):
    dx = (random() - 0.5) * xcoef
    dy = (random() - 0.5) * ycoef
    aapo.touchPos(x + dx, y + dy)

def RandomSleep(time):
    dt = (random() - 0.5) * 1
    aapo.sleep(time + dt)

def main():
    while True:
        TouchRandomPos(500, 2000)  # まとめて引く
        RandomSleep(2)
        TouchRandomPos(500, 1850)  # 閉じる
        RandomSleep(3)
        TouchRandomPos(700, 480)  # 次ステップへ
        RandomSleep(1)
        TouchRandomPos(700, 1300)  # 
        RandomSleep(3)

if __name__ == "__main__":
    main()

# This Python file uses the following encoding: utf-8
# pip install android-auto-play-opencv
import android_auto_play_opencv as am
import subprocess
from random import random
from subprocess import check_output
import os

if os.name == 'nt':
    adbpath = 'C:\\Users\\higik\\OneDrive\\ドキュメント\\platform-tools\\'
elif os.name == 'posix':
    adbpath = "/Users/kenzaburo/Library/Android/sdk/platform-tools/"
imgpath = "konofun_oppo/img/"
aapo = am.AapoManager(adbpath)

def TouchRandomPos(x, y, xcoef=20, ycoef=20):
    dx = (random() - 0.5) * xcoef
    dy = (random() - 0.5) * ycoef
    aapo.touchPos(x + dx, y + dy)

def RandomSleep(time):
    dt = (random() - 0.5) * 1
    aapo.sleep(time + dt)

def main():
    ntimes = 20
    # ntimes = int(input("何回やるか: "))
    n = 0
    while n < ntimes:
        n += 1
        print(f"{n}回目スタート！")
        # subprocess.run(f"say -v Samantha '{n} times loop is now started!'", shell=True)
        while True:
            aapo.screencap()
            if aapo.chkImg(imgpath+"chosen.png"):
                TouchRandomPos(2200, 600) # ストーリー解放対策
                RandomSleep(2)
                aapo.touchImg(imgpath+"chosen.png")
                break
            else:
                aapo.touchImg(imgpath+"next.png") # なんか間違って処理が進んだ時用
                TouchRandomPos(2200, 600) # ストーリー解放対策
                RandomSleep(4)
        RandomSleep(4)
        TouchRandomPos(1850, 1000) # 挑戦する
        RandomSleep(40)
        while True:
            aapo.screencap()
            if aapo.touchImg(imgpath+"next.png"):
                RandomSleep(4)
                TouchRandomPos(1600, 980) # 次へ
                RandomSleep(7)
                break
            RandomSleep(4)



if __name__ == '__main__':
    main()
    subprocess.run("say -v Samantha 'Loop is now finished!'", shell=True)

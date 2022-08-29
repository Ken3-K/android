# This Python file uses the following encoding: utf-8
# pip install android-auto-play-opencv
import android_auto_play_opencv as am
import subprocess
from random import random
from subprocess import check_output

# adbpath = 'C:\\Users\\higik\\OneDrive\\ドキュメント\\platform-tools\\'
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
    while True:
        aapo.screencap()
        if aapo.touchImg(imgpath+"again.png"):
            RandomSleep(2)
            TouchRandomPos(1400, 740)
        aapo.sleep(15)

if __name__ == '__main__':
    main()

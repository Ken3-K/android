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

def hammer():
    TouchRandomPos(700, 1630)
    result = input("continue? : ")
    print(result)
    if not result:
        TouchRandomPos(350, 1590)
        aapo.sleep(1.5)
        hammer()
    else:
        TouchRandomPos(700, 1600)
        aapo.sleep(1.5)
        TouchRandomPos(350, 1530)
        exit()

def auto():
    TouchRandomPos(700, 1630)
    aapo.sleep(2)
    aapo.screencap()
    while True:
        if aapo.chkImg(imgpath + "overrap.png"):
            break
        aapo.sleep(1.5)
        aapo.screencap()
    if aapo.chkImg(imgpath + "sp_hammer.png") or aapo.chkImg(imgpath + "sp_small.png"):
        subprocess.run("afplay /System/Library/Sounds/Glass.aiff", shell=True)

    else:
        TouchRandomPos(350, 1590)
        aapo.sleep(1.5)
        auto()

if __name__ == "__main__":
    hammer()
    # auto()
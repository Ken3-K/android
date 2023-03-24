# アリーナメダルの交換

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

def change_medal():
    TouchRandomPos(850, 600)
    RandomSleep(1)
    aapo.swipeTouchPos(450, 1350, 900, 1350, 500)
    TouchRandomPos(750, 1550)
    RandomSleep(2)

def main():

    n = 4
    for _ in range(n):
        change_medal()

if __name__ == "__main__":
    main()
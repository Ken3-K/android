# 強者の塔を下から順に進めるコード
# 現在は5階層から先の分を実装

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

def to_quest():
    TouchRandomPos(800, 1350) # from home to quest
    RandomSleep(2)
    while True:
        aapo.screencap()
        if aapo.touchImg(imgpath + "grand-arena.png"): # to grand arena
            RandomSleep(2)
            break
        aapo.sleep(1)

def to_shiren():
    while True:
        aapo.screencap()
        if aapo.touchImg(imgpath + "shiren.png"): # to list
            RandomSleep(2)
            break
        aapo.sleep(1)

def tower_battle():
    TouchRandomPos(500, 2000)
    aapo.sleep(15)

def AfterBattle():
    while True:
        aapo.screencap()
        if aapo.touchImg(imgpath + "ok.png"): # tap OK
            RandomSleep(2)
            aapo.screencap()
            aapo.touchImg(imgpath + "next.png")  # tap 次へ
            aapo.sleep(2)
            break
        else: aapo.sleep(3)


def main():
    n = 13
    start = 0
    for i in range(start, n):
        if i < 4:
            TouchRandomPos(500, 1700 - 300 * i)
        else:
            TouchRandomPos(500, 600)
        RandomSleep(3)
        tower_battle()
        AfterBattle()

if __name__ == "__main__":
    main()
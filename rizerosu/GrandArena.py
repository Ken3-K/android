# グランドアリーナで、一番上の相手を選んで周回するだけのコード

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

def to_grandarena():
    TouchRandomPos(540, 1550) # home to arena
    RandomSleep(1)
    while True:
        aapo.screencap()
        if aapo.touchImg(imgpath + "grand-arena.png"): # to grand arena
            RandomSleep(1)
            break
        aapo.sleep(1)

def to_list():
    while True:
        aapo.screencap()
        if aapo.touchImg(imgpath + "battle-list.png"): # to list
            RandomSleep(1)
            break
        aapo.sleep(1)

def battle():
    while True:
        aapo.screencap()
        if aapo.chkImg(imgpath + "battle.png"):
            TouchRandomPos(860, 600) # 一番上の対戦を選ぶ
            RandomSleep(1)
            break
        aapo.sleep(1)
    aapo.sleep(2)
    aapo.screencap()
    aapo.touchImg(imgpath + "party3.png")
    RandomSleep(1)
    TouchRandomPos(540, 2000) # tap 決定
    while True:
        aapo.screencap()
        if aapo.touchImg(imgpath + "sortie.png"): # 出撃する
            RandomSleep(1)
            break
        aapo.sleep(1)

def AfterBattle():
    while True:
        aapo.screencap()
        if aapo.touchImg(imgpath + "ok.png") or aapo.touchImg(imgpath + "close.png"): # tap OK or 閉じる
            RandomSleep(1)
            TouchRandomPos(540, 1750)# tap 次へ
        else: aapo.sleep(3)


def main():
    n = int(input("何回やりますか："))
    to_grandarena()
    for i in range(1, n):
        to_list()
        battle()
        aapo.sleep(20)
        AfterBattle()

if __name__ == "__main__":
    main()
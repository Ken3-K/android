# イベント用

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


def kakera1():
    # aapo.swipeTouchPos(100, 1000, 100, 150, 500)
    # aapo.sleep(3)
    TouchRandomPos(740, 1260)
    RandomSleep(4)
    skip()

def kakera2():
    TouchRandomPos(740, 1050)
    RandomSleep(4)
    skip()

def bonus1():
    TouchRandomPos(740, 1180)  # ボーナスバトル
    RandomSleep(4)
    skip()

def bonus2():
    TouchRandomPos(550, 1600)  # ボーナスバトル
    RandomSleep(4)
    skip()

def bonus3():
    TouchRandomPos(740, 1600)  # ボーナスバトル
    RandomSleep(4)
    skip()

def kakera3():
    TouchRandomPos(800, 1000)  # ボーナスバトル
    RandomSleep(4)
    skip()

def kakera4():
    TouchRandomPos(200, 1800)  # ボーナスバトル
    RandomSleep(4)
    skip()

def bonus4():
    TouchRandomPos(200, 600)  # ボーナスバトル
    RandomSleep(4)
    skip()

def bonus5():
    TouchRandomPos(200, 1260)  # ボーナスバトル
    RandomSleep(4)
    skip()

def bonus6():
    TouchRandomPos(600, 1050)  # ボーナスバトル
    RandomSleep(4)
    skip()


def shukai():
    # TouchRandomPos(200, 1650)
    # aapo.sleep(3)
    skip(True)
    skip(True)
"""2022/10
# def kakera1():
#     TouchRandomPos(200, 1250)  # かけらバトル
#     RandomSleep(4)
#     skip()

# def kakera2():
#     TouchRandomPos(200, 1650)  # かけらバトル
#     RandomSleep(3)
#     skip()

# def bonus1():
#     TouchRandomPos(600, 1450)  # ボーナスバトル
#     RandomSleep(4)
#     skip()

# def bonus2():
#     TouchRandomPos(400, 1850)  # ボーナスバトル
#     RandomSleep(4)
#     skip()

# def bonus3():
#     aapo.swipeTouchPos(100, 1000, 100, 600, 500)
#     TouchRandomPos(200, 1700)  # ボーナスバトル
#     RandomSleep(4)
#     skip()
#     aapo.swipeTouchPos(100, 600, 100, 1000, 500)
#     aapo.sleep(1)

# def shukai():
#     TouchRandomPos(200, 1050)  # 周回
#     for _ in range(3):
#         RandomSleep(4)
#         TouchRandomPos(500, 1600)  # quest
#         RandomSleep(3)
#         TouchRandomPos(350, 2000)  # skip
#         RandomSleep(1)
#         TouchRandomPos(860, 960)
#         while True:
#             aapo.screencap()
#             if aapo.touchImg(imgpath + "ok.png"):
#                 break
#             aapo.sleep(1)
#         aapo.sleep(23)
#         for i in range(60):
#             aapo.screencap()
#             if aapo.touchImg(imgpath + "next.png"):
#                 break
#             aapo.sleep(1)

"""

def skip(shukai=False):
    if shukai:
        wait = 20
        TouchRandomPos(500, 1600)  # quest
    else:
        wait = 13
        TouchRandomPos(500, 850)  # quest
    RandomSleep(3)
    # 記憶結晶とかイベント用にセットしておいたやつを使う
    # for j in range(1):
    #     TouchRandomPos(1040, 710)
    #     aapo.sleep(3)
    TouchRandomPos(350, 2000)  # skip
    RandomSleep(1)
    TouchRandomPos(860, 960)
    while True:
        aapo.screencap()
        if aapo.touchImg(imgpath + "ok.png"):
            break
        aapo.sleep(1)
    aapo.sleep(wait)
    for i in range(60):
        aapo.screencap()
        if aapo.touchImg(imgpath + "next.png"):
            aapo.sleep(3)
            break
        aapo.sleep(1)


def mission():
    aapo.touchPos(850, 2015)
    aapo.sleep(2)
    aapo.touchPos(800, 2150)
    while True:
        aapo.screencap()
        if aapo.touchImg(imgpath + "ok.png"):
            aapo.sleep(2)
            break
        aapo.sleep(1)
    aapo.touchPos(70, 2200)
    aapo.sleep(2)
    # aapo.swipeTouchPos(100, 600, 100, 1000, 500)
    aapo.sleep(1)

def main():
    mission()

    aapo.swipeTouchPos(100, 1000, 100, 150, 500)
    aapo.sleep(2)

    bonus1()
    bonus2()
    bonus3()

    kakera1()
    kakera2()

    mission()

    aapo.touchPos(200, 1400)
    aapo.sleep(3)

    shukai()


def main2():

    # mission()

    kakera3()
    kakera4()

    mission()

    bonus4()
    bonus5()
    bonus6()

    mission()

    shukai()
    # mission()

if __name__ == "__main__":

    # main()
    # shukai()
    stamina = 10 * 68
    num = int(stamina/200)
    for i in range(num):
        skip(True)
    subprocess.run("afplay /System/Library/Sounds/Glass.aiff", shell=True)
# 
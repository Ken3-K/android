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

def skip(shukai=False):

    # wait = 5
    # TouchRandomPos(500, 750)  # quest
    # aapo.sleep(2)
    # TouchRandomPos(500, 1850)  # quest
    # RandomSleep(3)
    # # 記憶結晶とかイベント用にセットしておいたやつを使う
    # for j in range(1):
    #     TouchRandomPos(1040, 710)
    #     aapo.sleep(3)    
    TouchRandomPos(350, 2000)  # skip
    for i in range(num_play):
        RandomSleep(1)
        aapo.screencap()
        if aapo.chkImg(imgpath + "not_ok.png"):
            aapo.touchPos(330, 1600) # キャンセル
            aapo.sleep(1)
            aapo.touchPos(1000, 2150)
            exit()
        else:
            pass
        TouchRandomPos(860, 960)
        while True:
            aapo.screencap()
            if aapo.touchImg(imgpath + "ok.png"):
                break
            aapo.sleep(1)
        aapo.sleep(wait)
        for i in range(60):
            aapo.screencap()
            if aapo.chkImg(imgpath + "next.png"):
                aapo.touchImg(imgpath + "skip.png")
                # aapo.sleep(4)
                break
            aapo.sleep(1)

def main():
        skip()

def onetime():
    TouchRandomPos(350, 2000)  # skip
    RandomSleep(1)
    aapo.screencap()
    if aapo.chkImg(imgpath + "not_ok.png"):
        aapo.touchPos(330, 1600) # キャンセル
        aapo.sleep(1)
        aapo.touchPos(1000, 2150)
        exit()
    else:
        pass
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
            # aapo.sleep(4)
            break
        aapo.sleep(1)

if __name__ == "__main__":
    one = 0
    if one == 1:
        num_play = 2
        wait = 25
        main()
    else:
        wait = 3
        onetime()
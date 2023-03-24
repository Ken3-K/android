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

def auto(event=False):
    TouchRandomPos(700, 1630)
    aapo.sleep(2)
    aapo.screencap()
    while True:
        if aapo.chkImg(imgpath + "overrap.png"):
            break
        aapo.sleep(1.5)
        aapo.screencap()
    if event==True:
        # if aapo.chkImg(imgpath + result_image2):
        if aapo.chkImg(imgpath + result_image1) or aapo.chkImg(imgpath + result_image2):
            subprocess.run("afplay /System/Library/Sounds/Glass.aiff", shell=True)
            is_continue = input("continue?: ")
            if is_continue == "":
                TouchRandomPos(350, 1590)
                aapo.sleep(1.5)
                auto(event)
            else:
                exit()
    else:
        if aapo.chkImg(imgpath + result_image3):
            subprocess.run("afplay /System/Library/Sounds/Glass.aiff", shell=True)
            # print(aapo.chkImg2(imgpath + result_image4))
            exit()
    TouchRandomPos(350, 1590)
    aapo.sleep(1.5)
    auto(event)

if __name__ == "__main__":

    result_image1 = "sp_hammer.png"
    result_image2 = "sp_small.png" # for event
    result_image3 = "subayasa.png"
    result_image4 = "start_gage.png"

    hammer()
    # auto(event=False)
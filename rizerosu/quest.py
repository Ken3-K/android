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


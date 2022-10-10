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
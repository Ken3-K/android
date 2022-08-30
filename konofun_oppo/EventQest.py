


# This Python file uses the following encoding: utf-8
# pip install android-auto-play-opencv
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
def main():
    aapo = am.AapoManager(adbpath)
    aapo.touchPos(750 + (round((random() - 0.5) * 10, 3)), 1020 + (round((random() - 0.5) * 10, 3))) # tap quest
    aapo.sleep(6)
    aapo.touchPos(1560 + (round((random() - 0.5) * 10, 3)), 400 + (round((random() - 0.5) * 10, 3))) # tap event
    aapo.sleep(5)
    aapo.touchPos(1450 + (round((random() - 0.5) * 10, 3)), 360 + (round((random() - 0.5) * 10, 3))) # tap quest
    aapo.sleep(4)
    aapo.touchPos(1600 + (round((random() - 0.5) * 10, 3)), 340 + (round((random() - 0.5) * 10, 3))) # select normal 12
    aapo.sleep(3)
    aapo.touchPos(1820 + (round((random() - 0.5) * 10, 3)), 840 + (round((random() - 0.5) * 10, 3))) # 挑戦準備
    aapo.sleep(4)
    aapo.touchPos(1850 + (round((random() - 0.5) * 10, 3)), 1000 + (round((random() - 0.5) * 10, 3))) # 挑戦する
    n = 0
    nmax = 30
    while n < nmax:
        n += 1

        # CPU温度の取得。多分10倍されている。
        cpu_temp = check_output("adb shell cat /sys/class/thermal/thermal_zone9/temp", text=True, shell=True)
        cpu_temp = int(cpu_temp)
        print(f"cpu temperature: {cpu_temp/10}°C")
        # ついでにメモリ使用量も出力
        print(check_output('adb shell dumpsys meminfo | grep -e "Used RAM" -e " Free RAM"', shell=True, text=True))
        aapo.sleep(round(random(), 2) +31)
        while True:
            aapo.screencap()
            x = 0
            y = 0
            checkimg, x, y = aapo.chkImg2(imgpath + "next.png")
            if checkimg:
                aapo.touchPos(50 + (round((random()  -0.5) * 10, 3)), 500 + (round((random() - 0.5) * 10, 3))) # わきみち対策
                aapo.sleep(1)
                aapo.touchPos(x, y)
                # aapo.touchImg(imgpath + "next.png")
                break
            # もしスキップ画面にいったら
            elif aapo.touchImg(imgpath + "cancel.png"):
                aapo.sleep(3)
                aapo.touchPos(1600 + (round((random() - 0.5) * 10, 3)), 340 + (round((random() - 0.5) * 10, 3))) # select normal 12
                aapo.sleep(2)
                aapo.touchPos(1820 + (round((random() - 0.5) * 10, 3)), 840 + (round((random() - 0.5) * 10, 3))) # 挑戦準備
                aapo.sleep(3)
                aapo.touchPos(1850 + (round((random() - 0.5) * 10, 3)), 1000 + (round((random() - 0.5) * 10, 3))) # 挑戦する
            else:
                aapo.touchPos(50 + (round((random()  -0.5) * 10, 3)), 500 + (round((random() - 0.5) * 10, 3))) # わきみち対策
                aapo.sleep(round(random(), 2) + 3)
            aapo.sleep(round(random(), 2) +1) 
        aapo.sleep(round(random(), 2) +2.5)
        aapo.touchPos(1200 + (round((random() - 0.5) * 10, 3)), 970 + (round((random() - 0.5) * 10, 3))) # 再選する
        aapo.sleep(round(random(), 2) +1)
        aapo.touchPos(1400 + (round((random() - 0.5) * 10, 3)), 740 + (round((random() - 0.5) * 10, 3))) # OK
        aapo.sleep(round(random(), 2) +1)
        aapo.touchPos(1200 + (round((random() - 0.5) * 10, 3)), 970 + (round((random() - 0.5) * 10, 3))) # 念のためもう一回　再戦する
        aapo.sleep(round(random(), 2) +1)
        aapo.touchPos(1400 + (round((random() - 0.5) * 10, 3)), 740 + (round((random() - 0.5) * 10, 3))) # OK
        aapo.sleep(round(random(), 2) +1) 

# 1000 870

if __name__ == '__main__':
    main()
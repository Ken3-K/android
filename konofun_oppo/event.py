# This Python file uses the following encoding: utf-8
# pip install android-auto-play-opencv
import android_auto_play_opencv as am
from subprocess import check_output
from random import random
import os

if os.name == 'nt':
    adbpath = 'C:\\Users\\higik\\OneDrive\\ドキュメント\\platform-tools\\'
elif os.name == 'posix':
    adbpath = "/Users/kenzaburo/Library/Android/sdk/platform-tools/"
    
imgpath = "konofun_oppo/img/"
def main():
    aapo = am.AapoManager(adbpath)
    aapo.touchPos(750 + (round((random() - 0.5) * 10, 3)), 1020 + (round((random() - 0.5) * 10, 3))) # tap quest
    aapo.sleep(2)
    aapo.touchPos(1560 + (round((random() - 0.5) * 10, 3)), 400 + (round((random() - 0.5) * 10, 3))) # tap event
    aapo.sleep(3)
    aapo.touchPos(1840, 360)
    aapo.sleep(2)
    aapo.touchPos(1160, 540)
    aapo.sleep(3)
    aapo.touchPos(1600, 370)
    aapo.sleep(3)
    for _ in range(6):
        aapo.touchPos(1928, 740)
    while True:
        # 画面キャプチャ
        aapo.screencap()
        # イベントの挑戦準備をおしたら
        if aapo.touchImg(imgpath + "chosen.png"):
            aapo.sleep(2.5)
            # aapo.screencap()
            # aapo.touchImg(imgpath + "enterroom.png")
            aapo.touchPos(1800, 1020)
            # CPU温度の取得。多分10倍されている。
            cpu_temp = check_output("adb shell cat /sys/class/thermal/thermal_zone9/temp", text=True, shell=True)
            cpu_temp = int(cpu_temp)
            # ついでにメモリ使用量も出力
            print(f"cpu temperature: {cpu_temp/10}°C")
            print(check_output('adb shell dumpsys meminfo | grep -e "Used RAM" -e " Free RAM"', shell=True, text=True))
            print("sleep 40 second")
            aapo.sleep(40)
            while True:
                aapo.screencap()
                if aapo.touchImg(imgpath + "next.png"):
                    aapo.sleep(5)
                    # aapo.screencap()
                    # aapo.touchImg(imgpath + "backroom.png")
                    aapo.touchPos(1400, 975)
                    aapo.sleep(1)
                    # aapo.screencap()
                    # aapo.touchImg(imgpath + "ok.png")
                    aapo.touchPos(1400, 740)
                    aapo.sleep(12)
                    aapo.screencap()
                    if aapo.touchImg(imgpath + "boshu.png"):
                        print("sleep 40 second")
                        aapo.sleep(40)
                    # ルームが解散した時
                    elif aapo.touchImg(imgpath + "ok.png"):
                        aapo.sleep(5)
                        aapo.touchPos(1840, 360)
                        aapo.sleep(2)
                        aapo.touchPos(1160, 540)
                        aapo.sleep(3)
                        aapo.touchPos(1600, 370)
                        aapo.sleep(3)
                        aapo.touchPos(1928, 740)
                        aapo.touchPos(1928, 740)
                        # aapo.touchImg(imgpath + "chosen.png")
                        break
                elif aapo.touchImg(imgpath + "backroom.png"):
                    aapo.touchPos(1400, 740)
                    aapo.sleep(12)
                    aapo.screencap()
                    if aapo.touchImg(imgpath + "boshu.png"):
                        print("sleep 40 second")
                        aapo.sleep(40)
                    # ルームが解散した時
                    elif aapo.touchImg(imgpath + "ok.png"):
                        aapo.sleep(5)
                        aapo.touchPos(1840, 360)
                        aapo.sleep(2)
                        aapo.touchPos(1160, 540)
                        aapo.sleep(3)
                        aapo.touchPos(1600, 370)
                        aapo.sleep(3)
                        aapo.touchPos(1928, 740)
                        aapo.touchPos(1928, 740)
                        # aapo.touchImg(imgpath + "chosen.png")
                        break
                aapo.sleep(2)

        aapo.sleep(3)

if __name__ == '__main__':
    main()
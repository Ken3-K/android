# This Python file uses the following encoding: utf-8
# pip install android-auto-play-opencv
import android_auto_play_opencv as am
import subprocess

from cv2 import cornerEigenValsAndVecs

# adbpath = 'C:\\Users\\higik\\OneDrive\\ドキュメント\\platform-tools\\'
adbpath = "/Applications/platform-tools/"
imgpath = "konofun_oppo/img/"
def main():
    aapo = am.AapoManager(adbpath)
    aapo.touchPos(750, 1020) # tap quest
    aapo.sleep(2)
    aapo.touchPos(1600, 750) # arena
    aapo.sleep(3)
    aapo.touchPos(1200, 810) # 挑戦する
    aapo.sleep(3)
    aapo.touchPos(1800, 600) # 上級
    aapo.sleep(2)
    aapo.touchPos(1700, 830) # 挑戦準備
    aapo.sleep(2)
    aapo.touchPos(1900, 1000) # 挑戦する
    while True:
        aapo.sleep(60)
        while True:
            aapo.screencap()
            # if  
            # 再戦のところ考え中
            if aapo.touchImg(imgpath + "next.png"):
                continue
            else:
                aapo.touchPos(1100, 980) # 
                aapo.sleep(1)
        aapo.sleep(2.5)
        aapo.touchPos(1200, 970) # 再選する
        aapo.sleep(1)
        aapo.touchPos(1400, 740) # OK

if __name__ == '__main__':
    main()
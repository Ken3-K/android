# This Python file uses the following encoding: utf-8
# pip install android-auto-play-opencv
import android_auto_play_opencv as am
from subprocess import check_output
# adbpath = 'C:\\Users\\higik\\OneDrive\\ドキュメント\\platform-tools\\'
adbpath = "/Users/kenzaburo/Library/Android/sdk/platform-tools/"
imgpath = "konofun_oppo/img/"

def main():
    aapo = am.AapoManager(adbpath)
    aapo.screencap()
    aapo.imgSave(imgpath + "temp.png")
    # cpu_temp = check_output(["adb", "shell", "cat", "/sys/class/thermal/thermal_zone9/temp"], text=True)
    # cpu_temp = int(cpu_temp)
    # print(cpu_temp/10)
    # while True:
        # 画面キャプチャ
        # aapo.screencap()
        # aapo.imgSave(imgpath + "temp.png")
if __name__ == '__main__':
    main()
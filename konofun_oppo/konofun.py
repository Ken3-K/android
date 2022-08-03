# This Python file uses the following encoding: utf-8
# pip install android-auto-play-opencv
import android_auto_play_opencv as am
import subprocess
# adbpath = 'C:\\Users\\higik\\OneDrive\\ドキュメント\\platform-tools\\'
adbpath = subprocess.check_output(["which", "adb"], text=True)
print(adbpath)
def main():
    aapo = am.AapoManager(adbpath)
    while True:
        # 画面キャプチャ
        aapo.screencap()
        # aapo.touchImg("img/hoge.png")
if __name__ == '__main__':
    main()
# This Python file uses the following encoding: utf-8
# pip install android-auto-play-opencv
import android_auto_play_opencv as am
adbpath = 'C:\\Users\\higik\\OneDrive\\ドキュメント\\platform-tools\\'

def main():
    aapo = am.AapoManager(adbpath)
    aapo.screencap()
    aapo.imgSave("img/free-quest-list.png")
if __name__ == '__main__':
    main()
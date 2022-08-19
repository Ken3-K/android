from re import sub
import subprocess
import time

subprocess.run("adb devices", shell=True)
subprocess.run("adb tcpip 5555", shell=True)
time.sleep(3)
ip = subprocess.check_output("adb shell ip route", shell=True, text=True).split()[-1]
time.sleep(2)
subprocess.run(f"adb connect {ip}:5555", shell=True)
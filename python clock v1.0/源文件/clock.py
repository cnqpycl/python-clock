import os
import pyautogui
import time
from playsound import playsound
from pymouse import PyMouse
m = PyMouse()
def main():
    print(time.localtime())
 
    year = time.localtime().tm_year
    month = time.localtime().tm_mon
    day = time.localtime().tm_mday
 
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min
    second = time.localtime().tm_sec
    print(year, '年', month, '月', day, '日')
    print(hour, '时', minute, '分', second, '秒')
main()
def mic():
    time.sleep(0.5)   
    xy = pyautogui.locateOnScreen('1.png')
    center = pyautogui.center(xy)
    pyautogui.click(center)   
def ring():
    if pyautogui.locateOnScreen('1.png'):
        mic()
        playsound("1.mp3")
        time.sleep(1800)
        playsound("2.mp3")
    else:
        playsound("1.mp3")
        time.sleep(1800)
        playsound("2.mp3")
def timeoff(hour,minute,second):
    if hour == time.localtime().tm_hour and minute == time.localtime().tm_min and second == time.localtime().tm_sec:
        ring()
 
while 1:
    timeoff(8,19,41)
    timeoff(9,9,41)
    timeoff(10,9,41)
    timeoff(13,59,41)
    timeoff(14,59,41)
    timeoff(15,49,41)

os._exit(0)
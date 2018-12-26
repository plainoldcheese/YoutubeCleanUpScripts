#yt clicker
'''
This worked for me on 27 Dec 2018 with 1920x1080p resolution in firefox 64.
Adjust the coordinates (depending on resoultion) and wait times (dependingon internet connection and computer speed)
WARNING: this program runs in a infinite loop, please utlize pyautoguis FAILSAFE by dragging mouse to top left cornerof screen to quit
'''
import pyautogui
import time

count = 0
while True:
    count += 1
    pyautogui.click(1839, 344) #coordinate of delete item button
    time.sleep(0.1)
    print('clicked {} times'.format(count))
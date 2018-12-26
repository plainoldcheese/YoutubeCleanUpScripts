#yt unsubscriber 
'''
This worked for me on 27 Dec 2018 with 1920x1080p resolution in firefox 64.
Adjust the coordinates (depending on resoultion) and wait times (dependingon internet connection and computer speed)
'''
import pyautogui
import time
import webbrowser
webbrowser.open('https://www.youtube.com/subscription_manager')
#initial position of unsubscribe button
x= 1450 
y= 334
#position of unsubscribe dialog button
x_d=1011
y_d=581
down = 57
count = 0
while True:
    for j in range(4):
        for i in range(12):
            pyautogui.click(x, y, interval=0.4)
            time.sleep(0.3)
            pyautogui.click(x_d, y_d, interval=0.4)
            time.sleep(0.3)
            y += down
        # reset y
        y= 334
        pyautogui.press('pagedown')
        time.sleep(0.2)
    webbrowser.open('https://www.youtube.com/subscription_manager') #its easier than trying to click next 
    time.sleep(12)

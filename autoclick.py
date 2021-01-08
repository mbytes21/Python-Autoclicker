import time
import pynput

from time import sleep
from pynput import mouse
from pynput.mouse import Button, Controller

mouse = Controller()

delay1 = input("How long until the clicking starts? ")

clicknum = int(input("How many times do you want it to click? "))

x=int(delay1)

for i in range(x):
    sleep(1)
    

mouse.click(Button.left, clicknum)
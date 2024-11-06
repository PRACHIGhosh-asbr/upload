
import random

#@pyhthon.coder_

import pyautogui as pg

import time

animal=('my', 'love')


time.sleep(9)

for i in range(10):
  a=random.choice(animal)
  pg.write('You are ' +a)
  pg.press('enter')

import time
import sys
import random
from psychopy import visual,event,core


names = open('names.txt', 'r').readlines()
lastNames = [name.split(' ')[1] for name in names]
firstNames = [name.split(' ')[0] for name in names]
"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	

win = visual.Window([800,600],color="black", units='pix')
NameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
fixCross = visual.TextStim(win, text="+", height=40, color="white", pos=[0,0])
while True:
    fixCross.draw()
    win.flip()
    core.wait(.5)
    nameShown = random.choice(lastNames+firstNames)
    if nameShown in firstNames:
        NameStim.setText(nameShown)
    if nameShown in lastNames:
        NameStim.setText(nameShown[:-1])
    NameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)

    if event.getKeys(['q']):
        break
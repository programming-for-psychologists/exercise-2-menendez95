import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
lastNames = [name.split(' ')[1] for name in names]
firstNames = [name.split(' ')[0] for name in names]


userVar = {'Name':'Enter your name'}
dlg = gui.DlgFromDict(userVar)

def popupError(text):
    errorDlg = gui.Dlg(title="Error", pos=(200,400))
    errorDlg.addText('Error: '+text, color='Red')
    errorDlg.show()



win = visual.Window([800,600],color="black", units='pix')
NameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
fixCross = visual.TextStim(win, text="+", height=40, color="white", pos=[0,0])
correct = visual.TextStim(win,text="O", height=40, color="green",pos=[0,0])
incorrect = visual.TextStim(win,text="X", height=40, color="red",pos=[0,0])

if userVar['Name'] not in firstNames:
    popupError('There was an error!')
else:
    while True:
        fixCross.draw()
        win.flip()
        core.wait(.5)
        nameShown = random.choice(lastNames+firstNames)
        if nameShown in firstNames:
            NameStim.setText(nameShown)
            NameStim.draw()
            win.flip()
            correctResponse = ['f']
        if nameShown in lastNames:
            NameStim.setText(nameShown[:-1])
            NameStim.draw()
            win.flip()
            correctResponse = ['l']
        response = event.waitKeys(keyList=['f', 'l', 'space'], maxWait=1)
        if nameShown == userVar['Name']:
            correctResponse = ['space']

        if correctResponse == response:
            correct.draw()
            win.flip()
            core.wait(.5)
        elif correctResponse != response:
            incorrect.draw()
            win.flip()
            core.wait(.5)
        
        core.wait(.75)
        win.flip()
        core.wait(.15)

        if event.getKeys(['q']):
            break
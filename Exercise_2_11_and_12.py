import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
lastNames = [name.split(' ')[1] for name in names]
firstNames = [name.split(' ')[0] for name in names]

SubID = {'SubID':'Participant number'}
sub = gui.DlgFromDict(SubID)

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
timer = core.Clock()


output = open('output.txt', 'w')
output.write('SubID\ttrail\tname\town\tcorrect\tRT\n') #creating variable names

i=1
if userVar['Name'] not in firstNames: #subjects cannot enter a name that is not in the list
    popupError('There was an error!')
else:
    while i < 34: #Subjects will only have 34 trails
        output.write(SubID['SubID']+'\t')
        output.write(str(i)+'\t')
        fixCross.draw()
        win.flip()
        core.wait(.5)
        allNames = lastNames+firstNames
        nameShown = random.choice(allNames+[userVar['Name']]*((len(allNames)/4)-1)) #making the typed name appear 1/4 of the trials
        if nameShown in firstNames:
            output.write('first\t')
            NameStim.setText(nameShown)
            NameStim.draw()
            win.flip()
            timer.reset(newT=0.0)
            correctResponse = ['f']
        if nameShown in lastNames:
            output.write('last\t')
            NameStim.setText(nameShown[:-1])
            NameStim.draw()
            win.flip()
            timer.reset(newT=0.0)
            correctResponse = ['l']
        response = event.waitKeys(keyList=['f', 'l', 'space'], maxWait=1)
        if nameShown == userVar['Name']:
            correctResponse = ['space']
            output.write('1\t')
        else:
            output.write('0\t')

        if correctResponse == response:
            output.write('1\t')
            output.write(str(timer.getTime()*1000)+'\n')
            correct.draw()
            win.flip()
            core.wait(.5)
        elif correctResponse != response:
            output.write('0\t')
            output.write(str(timer.getTime()*1000)+'\n')
            incorrect.draw()
            win.flip()
            core.wait(.5)
        
        core.wait(.75)
        win.flip()
        core.wait(.15)
        i= i+1

        if event.getKeys(['q']):
            break
output.close()
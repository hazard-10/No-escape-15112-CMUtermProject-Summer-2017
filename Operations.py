import math
from SetTheme import *

def mainOperation(data,event):
    x,y=event.x,event.y
    if(x<700 and x>500 and y<450 and y >350):
        data.main=False
        data.set=True 
    elif(x<700 and x>500 and y<600 and y >500):
        data.main=False
        data.help=True  
    else: 
        data.MainSwitch=True 
#        data.isGameOver=False 
def gamePress(data,event):
    if(event.keysym=='space'):
        print('pass')
        data.gameStart=True
    # use event.char and event.keysym
    if(event.char=='p' and data.pause==False):  
        data.pause=True
    elif(event.char=='p' and data.pause==True):  
        data.pause=False 
    elif((event.keysym=='Right') and data.pause!= True):
    
        for i in range(2):
            data.color[2][i]=[data.color[2][i][len(data.color[2][i])-1]]+data.color[2][i][0:len(data.color[2][i])-1]
        for i in range (len(data.indexes)):
            for j in range(2):
                data.indexes[i][j]+=1
        for i in data.xy: 
            i[1]-=math.pi/6
    elif((event.keysym=='Left') and data.pause!= True):
        for i in range (len(data.indexes)):
            for j in range(2):
                data.indexes[i][j]-=1
        for i in data.xy: 
            i[1]+=math.pi/6
    
        for i in range(2):
            data.color[2][i]=data.color[2][i][1:]+[data.color[2][i][0]]
            '''
    for i in range(2):
        data.color[2][i]=data.color[2][i][data.colorindex:]+data.color[2][i][:data.colorindex] 
        print(len(data.color[2][i]))
    print(data.color[2][1])
    print(data.colorindex)
    '''
def setOperation(data,event):
    
    x,y=event.x,event.y
    if(x>0 and x<200 and y>0 and y<100):
        data.set=False
        data.main=True
    elif(x>500 and x<700 and y>525 and y<575):
        data.color=data.color=allThemes()[2]
    elif(x>800 and x<1000 and y>525 and y<575):
        data.color=data.color=allThemes()[3]
    elif(x>500 and x<700 and y>575 and y<625):
        data.color=data.color=allThemes()[0]
    elif(x>800 and x<1000 and y>575 and y<625):
        data.color=data.color=allThemes()[1]
    elif(x>550 and x<650 and y>375 and y<425):
        data.level=1
    elif(x>850 and x<950 and y>375 and y<425):
        data.level=2
 
def helpOperation(data,event):
    x,y=event.x,event.y
    if(x>0 and x<200 and y>0 and y<100):
        data.help=False
        data.main=True
    

def pauseOperation(data,event):    
    x,y=event.x,event.y
    if(x>50 and x<150 and y>25 and y<75):
        data.MainSwitch=False
        data.initCount=0
        data.main=True
        data.pause=False    
        data.alpha=1
        data.gameStart=False
        data.MainSwitch=False
        data.score=0
        data.isGameOver=False
        data.timeCounter=0  
        data.colorindex=0
def overOperation(data,event):    
    x,y=event.x,event.y
    if(x>50 and x<150 and y>25 and y<75):
#        data.MainSwitch=False
        data.MainSwitch=False
        data.initCount=0
        data.main=True
        data.pause=False
        data.isGameOver=False
        data.gameStart=False
        data.alpha=1
        data.score=0
        data.timeCounter=0
        data.colorindex=0
        data.colorindex=0
# I used barebones to complete this work
# Barebones timer, mouse, and keyboard events

from tkinter import *

from DrawTunnel import *
from DrawObstacle import *
from DrawInterface import *
from Operations import *
from SetTheme import *

import math
import random
import copy
# MODEL VIEW CONTROLLER (MVC)
####################################
# MODEL:       the data
# VIEW:        redrawAll and its helper functions
# CONTROLLER:  event-handling functions and their helper functions
####################################


####################################
# customize these functions
####################################


# Initialize the data which will be used to draw on the screen.
def init(data):
    # load data as appropriate 
    data.width=1200
    data.v=50
    data.height=800
    data.dots=[[1200,400], 
    [1000,800],
    [200,800],
    [0,400],
    [0,400-600*math.tan(math.pi*2*(25/360))],
    [200,0],\
    [600-400/math.tan(math.pi*2*(63/360)),0],\
    [600-400/math.tan(math.pi*2*(81/360)),0],\
    [600+400/math.tan(math.pi*2*(81/360)),0],\
    [600+400/math.tan(math.pi*2*(63/360)),0],\
    [1000,0], \
    [1200,400-600*math.tan(math.pi*2*(25/360))]] # L1.angle= 25 #L2.angle=45
    data.moveDotsmainL=[[0,400],[600-300,400],[600-150,400],[600-75,400],[600-37.5,400],[600-37.5/2,400],[600-37.5/4,400]]
    data.moveDotsmainR=[[1200,400],[600+300,400],[600+150,400],[600+75,400],[600+37.5,400],[600+37.5/2,400],[600+37.5/4,400]]
    data.tempML=[]
    data.tempMR=[]  
    data.tempL1,data.tempL8=[],[]
    data.tempL2,data.tempL7=[],[]
    data.tempL3,data.tempL6=[],[] 
    data.tempL4,data.tempL5=[],[]  
    data.allDots=[data.moveDotsmainR,data.tempMR,data.tempML,data.moveDotsmainL,data.tempL1,data.tempL2,data.tempL3,data.tempL4,data.tempL5,data.tempL6,data.tempL7,data.tempL8]
    data.allAngels=[60,30,0,-30,-60,-90,-120,-150,-180,150,120,90] 
    data.smallPoint=0
    data.timeCounter=0
    data.allObstacles=[]    
    data.numList7=[0,1,2,3,4,5,6]
    data.ranflag=1  #obs2
    data.indexes=[]
    data.score=0
    data.alpha=1
    data.color=allThemes()[0]
    data.colorindex=0
    data.xy=[]
    data.level=1
    for i in range(500):
        length=random.randint(0,720)
        angel=random.uniform(0,2*math.pi)
        data.xy.append([length,angel])
    for i in range(7):
        n1,n2,n3=random.randint(0,11),random.randint(0,11),random.randint(0,11)
        data.indexes.append([n1,n2])  
    
    data.initCount=0
    data.MainSwitch=False
    
    data.main=True
    data.set=False
    data.help=False
    
    data.gameStart=False 
    data.isGameOver=False
    data.pause=False
    data.flags=[0 for i in range (7)]
# These are the CONTROLLERs.
# IMPORTANT: CONTROLLER does *not* draw at all!
# It only modifies data according to the events.
def mousePressed(event, data):
    if(data.MainSwitch==False):
    # use event.x and event.y
        if(data.main==True):
            mainOperation(data,event)
            pass
        elif(data.help==True):
            helpOperation(data,event)
        elif(data.set==True):
            setOperation(data,event)
    else:
        if(data.pause==True):
            pauseOperation(data,event)
        elif(data.isGameOver==True):
            overOperation(data,event)
def keyPressed(event, data):
    if(data.MainSwitch==True):
        gamePress(data,event)
        if(event.char=='r'):
            temp=copy.deepcopy(data.color)
            init(data)    
            data.color=temp
            data.main=False 
            data.MainSwitch=True
        if(data.isGameOver==True):
            overOperation(data,event)
        
def timerFired(data):
    for i in data.xy: 
        i[1]-=math.pi/300 #stars
        
    if(data.pause==True): 
        pass
    else:
        data.obsFlag=False
        data.root.attributes("-alpha",data.alpha)
        if(data.MainSwitch==True and data.pause==False):
            data.alpha=0.7
            data.initCount+=1 
            if(data.initCount>110):
                data.alpha=1
                data.gameStart=True

            
        for dot in data.moveDotsmainL:
            dot[0]-=(600-dot[0])/(10-(data.level-1)*4)
        for i in range(len(data.moveDotsmainL)): 
            if(data.moveDotsmainL[i][0]<-500):
                data.moveDotsmainL.pop(i)
                data.moveDotsmainL.insert(i,[600-37.5/4,400])  

                
        for dot in data.moveDotsmainR:
            dot[0]+=(dot[0]-600)/(10-(data.level-1)*4)
        for i in range(len(data.moveDotsmainL)): 
            if(data.moveDotsmainR[i][0]>1700):
                data.moveDotsmainR.pop(i)
                data.moveDotsmainR.insert(i,[600+37.5/4,400])
                reset1(data)
                data.smallPoint+=1  
        if(data.gameStart==True):
            data.timeCounter+=1 

def reset1(data):
    data.ranflag= random.randint(0,3)
    a=data.indexes.pop(data.smallPoint%7)
    b=data.flags.pop(data.smallPoint%7)
    if(data.gameStart==True):
        for i in range(len(a)):
            if((((a[i]==2 or (b==1 and i==8))and data.level==2)  or (a[0]==2 and data.level==1)) and data.gameStart==True): 
                data.isGameOver=True
                data.gameStart=False
    n1,n2=random.randint(0,11),random.randint(0,11)
    if(data.ranflag==1):
        n2=n1
    data.indexes.insert(data.smallPoint%7,[n1,n2]) 
    data.flags.insert(data.smallPoint%7,data.ranflag)
    data.numList7.remove(data.smallPoint%7)
    data.numList7=[data.smallPoint%7]+data.numList7
    

# This is the VIEW
# IMPORTANT: VIEW does *not* modify data at all!
# It only draws on the canvas.



def redrawAll(canvas, data):
    drawBack(data,canvas)
    if(data.MainSwitch==False):
        if(data.main==True):   
            drawTunnel(data,canvas) 
            drawObstacle1(canvas,data) 
            drawMain(data,canvas)
        elif(data.set==True):
            drawSet(data,canvas)    
        elif(data.help==True):
            drawHelp(data,canvas)
    else: 
        if(data.isGameOver==True): 
            drawOver(data,canvas)
        else:
            drawTunnel(data,canvas) 
            drawObstacle1(canvas,data)  
            drawInit(data,canvas)
            drawScore(data,canvas)
            if(data.pause==True):
                drawPause(data,canvas)
            
            
#    canvas.create_rectangle(0,0,1200,800,fill='black')
#    drawTunnel(data,canvas)
#    if(data.gameStart==True and data.isGameOver==False): 
#        drawObstacle(canvas,data)

            

####################################
####################################
# use the run function as-is
####################################
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
        
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 10# milliseconds
    data.alpha=1
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    data.root = root
    # set up events
    data.root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    data.root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data) #data.alpha) 
    # and launch the app
    data.root.mainloop()  # blocks until window is closed
    print("bye!")

run(1200, 800)

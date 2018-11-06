#from DrawTunnel import *
import math
import random
def colorful():
    color=['red','orange','yellow','green','blue','purple','grey','snow','cyan','magenta']
    i = random.randint(0,9)
    return color[i]
    

def drawMain(data,canvas):

#    canvas.create_rectangle(0,0,1200,800,fill='black')    
#    canvas.create_rectangle(350,200,850,300,fill=data.color[0])
    canvas.create_text(600,250,text='NO ESCAPE',font="Times 86 bold",fill=colorful())
    
#    canvas.create_rectangle(500,350,700,450,fill=data.color[0])
    canvas.create_text(600,400,text='options',font="Times 36 bold",fill=colorful())
    
#    canvas.create_rectangle(500,500,700,600,fill=data.color[0])
    canvas.create_text(600,550,text='help',font="Times 36 bold",fill=colorful()) 
    
    canvas.create_text(600,750,text='click anywhere to start!',font="Times 16 bold",fill=colorful()) 
    
def drawBack(data,canvas):
    canvas.create_rectangle(0,0,1200,800,fill=data.color[0])
    if(data.color[0]=='black'):
        for i in data.xy:
            length=i[0]
            angel=i[1]
            x=length*math.cos(angel)+600
            y=length*math.sin(angel)+400
            
            canvas.create_oval(x-1.3,y-1.3,x+1.3,y+1.3,fill='white')

def drawSet(data,canvas):

    canvas.create_text(600,250,text='OPTIONS',font="Times 76 bold",fill=data.color[1])
    canvas.create_text(300,400,text='difficulty',font="Times 56 bold",fill=data.color[1])
    canvas.create_text(300,550,text='theme',font="Times 56 bold",fill=data.color[1]) 
    
#    canvas.create_rectangle(550,375,650,425,outline='white',fill=data.color[0])
    canvas.create_text(600,400,text='easy',font="Times 36 bold",fill=data.color[1]) 
    
#    canvas.create_rectangle(850,375,950,425,outline='white',fill=data.color[0])
    canvas.create_text(900,400,text='hard',font="Times 36 bold",fill=data.color[1])
    
#    canvas.create_rectangle(500,525,700,575,outline='white',fill=data.color[0])
    canvas.create_text(600,550,text='Spider Man',font="Times 36 bold",fill=data.color[1])
     
#    canvas.create_rectangle(800,525,1000,575,outline='white',fill=data.color[0])
    canvas.create_text(900,550,text='Iron Man',font="Times 36 bold",fill=data.color[1]) 
    
#    canvas.create_rectangle(500,575,700,625,outline='white',fill=data.color[0])
    canvas.create_text(600,600,text='night',font="Times 36 bold",fill=data.color[1])
    
#    canvas.create_rectangle(800,575,1000,625,outline='white',fill=data.color[0])
    canvas.create_text(900,600,text='Disco',font="Times 36 bold",fill=data.color[1]) 
    
    
    canvas.create_text(100,50,text='<---',font="Times 56 bold",fill=data.color[1]) 
    

def drawPause(data,canvas):
#    canvas.create_rectangle(250,150,950,650,fill=data.color[0])
    canvas.create_text(600,250,text='PAUSED',font="Times 76 bold",fill=data.color[1])
    canvas.create_text(600,450,text='press r to restart',font="Times 36 bold",fill=data.color[1])
    canvas.create_text(600,550,text='press p to continue',font="Times 36 bold",fill=data.color[1])  

#    canvas.create_rectangle(50,25,150,75,fill=data.color[0])  
    canvas.create_text(100,50,text='<---',font="Times 56 bold",fill=data.color[1]) 
    
def drawInit(data,canvas):
    if(data.initCount<99):
        
#        canvas.create_rectangle(550,75,650,125,fill=data.color[0])
        canvas.create_text(600,100,text=str(3-data.initCount//30),font="Times 36 bold",fill=data.color[1])
    elif(data.initCount<110 and data.initCount>89):
        
#        canvas.create_rectangle(550,75,650,125,fill=data.color[0])
        canvas.create_text(600,100,text='GO!!!',font="Times 36 bold",fill=data.color[1]) 
    elif(data.initCount>110):
        data.gameStart=True

def drawHelp(data,canvas):
    canvas.create_text(100,50,text='<---',font="Times 56 bold",fill=data.color[1]) 

    canvas.create_text(600,400,text='Press <-- or--> to move \n\n\npress p to pause \n\n\npress r to restart',font="Times 36 bold",fill=data.color[1]) 
    
def drawOver(data,canvas):
    canvas.create_text(600,350,text='Game Over',font="Times 66 bold",fill=data.color[1])
    canvas.create_text(600,450,text='Your score is  '+str(data.score),font="Times 46 bold",fill=data.color[1])
    canvas.create_text(600,550,text='press r to restart',font="Times 36 bold",fill=data.color[1])
#    canvas.create_rectangle(50,25,150,75,fill=data.color[0])  
    canvas.create_text(100,50,text='<---',font="Times 56 bold",fill=data.color[1]) 
    
def drawScore(data,canvas):
    color='black'
    if(data.color[0]=='black'):
        color='white'
    data.score=data.timeCounter
    canvas.create_text(1175,25,text=str(data.timeCounter),anchor='ne',font="Helvetica 36 bold",fill=color) 
        
    
    
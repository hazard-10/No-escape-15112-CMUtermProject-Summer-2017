##this is obstacle
import math 
import random

class Obstacle1(object):
    def __init__(self,point1,point2,angel1,angel2,length,data):
        self.point1=point1
        self.point2=point2
        self.angel1=angel1
        self.angel2=angel2
        
        self.length=length
        angel3=angel1+angel2
        self.point3=[self.point2[0]+self.length*math.cos(2*math.pi*(angel3/360)),self.point2[1]-self.length*math.sin(2*math.pi*(angel3/360))]
        self.point4=[self.point1[0]+self.point3[0]-self.point2[0],self.point1[1]+self.point3[1]-self.point2[1]]

class Obstacle2(object):
    def __init__(self,index,n,data):
        self.point1=data.allDots[index-1][n]
        self.point2=data.allDots[index][n]
        self.point3=data.allDots[(index-1+6)%12][n]
        self.point4=data.allDots[(index+6)%12][n]
        
        
def makeObstacle1(data):
    data.allObstacles=[]
    for i in data.numList7: 
        for j in range(data.level):
            index=(data.indexes[i][j]+24)%12
            p1=data.allDots[index-1][i]
            p2=data.allDots[index][i]
            angel1=data.allAngels[index]
            angel2=90
            length=data.tempMR[i][0]-data.tempML[i][0]
            if(data.indexes[i][0]==data.indexes[i][1] and data.level==2):
                a=Obstacle2(index,i,data) 
            else:
                a=Obstacle1(p1,p2,angel1,angel2,length,data) 
            data.allObstacles.append(a)
def drawObstacle1(canvas,data):
    makeObstacle1(data)
    for i in data.allObstacles:
        if(data.color[1]=='black'): 
            canvas.create_polygon(i.point1[0],i.point1[1],i.point2[0],i.point2[1],i.point3[0],i.point3[1],i.point4[0],i.point4[1],fill=colorful(),width=3,outline='black')
        else:
            canvas.create_polygon(i.point1[0],i.point1[1],i.point2[0],i.point2[1],i.point3[0],i.point3[1],i.point4[0],i.point4[1],fill=data.color[1],width=3,outline='black')
        
        
def colorful():
    color=['red','orange','yellow','green','blue','purple','grey','snow','cyan','magenta']
    i = random.randint(0,9)
    return color[i]
    
def makeObstacle2(data):
    data.index=[]
    space=[None for i in range (9)]
    for i in range(7):
        data.index.append((data.obstacle2_s+i)%11)
    data.index=space+data.index+space 
    for i in range(7):
        data.index.append((data.obstacle2_m+i)%11)
    data.index+=space 
    
    point=data.smallPoint%7  
    pos=[]
    for i in range(7):
        pos=[point+i]+pos
    data.allObstacles1index=[]
    data.allObstacles1index=data.index[data.obstacleCount-7:data.obstacleCount-7+7]
    print(data.allObstacles1index)
    
    for i in range(7):
        if(data.allObstacles1index[i]!=None):
            index=data.allObstacles1index[i]
            p1=data.allDots[index-1][i]
            p2=data.allDots[index][i]
            angel1=data.allAngels[index]
            angel2=90
            
            j=pos[i]%7
            length=data.tempMR[j][0]-data.tempML[j][0]
            b=Obstacle1(p1,p2,angel1,angel2,length) 
            data.allObstacles2.append(b)
            
        
# fail to draw 'snake like ' obstacle so these two functions are obsolete
def drawObstacle2(canvas,data):
    makeObstacle2(data)
    for i in data.allObstacles2:
        if(data.color[1]=='black'): 
            canvas.create_polygon(i.point1[0],i.point1[1],i.point2[0],i.point2[1],i.point3[0],i.point3[1],i.point4[0],i.point4[1],fill=colorful(),width=3,outline='black')
        else:
            canvas.create_polygon(i.point1[0],i.point1[1],i.point2[0],i.point2[1],i.point3[0],i.point3[1],i.point4[0],i.point4[1],fill=data.color[1],width=3,outline='black')
        
    
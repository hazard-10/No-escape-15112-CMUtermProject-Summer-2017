import math

def drawTunnel(data,canvas):

        
    for i in range(len(data.dots)):
        canvas.create_line(600,400,data.dots[i],data.dots[i],width=4,fill=data.color[2][0][i]) #[0][i]))
    
    # main line
#    canvas.create_line(0,data.height/2,data.width,data.height/2,width=4)#,fill='white')
    # draw in canvas   2*math.pi*(105/360)
    
    # tow lines down
    data.tempML=[]
    data.tempMR=[]
    for dot in data.moveDotsmainL: 
        length=(600-dot[0])/math.sin(2*math.pi*(105/360))*math.sin(2*math.pi*(45/360))
        ax,ay=dot[0],dot[1] 
        ax1,ay1=ax+math.cos(math.pi/6)*length,    ay+math.sin(math.pi/6)*length 
        canvas.create_line(ax,ay,ax1,ay1,width=3,fill=data.color[2][1][2]) #2
        data.tempML.append([ax1,ay1]) 
    for dot in data.moveDotsmainR: 
        length=(dot[0]-600)/math.sin(2*math.pi*(105/360))*math.sin(2*math.pi*(45/360))
        bx,by=dot[0],dot[1] 
        bx1,by1=bx+math.cos(math.pi/6*5)*length,    by+math.sin(math.pi/6*5)*length 
        canvas.create_line(bx,by,bx1,by1,width=3,fill=data.color[2][1][0]) #0
        data.tempMR.append([bx1,by1]) 
        
        
    #line 1 and line 8    
    data.tempL1,data.tempL8=[],[]
    for dot in data.moveDotsmainL: 
        length=(600-dot[0])/(math.sin(math.pi*2*(35/360)))*(math.sin(math.pi*2*(25/360)))
        x,y=dot[0],dot[1]
        x1,y1=x-math.cos(2*math.pi/6)*length, y-math.sin(2*math.pi/6)*length
        canvas.create_line(x,y,x1,y1,width=3,fill=data.color[2][1][3])#3
        data.tempL1.append([x1,y1])
        
    for dot in data.moveDotsmainR: 
        length=(dot[0]-600)/(math.sin(math.pi*2*(35/360)))*(math.sin(math.pi*2*(25/360)))
        x,y=dot[0],dot[1]
        x1,y1=x+math.cos(2*math.pi/6)*length, y-math.sin(2*math.pi/6)*length
        canvas.create_line(x,y,x1,y1,width=3,fill=data.color[2][1][11])#11
        data.tempL8.append([x1,y1])
        
    #line 2 and line 7
    data.tempL2,data.tempL7=[],[]
    for dot in data.tempL1:  
        x,y=dot[0],dot[1]
        x1,y1=x, 400-(600-x)
        canvas.create_line(x,y,x1,y1,width=3,fill=data.color[2][1][4])#4
        data.tempL2.append([x1,y1])
        
    for dot in data.tempL8: 
        x,y=dot[0],dot[1]
        x1,y1=x, 400-(x-600)
        canvas.create_line(x,y,x1,y1,width=3,fill=data.color[2][1][10])#10
        data.tempL7.append([x1,y1])
    
    #line 3 and line 6
    data.tempL3,data.tempL6=[],[] 
    for dot in data.tempL2: 
        length=(600-dot[0])*2**(1/2)/(math.sin(math.pi*2*(57/360)))*(math.sin(math.pi*2*(18/360)))
        x,y=dot[0],dot[1]
        x1,y1=x+math.cos(2*math.pi/6)*length, y-math.sin(2*math.pi/6)*length
        canvas.create_line(x,y,x1,y1,width=3,fill=data.color[2][1][5])#5
        data.tempL3.append([x1,y1])
        
    for dot in data.tempL7: 
        length=(dot[0]-600)*2**(1/2)/(math.sin(math.pi*2*(57/360)))*(math.sin(math.pi*2*(18/360)))
        x,y=dot[0],dot[1]
        x1,y1=x-math.cos(2*math.pi/6)*length, y-math.sin(2*math.pi/6)*length
        canvas.create_line(x,y,x1,y1,width=3,fill=data.color[2][1][9])#9
        data.tempL6.append([x1,y1])
        
    #line 4 and line 5
    data.tempL4,data.tempL5=[],[] 
    for dot in data.tempL3: 
        length=((600-dot[0])/math.cos(2*math.pi*63/360))/(math.sin(math.pi*2*(93/360)))*(math.sin(math.pi*2*(18/360)))
        x,y=dot[0],dot[1]
        x1,y1=x+math.cos(math.pi/6)*length, y-math.sin(math.pi/6)*length
        canvas.create_line(x,y,x1,y1,width=3,fill=data.color[2][1][6])#6
        data.tempL4.append([x1,y1])
        
    for dot in data.tempL6: 
        length=((dot[0]-600)/math.cos(2*math.pi*63/360))/(math.sin(math.pi*2*(69/360)))*(math.sin(math.pi*2*(18/360)))
        x,y=dot[0],dot[1]
        x1,y1=x-math.cos(math.pi/6)*length, y-math.sin(math.pi/6)*length
        canvas.create_line(x,y,x1,y1,width=3,fill=data.color[2][1][8])#8
        data.tempL5.append([x1,y1])
        
        
             
    for i in range(len(data.tempML)):
        canvas.create_line(data.tempML[i][0],data.tempML[i][1],data.tempMR[i][0],data.tempMR[i][1],width=3,fill=data.color[2][1][1])#1 
        canvas.create_line(data.tempL4[i][0],data.tempL4[i][1],data.tempL5[i][0],data.tempL5[i][1],width=3,fill=data.color[2][1][7]) #7
        i=len(data.tempMR)-1
        sidelength=data.tempMR[i][0]-data.tempML[i][0]
#        canvas.create_rectangle(data.tempML[i][0],data.tempML[i][1],data.tempML[i][0]+sidelength,data.tempML[i][1]-sidelength,fill='pink',width=3)
    
    

    data.allDots=[data.moveDotsmainR,data.tempMR,data.tempML,data.moveDotsmainL,data.tempL1,data.tempL2,data.tempL3,data.tempL4,data.tempL5,data.tempL6,data.tempL7,data.tempL8] 
import random
def allThemes(): 
    a1=['black','white', 'white', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']
    a2=['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']
    b1=['snow', 'black', 'black', 'snow', 'snow', 'snow', 'snow', 'snow', 'snow', 'snow', 'snow', 'snow']
    b2=['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']
    c1=['black', 'snow', 'snow', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']
    c2=['black', 'snow', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']
    d2=['gold', 'black', 'gold', 'gold', 'gold', 'gold', 'gold', 'gold', 'gold', 'gold', 'gold', 'gold']#['black', 'red', 'red', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']
    d1=['gold', 'black', 'black', 'gold', 'gold', 'gold', 'gold', 'gold', 'gold', 'gold', 'gold', 'gold']#['black', 'red', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']
    a=[a1,a2]
    b=[b1,b2]
    c=[c1,c2]
    d=[d1,d2]
    theme1=['black','white',a] #star sky
    theme2=['white','black',b] #iridecent
    theme3=['blue','red',c]#spiderman
    theme4=['gold','red',d]#iron man modefied
    return [theme1,theme2,theme3,theme4]
    
def colorful():
    color=['red','orange','yellow','green','blue','purple','grey','snow','cyan','magenta']
    i = random.randint(0,9)
    return color[i]
    
    
absu=['gold' for i in range (12)]
print('welcome')


from tkinter import *
import random

WIDTH=600
HEIGHT=600
BACKGROUND="#000000"
SNAKE_COLOR="#2D0DCE"
SNAKE_SIZE=3
FOOD="#D0E81C"
SPEED=120
SPACE=50

class  Snake:
    def __init__(self):
        self.size=SNAKE_SIZE
        self.coordinates=[]
        self.squares=[]
        
        for i in range(SNAKE_SIZE):
            self.coordinates.append([0,0])
            
        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y,x+SPACE,y+SPACE,fill=SNAKE_COLOR,tag='snake')
            self.squares.append(square)

class Food:
    
    def __init__(self):
        x=random.randint(0,(WIDTH//SPACE)-1)*SPACE
        y=random.randint(0,(HEIGHT//SPACE)-1)*SPACE
        
        self.coordinates=[x,y]
        
        self.id=canvas.create_oval(x,y,x+SPACE,y+SPACE,fill=FOOD,tags='food')
    

def next_turn(snake,food):
    x,y=snake.coordinates[0]
    if dir=='up':
        y-=SPACE
    elif dir=='down':
        y+=SPACE
    elif dir=='left':
        x-=SPACE
    elif dir=='right':
        x+=SPACE
        
    snake.coordinates.insert(0,(x,y))
    square=canvas.create_rectangle(x,y,x+SPACE,y+SPACE,fill=SNAKE_COLOR)
    snake.squares.insert(0,square)
    
    
    if x==food.coordinates[0] and y==food.coordinates[1]:
        global score
        score+=1
        label.config(text=f"Score {score}")

        canvas.delete(food.id)
        food=Food()
        
    else:
            del snake.coordinates[-1]
    
            canvas.delete(snake.squares[-1])
    
            del snake.squares[-1]
            
    if checkcollision(snake):
        over()
    else:
        window.after(SPEED,next_turn,snake,food)


def change_dir(new):
    global dir
    if new=='up':
        if dir!='down':
            dir=new
    elif new=='down':
        if dir!='up':
            dir=new
    elif new=='left':
        if dir!='right':
            dir=new
    elif new=='right':
        if dir!='left':
            dir=new
            

def over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,text="Game Over ",fill='red',font=('Consolas',50))
    

def checkcollision(snake):
    x, y = snake.coordinates[0]    
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        return True 
    for body in snake.coordinates[1:]:
        if x == body[0] and y == body[1]:
            return True
        
    return False

    
window=Tk()
window.title("Snake Game")
window.resizable(False,False)
score=0
dir='down'

label=Label(window,text="Score {}".format(score),font=('Impact',40))
label.pack()

canvas=Canvas(window,bg='black',height=HEIGHT,width=WIDTH)
canvas.pack()
window.update()

win_width=window.winfo_width()
win_height=window.winfo_height()
scr_width=window.winfo_screenwidth()
scr_height=window.winfo_screenheight()

x=int((scr_width/2)-(win_width/2))
y=int((scr_height/2)-(win_height/2))

window.geometry(f"{win_width}x{win_height}+{x}+{y}")
window.bind("<Up>",lambda event :change_dir('up'))
window.bind("<Down>",lambda event :change_dir('down'))
window.bind("<Left>",lambda event :change_dir('left'))
window.bind("<Right>",lambda event :change_dir('right'))

snake=Snake()
food=Food()
next_turn(snake,food)
window.mainloop()
import turtle as trtl
import random
import time
tom = trtl.Turtle()
#makes screen black 
tom.hideturtle()
wn = trtl.Screen()
wn.bgcolor("black")
fire=input("do you want fireworks?")
if fire == "n":
    print("I guess your boring then, here are fireworks anyways")   
    

while True:
    #makes tail of firework
    randomx= random.randint(-200, 200) 
    tom.speed(1)
    tom.goto(randomx,-200)
    tom.pencolor("red")
    tom.pensize(5)
    tom.setheading(90)
    tom.forward(200)
    tom.penup()
    tom.goto(randomx,-200)
    tom.pendown()
    tom.pencolor("black")
    tom.pensize(7)
    tom.setheading(90)
    tom.forward(200)
    
    
    count = 0
    #makes random color 
    def random_color():
        r = random.random()
        g = random.random()
        b = random.random()

        return (r,g,b)

    tom.pencolor(random_color())
    #makes the "head" of the firework
    while count < 360/40:
        tom.speed(0)
        tom.pensize(5)
        tom.penup()
        tom.goto(randomx,180)
        tom.pendown()

        tom.setheading(40*count)
        tom.forward (100)
        print(count)
        count += 1
    #clears firework
    time.sleep(1)
    tom.penup()
    tom.goto(randomx,180)
    tom.color("black")
    tom.fillcolor("black")
    ncount = 1
    '''while ncount < 5:
        tom.begin_fill()
        tom.circle(10 * ncount)
        tom.end_fill()
        ncount += 1'''
    while ncount < 5:
        tom.begin_fill()
        tom.dot(52 * ncount)
        tom.end_fill()
        ncount += 1
    tom.end_fill()
    tom.pendown()


#wn = trtl.Screen()
wn.mainloop()
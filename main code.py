
# Final Project
# Mr.Rich's Financial App
#This app will ask you simple questions regarding how much you spend monthly on various things.
#Then with the collected data it will give out advice on what to do to save more money


import turtle
import random
from turtle import simpledialog


global count
count = 0

global balance
balance = 0

global money_spent
money_spent = 0

global hit
hit = 1

def get_input(prompt):
    # Create a custom input box
    input_box = turtle.textinput("Input", prompt)

    # Wait for the user to enter text
    while input_box is None:
        input_box = turtle.textinput("Input", prompt)

    return input_box

def no_name(x,y):
    global count
    count += 1
    if count == 1:
        turtle.clearscreen()
        s.bgcolor("black")
        s.bgpic(photo_list[1])
        t_text.pencolor("yellow")
        t_text.goto(200, 210)
        t_text.write("My name is Mr. rich", False, align="center", font=("Verdana", 25, "bold"))
        t_text.goto(190, 160)
        t_text.write("I will ask you some simple question,", False, align="center", font=("Verdana", 25, "bold"))
        t_text.goto(190, 110)
        t_text.write("try to answer them", False, align="center", font=("Verdana", 25, "bold"))
 
        button()

        t_text.goto(170, -180)
        t_text.pencolor("yellow")
        #t_text.write("Lets Begin!", False, align="center", font=("Verdana", 30, "bold"))
        a = True
    else:
        turtle.onscreenclick(None)
        turtle.clearscreen()
        lol()

def button():
    next_button2 = turtle.Turtle()
    next_button2.penup()
    next_button2.goto(560, -290)
    turtle.addshape("next.gif")
    next_button2.shape("next.gif")
    next_button2.onclick(no_name)

def turtles_walk(turtle1, start1, end1, num, steps):  
    stick_pics = ["new_image3.gif", "new_image4.gif", "new_image5.gif", "new_image6.gif", "new_image7.gif"]

    turtle.addshape(stick_pics[num])
    stick.hideturtle()
    stick.penup()
    stick.speed(100)
    stick.shape(stick_pics[num])

    deltax1 = (end1[0] - start1[0])/steps
    deltay1 = (end1[1] - start1[1])/steps
    # set up starting spots
    x1 = start1[0]
    y1 = start1[1]
    # set up turtles at starting spot
    turtle1.goto(x1, y1)
    turtle1.showturtle()
    turtle1.speed(10)

    # move turtles together, one step at a time
    for iter in range(1, steps):
        x1 = x1 + deltax1
        y1 = y1 + deltay1
        turtle1.goto(x1, y1)
    

def icons_move(a, num, x, y, start, end):

    icon_list = ["icon_image1.gif", "icon_image2.gif", "icon_image3.gif", "icon_image4.gif", "icon_image5.gif", "icon_image6.gif", "icon_image7.gif"]
    small_icon_list = ["small_icon_image1.gif", "small_icon_image2.gif", "small_icon_image3.gif", "small_icon_image4.gif", "small_icon_image5.gif", "small_icon_image6.gif", "small_icon_image7.gif"]
    check_list = ["check.gif", "check.gif", "check.gif", "check.gif", "check.gif", "check.gif", "check.gif"]

    icon2 = turtle.Turtle()
    small2 = turtle.Turtle()
    
    if a == 1:
        turtle.addshape(icon_list[num])
        icon.speed(30)
        icon.goto(x,y)
        icon.showturtle()
        icon.penup()
        
        icon.shape(icon_list[num])

    else:
        turtle.addshape(icon_list[num])
        icon.penup()
        icon.speed(30)
        icon.goto(x,y)
        icon.showturtle()
        icon.shape(icon_list[num])

        steps = 5
        deltax1 = (end[0] - start[0])/steps
        deltay1 = (end[1] - start[1])/steps
        # set up starting spots
        x1 = start[0]
        y1 = start[1]
        # set up turtles at starting spot
        icon.goto(x1, y1)
        icon.showturtle()


        # move turtles together, one step at a time
        for iter in range(1, steps):
            x1 = x1 + deltax1
            y1 = y1 + deltay1
            icon.goto(x1, y1)

        icon.hideturtle()
        turtle.addshape(small_icon_list[num])
        small2.penup()
        small2.speed(30)
        small2.goto(end[0] + 120, end[1])
        small2.showturtle()
        small2.shape(small_icon_list[num])

        check = turtle.Turtle()
        check.hideturtle()
        check.speed(50)
        check.width(5) 
        check.penup()
        check.fillcolor("white")
        check.goto(end[0] + 250, end[1] - 30)
        check.begin_fill()
        check.pendown()
        check.circle(35)
        check.end_fill()
        check.penup()
        check.pensize(14)
        check.pencolor("green")
        check.goto(end[0] + 240, end[1]) 
        check.pendown()
        check.right(45)
        check.forward(15)
        check.backward(35)
        check.forward(35)
        check.left(90)
        check.forward(75)
        


def spent_money_and_balance():
    global balance
    global money_spent
    text2.clear()
    text2.goto(-620,220)
    Balance: {balance}
    text2.write(f'Balance: {balance} ',True, align = 'left',font = ('Verdana', 16, 'bold'))
    text2.write(f' Money Spent: {money_spent}',True, align = 'left',font = ('Verdana', 16, 'bold'))


def conversation(x,y):
    global hit
    conversation_list = ["bubble1.gif","bubble2.gif", "bubble3.gif"]
    turtle.addshape(conversation_list[0])
    turtle.addshape(conversation_list[1])
    turtle.addshape(conversation_list[2])
    if x == 1: 
        conversation1.hideturtle()
    elif hit == 5:
        conversation1.penup()
        conversation1.goto(240, -150)
        conversation1.shape(conversation_list[2])
        conversation1.showturtle()
    elif hit == 4: 
        conversation1.penup()
        conversation1.goto(210, 250)
        conversation1.shape(conversation_list[1])
        conversation1.showturtle()
    elif hit == 3:
        conversation1.penup()
        conversation1.goto(300, -50)
        conversation1.shape(conversation_list[0])
        conversation1.showturtle()

def anime(a):
    if a == 3:
        turtles_walk(stick, [800,-500], [590, -365], 0, 50) # Rent
    elif a == 4:
        conversation(1,0)
        turtles_walk(stick, [900,-170], [570, -170], 1, 50)   # Food
        stick.onclick(conversation)
    elif a == 5:
        conversation(1,0)
        turtles_walk(stick, [550,-600], [550, -285], 2, 50)  # Debt
    elif a == 6:
        conversation(1,0)
        turtles_walk(stick, [500,600], [500, 365], 3, 50)   # Transportation
        stick.onclick(conversation)
    elif a == 7:
        conversation(1,0)
        turtles_walk(stick, [490,-600], [490, -200], 4, 50)   # Miscellaneous
        stick.onclick(conversation)
    elif a == 8:
        conversation(1,0)
        stick.hideturtle() # How much to put in savings

def make_questionbox():
    t.penup()
    t.fillcolor("white")
    t.goto(-640, 360)
    t.pendown()
    t.begin_fill()
    t.setheading(0)
    t.forward(1280)
    t.right(90)
    t.forward(140)
    t.right(90)
    t.forward(1280)
    t.right(90)
    t.forward(140)
    t.end_fill()
    t.penup()

def tips():
    tip = turtle.Turtle()
    tip.hideturtle()
    tip.fillcolor("white")
    tip.penup()
    tip.goto(-370, -360)
    tip.speed(300)
    tip.pendown()
    tip.setheading(90)
    tip.begin_fill()
    tip.forward(60)
    tip.right(90)
    tip.forward(700)
    tip.right(90)
    tip.forward(60)
    tip.right(90)
    tip.forward(700)
    tip.end_fill()
    tip_text.penup()
    tip_text.goto(-360, -350)
    tip_text.pendown()


def question_set(i):
    global money_spent
    global balance
    global hit
    text.clear()
    a = False
    b = False
    good = True
    spending_list = []
    q = 3
    while i in [0,3,4,5,6,7,8]:
        tip_ran = random.randint(0, 4)
        
        if i == 0:
            while b == False:
                icon.hideturtle()
                small.hideturtle()
                check.hideturtle()

                text.write(f'{questions[0]}',False,align = 'left', font = ('Verdana', 16, 'bold'))
            
                balance = int(input(questions[0]))
                spending_list.append(balance)
                text.clear()
                text.write(f'{questions[1]}',False,align = 'left', font = ('Verdana', 16, 'bold'))
                icons_move(1,0, 0, 0, [0,0], [0,0])
                goal = int(input(questions[1]))
                icons_move(3,0, 0, 0, [0,0], [-680, 100])
                text.clear()
                text.write(f'{questions[2]}',False,align = 'left', font = ('Verdana', 16, 'bold'))
                
                years = int(input(questions[2]))
                
                text.clear()
                financial_goal = ((goal/years)/12)
                text.write(f'Based on your financial goal of ${goal} and wanting to complete it in {years} years,\n',False,align = 'left', font = ('Verdana', 16, 'bold'))
                text.write(f' we estimate that you will have to pay ${financial_goal:.2f} a month for {years} years. Is that ok? (y/n)', False, align = 'left', font = ('Verdana', 16, 'bold'))
                estimated_goal = input(f'Based on your financial goal of ${goal} and wanting to complete it in {years} years,we estimate that you will have to pay ${financial_goal:.2f} a month for {years} years. Is that ok? (y/n)')
                if estimated_goal == "y":
                    text.clear()
                    b = True
                else:
                    text.clear()
                    print("Ok let's go back then.")
                    b = False
                i = 3
        tips()
        if balance < 0:
            icon.hideturtle()
            small.hideturtle()
            check.hideturtle()
            b = True
            a = True
            q = 4
            break
        else:
            while True:
                spent_money_and_balance()
                tip_text.pencolor("red")
                tip_text.clear()
                tip_text.write(f'{tips_list[tip_ran]}',False, align = 'left',font = ('Verdana', 13, 'bold'))
                text.write(f'{questions[i]}',False, align = 'left',font = ('Verdana', 16, 'bold'))
                if i in [3, 4, 5]:
                    icons_move(1, i-2, 0,0, [0,0], [0,0])
                else:
                    icons_move(1, i-2, 50,0, [0,0], [0,0])
                anime(i)
                spent = simpledialog.askinteger("Question", f"{questions[i]}")
                turtle.update()
                text.write("Is this the right amount of money y/n?",False,align = 'left', font = ('Verdana', 16, 'bold'))
                #get_input(questions[i])
                x = simpledialog.askstring("Confirmation", "Is this the right amount of money y/n?")
                

                
                if x == "y":
                    text.clear()
                    money_spent += spent
                    balance -= spent
                    spent_money_and_balance()
                    spending_list.append(spent)
                    if i in [3, 4, 5]:
                        icons_move(3,i-2, 0, 0, [0,0], [-680, 100 - ((i-2) * 120)])
                    else:
                        icons_move(3,i-2, 0, 0, [0,0], [-380, 100 - ((i-6) * 120)])
                    break
                else:
                    text.clear()
        hit += 1
        q += 1
        i += 1
        conversation1.hideturtle()
    return a, spending_list

def final_recom(spending_list):
    avg_spending_list = [6228, 1526, 650, 1233, 800, 250]    #, 1000] this is for savings

    for j in range(len(avg_spending_list)):
        if spending_list[j] == 0:
            text.goto(-600, 210 - (50 * j))
            text.write(f'{finale_recom_list[17]}',False, align = 'left',font = ('Verdana', 18, 'bold'))
        elif spending_list[j] < avg_spending_list[j]:
            text.goto(-600, 210 - (50 * j))
            text.write(f'{finale_recom_list[j]}',False, align = 'left',font = ('Verdana', 18, 'bold'))
        elif spending_list[j] > avg_spending_list[j]:
            text.goto(-600, 210 - (50 * j))
            text.write(f'{finale_recom_list[j + 9]}',False, align = 'left',font = ('Verdana', 18, 'bold'))
            
    text.goto(-600, -90)
    text.write(f'{finale_recom_list[7]}',False, align = 'left',font = ('Verdana', 16, 'bold'))
    text.goto(-600,-120)
    text.write(f'{finale_recom_list[8]}',False, align = 'left',font = ('Verdana', 16, 'bold'))
    text.goto(-600, -170)
    text.write(f'{finale_recom_list[9]}',False, align = 'left',font = ('Verdana', 16, 'bold'))
    text.goto(-600, -190)
    text.pencolor("teal")
    text.write("TO GET MORE TIPS VISIT THESE LINKS: ",False, align = 'left',font = ('Verdana', 18, 'bold'))
    text.pencolor("blue")
    text.goto(-600, -230)
    text.write("Top 10 Financial Tips - https://www.thebalancemoney.com/top-ten-financial-tips-1289309",False,align = 'left', font = ('Verdana', 16, 'bold'))
    text.goto(-600, -270)
    text.write("15 Finance Tips And Tricks For Financial Success - https://tuppennysfireplace.com/financial-tips-and-tricks/",False,align = 'left', font = ('Verdana', 16, 'bold'))
    text.goto(-600, -310)
    text.write("Basic Budgeting Tips Everyone Should Know - https://www.thebalancemoney.com/budgeting-101-1289589",False,align = 'left', font = ('Verdana', 16, 'bold'))

def lol():
    global balance
    global money_spent
    turtle.clearscreen()
    s.bgcolor("black")

    text2.penup()
    text2.hideturtle()
    text2.goto(-640,300)

    text.penup()
    text.hideturtle()
    text2.hideturtle()
    text.goto(-615,300)

    good = False
    make_questionbox()
    i = 0
    while good == False:

        a, spending_list = question_set(i)
        good = False
        if a == True:
            print("Oops, your balance is in negative")
            money_spent = 0
            balance = spending_list[0]
            i = 3
            question_set(i)
            good = False
        else:
            good = True
            turtle.clearscreen()
            s.bgcolor("black")
            text.goto(0, 300)
            text.pencolor("white")
            text.write("Finale Recommendations",False,align = 'center', font = ('Verdana', 30, 'bold'))

            final_recom(spending_list)

s = turtle.getscreen()
t_text = turtle.Turtle()
t = turtle.Turtle()
text = turtle.Turtle()
icon = turtle.Turtle()
check = turtle.Turtle()
small = turtle.Turtle()
tip_text = turtle.Turtle()

turtle.screensize(1280, 720)
turtle.setup(1280, 720)
stick = turtle.Turtle()
text.hideturtle()

good = False
a = False
t.penup()
t.speed(300)
t.width(5)
t_text.hideturtle()
turtle.hideturtle()
icon.hideturtle()
small.hideturtle()
check.hideturtle()
tip_text.hideturtle()
conversation1 = turtle.Turtle()
conversation1.hideturtle()

photo_list = ["new_image1.gif", "new_image2.gif"]
s.bgpic("new_image1.gif")
files = open("questions.txt")
questions = files.readlines()

files2 = open("tips.txt")
tips_list = files2.readlines()

files3 = open("finale_recom.txt")
finale_recom_list = files3.readlines()
s.bgcolor("black")

next_button = turtle.Turtle()
turtle.addshape("next.gif")
next_button.penup()
next_button.goto(560, -290)
next_button.shape("next.gif")

text2 = turtle.Turtle()
t_text.penup()
t_text.goto(0, 190)
t_text.pencolor("white")
t_text.write("Welcome to My Little Q&A App!", False, align="center", font=("Verdana", 35, "bold"))
next_button.onclick(no_name)
turtle.onscreenclick(None)

turtle.mainloop()

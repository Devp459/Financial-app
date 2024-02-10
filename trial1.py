import turtle
import tkinter as tk
from tkinter import messagebox
from turtle import simpledialog

global count
count = 0

global balance
balance = 0

global money_spent
money_spent = 0

global hit
hit = 1

class FinancialApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mr. Rich's Financial App")
        self.geometry("600x400")

        self.balance = 0
        self.money_spent = 0

        self.create_widgets()

    def create_widgets(self):
        self.label_balance = tk.Label(self, text="Balance: $0")
        self.label_balance.pack()

        self.label_money_spent = tk.Label(self, text="Money Spent: $0")
        self.label_money_spent.pack()

        self.button_start = tk.Button(self, text="Start", command=self.start_questionnaire)
        self.button_start.pack()

    def start_questionnaire(self):
        self.question_index = 0
        self.questions = [
            "How much do you have in your account?",
            "How much do you want to save?",
            "How many years do you want to achieve your savings goal?",
            "How much do you spend on rent per month?",
            "How much do you spend on food per month?",
            "How much do you spend on debt payments per month?",
            "How much do you spend on transportation per month?",
            "How much do you spend on miscellaneous expenses per month?"
        ]

        self.ask_question()

    def ask_question(self):
        if self.question_index < len(self.questions):
            question = self.questions[self.question_index]

            self.input_frame = tk.Frame(self)
            self.input_frame.pack()

            self.label_question = tk.Label(self.input_frame, text=question)
            self.label_question.pack()

            self.entry_answer = tk.Entry(self.input_frame)
            self.entry_answer.pack()

            self.button_next = tk.Button(self.input_frame, text="Next", command=self.process_answer)
            self.button_next.pack()

        else:
            self.input_frame.destroy()  # Clean up input frame
            self.display_recommendations()

    def process_answer(self):
        answer = self.entry_answer.get()
        if answer.isdigit():
            answer = int(answer)

            if self.question_index == 0:
                self.balance = answer
            elif self.question_index == 1:
                self.savings_goal = answer
            elif self.question_index == 2:
                self.years_to_achieve_goal = answer
            else:
                self.money_spent += answer

            self.label_balance.config(text=f"Balance: ${self.balance}")
            self.label_money_spent.config(text=f"Money Spent: ${self.money_spent}")

            self.question_index += 1
            self.ask_question()

        else:
            messagebox.showerror("Error", "Please enter a valid number.")

    def display_recommendations(self):
        avg_spending_list = [0, 0, 0, 6228, 1526, 650, 1233, 800]  # Adjusted for questions 3-8
        recommendations = []

        for i in range(3, min(len(self.questions), len(avg_spending_list) + 3)):
            if self.money_spent == 0:
                recommendations.append("You haven't entered any expenses.")
                break
            elif self.money_spent < avg_spending_list[i - 3]:
                recommendations.append(f"You are spending less than average on {self.questions[i]}.")
            elif self.money_spent > avg_spending_list[i - 3]:
                recommendations.append(f"You are spending more than average on {self.questions[i]}.")

        messagebox.showinfo("Recommendations", "\n".join(recommendations))

def get_input():
    # Create a custom input box
    input_box = turtle.textinput("Input", )

    # Wait for the user to enter text
    while input_box is None:
        input_box = turtle.textinput("Input", )

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

    deltax1 = (end1[0] - start1[0]) / steps
    deltay1 = (end1[1] - start1[1]) / steps
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

def spent_money_and_balance():
    global balance
    global money_spent
    text2.clear()
    text2.goto(-620, 220)
    text2.write(f'Balance: {balance} ', True, align='left', font=('Verdana', 16, 'bold'))
    text2.write(f' Money Spent: {money_spent}', True, align='left', font=('Verdana', 16, 'bold'))

def lol():
    global balance
    global money_spent
    turtle.clearscreen()
    s.bgcolor("black")

    text2.penup()
    text2.hideturtle()
    text2.goto(-640, 300)

    text.penup()
    text.hideturtle()
    text2.hideturtle()
    text.goto(-615, 300)

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
            text.write("Finale Recommendations", False, align='center', font=('Verdana', 30, 'bold'))

            final_recom(spending_list)

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
    while i in [0, 3, 4, 5, 6, 7, 8]:
        tip_ran = random.randint(0, 4)

        if i == 0:
            while b == False:
                text.write(f'{questions[0]}', False, align='left', font=('Verdana', 16, 'bold'))

                balance = simpledialog.askinteger("Question", "How much do you have in your account?")
                spending_list.append(balance)
                text.clear()
                text.write(f'{questions[1]}', False, align='left', font=('Verdana', 16, 'bold'))

                goal = simpledialog.askinteger("Question", "How much do you want to save?")
                text.clear()
                text.write(f'{questions[2]}', False, align='left', font=('Verdana', 16, 'bold'))

                years = simpledialog.askinteger("Question", "How many years do you want to achieve your savings goal?")
                text.clear()

                financial_goal = ((goal / years) / 12)
                text.write(
                    f'Based on your financial goal of ${goal} and wanting to complete it in {years} years,\n',
                    False, align='left', font=('Verdana', 16, 'bold'))
                text.write(
                    f' we estimate that you will have to pay ${financial_goal:.2f} a month for {years} years. Is that ok? (y/n)',
                    False, align='left', font=('Verdana', 16, 'bold'))
                estimated_goal = get_input()

                if estimated_goal == "y":
                    text.clear()
                    b = True
                else:
                    text.clear()
                    print("Ok let's go back then.")
                    b = False
                i = 3

        if balance < 0:
            b = True
            a = True
            q = 4
            break
        else:
            while True:
                spent_money_and_balance()
                text.write(f'{questions[i]}', False, align='left', font=('Verdana', 16, 'bold'))

                spent = simpledialog.askinteger("Question", f"{questions[i]}")
                spent_money_and_balance()

                x = get_input()

                if x == "y":
                    text.clear()
                    money_spent += spent
                    balance -= spent
                    spent_money_and_balance()

                    break
                else:
                    text.clear()
        hit += 1
        q += 1
        i += 1

    return a, spending_list

def final_recom(spending_list):
    avg_spending_list = [6228, 1526, 650, 1233, 800]  # Adjusted for questions 3-8

    for j in range(len(avg_spending_list)):
        if spending_list[j] == 0:
            text.goto(-600, 210 - (50 * j))
            text.write(f'{finale_recom_list[17]}', False, align='left', font=('Verdana', 18, 'bold'))
        elif spending_list[j] < avg_spending_list[j]:
            text.goto(-600, 210 - (50 * j))
            text.write(f'{finale_recom_list[j]}', False, align='left', font=('Verdana', 18, 'bold'))
        elif spending_list[j] > avg_spending_list[j]:
            text.goto(-600, 210 - (50 * j))
            text.write(f'{finale_recom_list[j + 9]}', False, align='left', font=('Verdana', 18, 'bold'))

    text.goto(-600, -90)
    text.write(f'{finale_recom_list[7]}', False, align='left', font=('Verdana', 16, 'bold'))
    text.goto(-600, -120)
    text.write(f'{finale_recom_list[8]}', False, align='left', font=('Verdana', 16, 'bold'))
    text.goto(-600, -170)
    text.write(f'{finale_recom_list[9]}', False, align='left', font=('Verdana', 16, 'bold'))
    text.goto(-600, -190)
    text.pencolor("teal")
    text.write("TO GET MORE TIPS VISIT THESE LINKS: ", False, align='left', font=('Verdana', 18, 'bold'))
    text.pencolor("blue")
    text.goto(-600, -230)
    text.write(
        "Top 10 Financial Tips - https://www.thebalancemoney.com/top-ten-financial-tips-1289309", False,
        align='left', font=('Verdana', 16, 'bold'))
    text.goto(-600, -270)
    text.write(
        "15 Finance Tips And Tricks For Financial Success - https://tuppennysfireplace.com/financial-tips-and-tricks/",
        False, align='left', font=('Verdana', 16, 'bold'))
    text.goto(-600, -310)
    text.write("Basic Budgeting Tips Everyone Should Know - https://www.thebalancemoney.com/budgeting-101-1289589",
               False, align='left', font=('Verdana', 16, 'bold'))


s = turtle.getscreen()
t_text = turtle.Turtle()
t = turtle.Turtle()
text = turtle.Turtle()

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
stick.hideturtle()

photo_list = ["new_image1.gif", "new_image2.gif"]
s.bgpic("new_image1.gif")
files = open("questions.txt")
questions = files.readlines()

files2 = open("tips.txt")
tips_list = files2.readlines()

files3 = open("finale_recom.txt")
finale_recom_list = files3.readlines()
s.bgcolor("black")

text2 = turtle.Turtle()
t_text.penup()
t_text.goto(0, 190)
t_text.pencolor("white")
t_text.write("Welcome to My Little Q&A App!", False, align="center", font=("Verdana", 35, "bold"))

turtle.mainloop()

import tkinter as tk
from tkinter import messagebox

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

if __name__ == "__main__":
    app = FinancialApp()
    app.mainloop()

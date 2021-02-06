from tkinter import *
from tkinter import messagebox
import html

#Question

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


#Brain
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def got_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        unescaped_text = html.unescape(self.current_question.text) #unescape html txt
        return f"Q.{self.question_number}: {unescaped_text}"


    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

#UI
THEME_COLOR = "#375362"

def helpme():
    messagebox.showinfo("Help","Click True or False to continue")

class UI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain


        #basic settings and bg color
        self.window = Tk()
        self.window.title("Data Game!")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #score tracker
        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        #white canvas for questions
        self.canvas = Canvas(width = 300, height=300, bg="white")
        self.questions_canvas = self.canvas.create_text(150,
                                                        150,
                                                        width=280,
                                                        text="Questions here",
                                                        font=("Times New Roman", 15, "italic"),
                                                        fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        #True and False button
        true_pic = PhotoImage(file="images/true.png")
        self.true = Button(image=true_pic,
                           highlightthickness=0,
                           command=self.true_click)
        self.true.grid(row=2,column=1)

        false_pic = PhotoImage(file="images/false.png")
        self.false = Button(image=false_pic,
                            highlightthickness=0,
                            command=self.false_click)
        self.false.grid(row=2, column=0)

        #help button
        self.clicker = Button(text="help", command=helpme)
        self.clicker.grid(row=3, column=0, pady=40)

        self.get_next_question()

        #main loop
        self.window.mainloop()


        #create new method to get new question

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.got_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            new_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questions_canvas, text=new_text)

        else:
            self.canvas.itemconfig(self.questions_canvas, text="End of quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

        #create new methods for true or false

    def true_click(self):
        correct = self.quiz.check_answer("True")
        self.feedback(correct)

    def false_click(self):
        correct = self.quiz.check_answer("False")
        self.feedback(correct)

    def feedback(self, correct):
        if correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(500, self.get_next_question)


#main code

question_bank = []
for q in questions:
    q_text = q["question"]
    q_answer = q["correct_answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_user_interface = UI(quiz)

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")

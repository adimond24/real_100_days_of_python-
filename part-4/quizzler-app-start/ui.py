from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:



    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)


        self.score_label = Label(text=f"put score here", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.card = Canvas(width=300, height=250, bg="white")
        self.question_text = self.card.create_text(
            150,
            125,
            width= 280,
            text="add text here",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")

            )
        self.card.grid(row=1, column=0, columnspan=2, pady=50)

        check_mark_image = PhotoImage(file="images/true.png")
        self.check_mark_button = Button(image=check_mark_image, highlightthickness=0, command=self.true_pressed())
        self.check_mark_button.grid(column=0, row=2)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.false_pressed())
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.card.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.card.itemconfig(self.question_text, text=q_text)
        else:
            self.card.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.wrong_button.config(state="disabled")
            self.check_mark_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):

        if is_right:
            self.card.config(bg="green")
        else:
            self.card.config(bg="red")
        self.window.after(1000, self.get_next_question)


        
        
import tkinter as tk
from tkinter import messagebox
from main import Quiz, Question
from unittest.mock import patch, MagicMock

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz App")
        self.geometry("400x300")
        self.questions = [
            Question("What is the capital of France?",
                     ["London", "Paris", "Berlin", "Rome"],
                     "Paris"),
            Question("What is the largest planet in our solar system?",
                     ["Jupiter", "Saturn", "Mars", "Earth"],
                     "Jupiter"),
            # Add more questions here
        ]
        self.quiz = None
        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self, text="")
        self.question_label.pack()

        self.option_var = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            option_button = tk.Radiobutton(self, variable=self.option_var)
            option_button.pack()
            self.option_buttons.append(option_button)

        self.submit_button = tk.Button(self, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.next_button = tk.Button(self, text="Next", command=self.next_question)
        self.next_button.pack()
        self.next_button.configure(state="disabled")

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def start_quiz(self):
        self.quiz = Quiz(self.questions)
        self.next_question()

    def show_question(self):
        question = self.quiz.get_current_question()
        self.question_label.config(text=question.prompt)
        for i, option in enumerate(question.options):
            self.option_buttons[i].config(text=option, value=option)
        self.option_var.set("")

    def check_answer(self):
        selected_answer = self.option_var.get()
        is_correct = self.quiz.check_answer(selected_answer)
        if is_correct:
            messagebox.showinfo("Result", "Correct answer!")
        else:
            messagebox.showinfo("Result", "Incorrect answer!")
        self.submit_button.configure(state="disabled")
        self.next_button.configure(state="normal")

    def next_question(self):
        self.quiz.next_question()
        if self.quiz.has_ended():
            self.show_results()
        else:
            self.show_question()

    def show_results(self):
        score = self.quiz.get_score()
        total_questions = self.quiz.get_total_questions()
        result_text = f"You got {score} out of {total_questions} questions correct!"
        result_text += "\n\nHere are the questions and your answers:\n"
        for i, question in enumerate(self.questions):
            result_text += f"\nQuestion {i+1}:\n"
            result_text += f"Your answer: {question.user_answer}\n"
            result_text += f"Correct answer: {question.correct_answer}\n"
        self.result_label.config(text=result_text)


if __name__ == "__main__":
    app = QuizApp()
    app.start_quiz()
    app.mainloop()

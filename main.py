import tkinter as tk
from tkinter import messagebox

class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question_index = 0
        self.option_var = None

    def check_answer(self):
        selected_option = self.option_var.get()
        current_question = self.questions[self.current_question_index]
        if selected_option == current_question.answer:
            self.score += 1
        self.next_question()

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index == len(self.questions):
            self.show_results()
        else:
            self.show_question()

    def show_question(self):
        global question_label, option_radiobuttons, root
        current_question = self.questions[self.current_question_index]
        question_label.config(text=current_question.prompt)
        for i, option in enumerate(current_question.options):
            option_radiobuttons[i].config(text=option, variable=self.option_var, value=option, anchor='w')
            option_radiobuttons[i].deselect()
        option_radiobuttons[0].focus()

    def show_results(self):
        result_message = f"You got {self.score} out of {len(self.questions)} questions correct!"
        for question in self.questions:
            result_message += f"\n\n{question.prompt}\nYour answer: {self.option_var.get()}\nCorrect answer: {question.answer}"
        messagebox.showinfo("Quiz Results", result_message)
        root.destroy()


def start_quiz():
    global question_label, option_radiobuttons, root
    # Define the questions for the quiz
    questions = [
        Question("What is the capital of France?",
                 ["London", "Paris", "Berlin", "Rome"],
                 "Paris"),
        Question("What is the largest planet in our solar system?",
                 ["Jupiter", "Saturn", "Mars", "Earth"],
                 "Jupiter"),
        Question("Which is the largest ocean in the world?",
                 ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                 "Pacific Ocean"),
        Question("What is the chemical symbol for gold?",
                 ["Au", "Ag", "Gd", "Go"],
                 "Au"),
        Question("Who painted the Mona Lisa?",
                 ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
                 "Leonardo da Vinci"),
        Question("Which planet is known as the Red Planet?",
                 ["Mars", "Jupiter", "Mercury", "Venus"],
                 "Mars"),
        Question("What is the largest country by land area?",
                 ["Russia", "China", "United States", "Canada"],
                 "Russia"),
        Question("What is the national animal of Australia?",
                 ["Kangaroo", "Koala", "Emu", "Platypus"],
                 "Kangaroo"),
        Question("Which scientist is famous for the theory of relativity?",
                 ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
                 "Albert Einstein"),
        Question("Which country hosted the 2016 Summer Olympics?",
                 ["Brazil", "United States", "China", "Russia"],
                 "Brazil")
    ]

    # Creating a Quiz instance
    quiz = Quiz(questions)

    # Create the GUI using Tkinter
    root = tk.Tk()
    root.title("Quiz Application")

    question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 12))
    question_label.pack(pady=20)

    quiz.option_var = tk.StringVar()

    option_radiobuttons = []
    for i in range(4):
        option_radiobutton = tk.Radiobutton(root, text="", variable=quiz.option_var, width=50, anchor='w')
        option_radiobutton.pack()
        option_radiobuttons.append(option_radiobutton)

    next_button = tk.Button(root, text="Next", command=quiz.check_answer)
    next_button.pack(pady=20)

    quiz.show_question()

    root.mainloop()


start_quiz()

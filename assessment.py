import random
from tkinter import *
from PIL import Image, ImageTk


# Window setup
root = Tk()
root.title("World War II Quiz")
root.state("zoomed")


MAIN_GREEN = "#1e7e34"
root.configure(bg=MAIN_GREEN)


HOME_IMAGE_WIDTH = 900
HOME_IMAGE_HEIGHT = 550


QUIZ_IMAGE_WIDTH = 900
QUIZ_IMAGE_HEIGHT =500



questions = [
   {
       "q": "When did World War II begin?",
       "options": ["1914", "1939", "1945", "1922"],
       "answer": "1939",
       "image": "question1.png"
   },
   {
       "q": "Which country was led by Adolf Hitler in World War II?",
       "options": ["India", "Italy", "Germany", "Afghanistan"],
       "answer": "Germany",
       "image": "image2.png"
   },
   {
       "q": "Which event caused the US to join World War II?",
       "options": ["Battle of Britain", "Pearl Harbour attack", "D-Day", "Treaty of Versailles"],
       "answer": "Pearl Harbour attack",
       "image": "image3.png"
   },
   {
       "q": "Which alliance included Germany, Italy, and Japan?",
       "options": ["NATO", "League of Nations", "Axis Powers", "British Empire"],
       "answer": "Axis Powers",
       "image": "image4.png"
   },
   {
       "q": "Which city had the first atomic bomb dropped on it?",
       "options": ["Tokyo", "Hiroshima", "Nagasaki", "Osaka"],
       "answer": "Hiroshima",
       "image": "image5.png"
   }
]


random.shuffle(questions)
score = 0
q_index = 0


# UI Frame Controller Setup
container = Frame(root, bg=MAIN_GREEN)
container.pack(fill="both", expand=True)


frames = {}




def show_frame(page_class):
   frame = frames[page_class]
   frame.tkraise()
   if hasattr(frame, "update_page"):
       frame.update_page()




class HomePage(Frame):
   def __init__(self, parent):
       super().__init__(parent, bg=MAIN_GREEN)


       title = Label(
           self,
           text="Welcome to my quiz on World War II",
           font=("Arial", 34, "bold"),
           fg="white",
           bg=MAIN_GREEN
       )
       title.place(relx=0.5, rely=0.10, anchor=CENTER)


       self.image_label = Label(self, bg=MAIN_GREEN)
       self.image_label.place(relx=0.5, rely=0.45, anchor=CENTER)


       try:
           opened_img = Image.open("intro.png")
           resized_img = opened_img.resize((HOME_IMAGE_WIDTH, HOME_IMAGE_HEIGHT), Image.Resampling.LANCZOS)
           self.intro_img = ImageTk.PhotoImage(resized_img)
           self.image_label.config(image=self.intro_img, text="")
           self.image_label.image = self.intro_img
       except Exception:
           self.image_label.config(text="[intro.png Not Found]", fg="yellow", bg=MAIN_GREEN, font=("Arial", 14))


       start_button = Button(
           self,
           text="Start Quiz",
           font=("Arial", 18, "bold"),
           bg="black",
           fg="white",
           activebackground="#222222",
           activeforeground="white",
           bd=0,
           padx=35,
           pady=12,
           cursor="hand2",
           command=lambda: show_frame(QuizPage)
       )
       start_button.place(relx=0.5, rely=0.90, anchor=CENTER)




class QuizPage(Frame):
   def __init__(self, parent):
       super().__init__(parent, bg=MAIN_GREEN)
       self.answered = False


       self.score_label = Label(self, text="Score: 0", font=("Arial", 16, "bold"), fg="white", bg=MAIN_GREEN)
       self.score_label.place(relx=0.92, rely=0.05, anchor=CENTER)


       self.question_label = Label(
           self,
           text="",
           font=("Arial", 25, "bold"),
           fg="black",
           bg="#d9d9d9",
           wraplength=950,
           justify=CENTER,
           padx=20,
           pady=20
       )
       self.question_label.place(relx=0.5, rely=0.10, anchor=CENTER)


       self.image_label = Label(self, bg=MAIN_GREEN)
       self.image_label.place(relx=0.5, rely=0.42, anchor=CENTER)


       self.option_buttons = []
       positions = [(0.30, 0.85), (0.70, 0.85), (0.30, 0.70), (0.70, 0.70)]


       for i in range(4):
           btn = Button(
               self,
               text="",
               font=("Arial", 16, "bold"),
               bg="black",
               fg="white",
               activebackground="#333333",
               activeforeground="white",
               width=25,
               height=2,
               bd=0,
               wraplength=250,
               cursor="hand2",
               command=lambda x=i: self.check_answer(x)
           )
           x, y = positions[i]
           btn.place(relx=x, rely=y, anchor=CENTER)
           self.option_buttons.append(btn)


       self.feedback_label = Label(self, text="", font=("Arial", 18, "bold"), fg="white", bg=MAIN_GREEN)
       self.feedback_label.place(relx=0.5, rely=0.78, anchor=CENTER)


       self.previous_button = Button(
           self,
           text="← Previous",
           font=("Arial", 14, "bold"),
           bg="#d9d9d9",
           fg="black",
           bd=0,
           padx=20,
           pady=8,
           cursor="hand2",
           command=self.previous_question
       )










       self.next_button = Button(self, text="Next →", font=("Arial", 14, "bold"), bg="black", fg="white", bd=0,
                                 padx=20, pady=8, cursor="hand2", command=self.next_question)
       self.next_button.place(relx=0.90, rely=0.95, anchor=CENTER)


       self.load_question()


   def load_question(self):
       global q_index, score
       self.answered = False
       q_data = questions[q_index]


       self.question_label.config(text=q_data["q"])
       self.score_label.config(text=f"Score: {score}")
       self.feedback_label.config(text="")


       try:
           opened_img = Image.open(q_data["image"])
           resized_img = opened_img.resize((QUIZ_IMAGE_WIDTH, QUIZ_IMAGE_HEIGHT), Image.Resampling.LANCZOS)
           self.current_img = ImageTk.PhotoImage(resized_img)
           self.image_label.config(image=self.current_img, text="")
           self.image_label.image = self.current_img
       except Exception:
           self.image_label.config(image="", text=f"[{q_data['image']} Not Found]", fg="yellow", font=("Arial", 14))


       for i, btn in enumerate(self.option_buttons):
           btn.config(text=q_data["options"][i], bg="black", fg="white", state=NORMAL)


   def check_answer(self, selected_idx):
       global score
       if self.answered:
           return
       self.answered = True


       q_data = questions[q_index]
       selected_ans = q_data["options"][selected_idx]
       correct_ans = q_data["answer"]


       if str(selected_ans) == str(correct_ans):
           score += 1
           self.option_buttons[selected_idx].config(bg="green", fg="white")
           self.feedback_label.config(text="Correct!", fg="white")
       else:
           self.option_buttons[selected_idx].config(bg="red", fg="white")
           self.feedback_label.config(text=f"Incorrect! Correct answer: {correct_ans}", fg="white")


       self.score_label.config(text=f"Score: {score}")


   def next_question(self):
       global q_index
       if not self.answered:
           self.feedback_label.config(text="You must answer this question before you can proceed!", fg="yellow")
           return


       if q_index < len(questions) - 1:
           q_index += 1
           self.load_question()
       else:
           show_frame(EndPage)


   def previous_question(self):
       global q_index
       if q_index > 0:
           q_index -= 1
           self.load_question()


   def update_page(self):
       self.load_question()




class EndPage(Frame):
   def __init__(self, parent):
       super().__init__(parent, bg=MAIN_GREEN)


       self.center_box = Frame(self, bg="#155724", padx=50, pady=40, bd=2, relief=SOLID)
       self.center_box.place(relx=0.5, rely=0.5, anchor=CENTER)


       self.heading = Label(self.center_box, text="Great work!!", font=("Arial", 32, "bold"), fg="#d4edda",
                            bg="#155724")
       self.heading.pack(pady=10)


       self.score_display = Label(self.center_box, text="", font=("Arial", 24, "bold"), fg="white", bg="#155724")
       self.score_display.pack(pady=15)


       self.thanks_label = Label(self.center_box, text="Thank You for Playing!!!", font=("Arial", 22, "bold"),
                                 fg="#d4edda", bg="#155724")
       self.thanks_label.pack(pady=10)


   def update_page(self):
       self.score_display.config(text=f"Your Final Score: {score} / {len(questions)}")





class EndPage(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=MAIN_GREEN)

        self.center_box = Frame(self, bg=MAIN_GREEN)
        self.center_box.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.msg_label = Label(
            self.center_box,
            text="Great work!!",
            font=("Arial", 60, "bold"),
            fg="white",
            bg=MAIN_GREEN,
            pady=20
        )
        self.msg_label.pack()

        self.score_display = Label(
            self.center_box,
            text="",
            font=("Arial", 45, "bold"),
            fg="white",
            bg=MAIN_GREEN,
            pady=20
        )
        self.score_display.pack()

        self.thank_label = Label(
            self.center_box,
            text="Thank You for Playing!!!",
            font=("Arial", 35, "bold"),
            fg="white",
            bg=MAIN_GREEN,
            pady=20
        )
        self.thank_label.pack()

    def update_page(self):
        self.score_display.config(text=f"Your Final Score: {score} / {len(questions)}")


# Completely fresh window initialization code
for F in (HomePage, QuizPage, EndPage):
    frame = F(container)
    frames[F] = frame
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

show_frame(HomePage)
root.mainloop()

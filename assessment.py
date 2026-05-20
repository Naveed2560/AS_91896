
# =====================================================
# HOME PAGE
# =====================================================
class HomePage(Frame):

    def __init__(self, parent):

        super().__init__(parent, bg=MAIN_GREEN)

        # Main Title
        title = Label(
            self,
            text="Welcome to my quiz on World War II",
            font=("Arial", 34, "bold"),
            fg="white",
            bg=MAIN_GREEN
        )

        title.place(
            relx=0.5,
            rely=0.28,
            anchor="center"
        )

        # Subtitle
        subtitle = Label(
            self,
            text="Test your knowledge and see how much you know!",
            font=("Arial", 18),
            fg="white",
            bg=MAIN_GREEN
        )

        subtitle.place(
            relx=0.5,
            rely=0.38,
            anchor="center"
        )

        # Start Button
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

        start_button.place(
            relx=0.5,
            rely=0.58,
            anchor="center"
        )

import tkinter as tk
from tkinter import ttk, messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")

        # Initialize variables
        self.user_score = 0
        self.computer_score = 0

        # Create style and ttkbootstrap theme
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Create widgets
        self.label = ttk.Label(root, text="Choose: Rock, Paper, or Scissors", font=("Helvetica", 14))
        self.label.grid(row=0, column=0, pady=10, columnspan=3)

        self.user_choice_var = tk.StringVar()
        choices = ["Rock", "Paper", "Scissors"]
        self.user_choice_dropdown = ttk.Combobox(root, textvariable=self.user_choice_var, values=choices, state="readonly")
        self.user_choice_dropdown.grid(row=1, column=0, pady=10, padx=10)

        self.play_button = ttk.Button(root, text="Play", command=self.play_game)
        self.play_button.grid(row=1, column=1, pady=10, padx=10)

        self.result_label = ttk.Label(root, text="", font=("Helvetica", 12))
        self.result_label.grid(row=2, column=0, pady=10, columnspan=3)

        self.score_label = ttk.Label(root, text="Score: User {} - {} Computer".format(self.user_score, self.computer_score), font=("Helvetica", 12))
        self.score_label.grid(row=3, column=0, pady=10, columnspan=3)

        self.play_again_button = ttk.Button(root, text="Play Again", command=self.reset_game)
        self.play_again_button.grid(row=4, column=0, pady=10, columnspan=3)
        self.play_again_button.state(['disabled'])

    def play_game(self):
        user_choice = self.user_choice_var.get()
        if not user_choice:
            messagebox.showwarning("Warning", "Please choose Rock, Paper, or Scissors.")
            return

        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        
        self.display_result(user_choice, computer_choice)
        print(computer_choice)
    def display_result(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            result = "It's a tie!"
            
            messagebox.showinfo("Result", "It's a tie!")

        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You win!"
            messagebox.showinfo("Result", "You Win")
            self.user_score += 1

        else:
            result = "Computer wins!"
            messagebox.showinfo("Result", "You Lose")
            self.computer_score += 1

        self.result_label.config(text="User: {}   Computer: {}".format(user_choice, computer_choice))
        self.score_label.config(text="Score: User {} - {} Computer".format(self.user_score, self.computer_score))
        self.play_again_button.state(['!disabled'])

    def reset_game(self):
        self.user_choice_var.set("")
        self.result_label.config(text="")
        self.play_again_button.state(['disabled'])
        
# Main application loop

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()



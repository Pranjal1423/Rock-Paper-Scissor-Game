import tkinter as tk
import random
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x400")

# Define moves and their icons
moves = ["Rock", "Paper", "Scissors"]
move_icons = {
    "Rock": "✊",
    "Paper": "✋",
    "Scissors": "✌"
}

# Function to handle the game logic and update the interface
def play(player_choice):
    computer_choice = random.choice(moves)
    if player_choice == computer_choice:
        result = "It's a Tie!"
        root.config(bg="yellow")  # Change background to yellow
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win! 🎉"
        root.config(bg="green")  # Change background to green
    else:
        result = "You Lose! 😢"
        root.config(bg="red")  # Change background to red

    result_label.config(
        text=f"Computer chose: {move_icons[computer_choice]}\n{result}"
    )

# Title Label
title_label = tk.Label(
    root, text="Rock, Paper, Scissors", font=("Helvetica", 20, "bold"),
    bg="black", fg="white"
)
title_label.pack(pady=20, fill="x")

# Result Label
result_label = tk.Label(
    root, text="", font=("Helvetica", 16), bg="lightblue", fg="black"
)
result_label.pack(pady=20)

# Create Buttons for Player Choices
rock_button = tk.Button(
    root, text="✊ Rock", font=("Helvetica", 14), bg="blue", fg="white",
    width=15, command=lambda: play("Rock")
)
paper_button = tk.Button(
    root, text="✋ Paper", font=("Helvetica", 14), bg="blue", fg="white",
    width=15, command=lambda: play("Paper")
)
scissors_button = tk.Button(
    root, text="✌ Scissors", font=("Helvetica", 14), bg="blue", fg="white",
    width=15, command=lambda: play("Scissors")
)

# Arrange Buttons on the Window
rock_button.pack(pady=10)
paper_button.pack(pady=10)
scissors_button.pack(pady=10)

# Set default background color and run the main loop
root.config(bg="lightblue")
root.mainloop()

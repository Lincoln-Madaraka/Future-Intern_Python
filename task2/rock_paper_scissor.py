import random

def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "YOU WIN!"
    else:
        return "YOU LOSE!"

def rock_paper_scissors():
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        # Input validation
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        # Determine and print the result
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Exit the loop if the user wins
        if result == "YOU WIN!":
            break

rock_paper_scissors()


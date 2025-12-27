import random

# Initial scores
user_score = 0
computer_score = 0

print("=== Rock Paper Scissors Game ===")
print("Rules:")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")
print("-------------------------------")

while True:
    # User input
    user_choice = input("Enter your choice (rock / paper / scissors): ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.\n")
        continue

    # Computer choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Game logic
    if user_choice == computer_choice:
        print("Result: It's a tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("Result: You win!")
        user_score += 1

    else:
        print("Result: You lose!")
        computer_score += 1

    # Display score
    print(f"Score -> You: {user_score} | Computer: {computer_score}")

    # Play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    print()

    if play_again != "yes":
        print("Thanks for playing!")
        break

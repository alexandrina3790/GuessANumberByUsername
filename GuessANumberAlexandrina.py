import random
import time

bold_pink = "\033[1;35m"
reset_style = "\033[0m"

high_score = None

print(f"{bold_pink}Welcome to the Number Guessing Game!{reset_style}")

level = 1
min_number = 1
max_number = 100

while True:
    print(f"{bold_pink}Level {level} - Guess a number between {min_number} and {max_number}{reset_style}")

    print(f"{bold_pink}Choose your difficulty level:{reset_style}")
    print(f"{bold_pink}1. Easy (10 attempts){reset_style}")
    print(f"{bold_pink}2. Medium (7 attempts){reset_style}")
    print(f"{bold_pink}3. Hard (5 attempts){reset_style}")
    print(f"{bold_pink}4. Custom difficulty (choose attempts){reset_style}")

    while True:
        choice = input("Enter the number of your choice (1, 2, 3, or 4): ")
        if choice == "1":
            difficulty = 10
            break
        elif choice == "2":
            difficulty = 7
            break
        elif choice == "3":
            difficulty = 5
            break
        elif choice == "4":
            while True:
                custom_difficulty = input("Enter the number of attempts (between 5 and 20): ")
                if custom_difficulty.isdigit() and 5 <= int(custom_difficulty) <= 20:
                    difficulty = int(custom_difficulty)
                    break
                else:
                    print(f"{bold_pink}Please enter a valid number between 5 and 20.{reset_style}")
            break
        else:
            print(f"{bold_pink}Invalid choice. Please select 1, 2, 3, or 4.{reset_style}")

    computer_number = random.randint(min_number, max_number)
    remaining_attempts = difficulty

    start_time = time.time()

    print(f"{bold_pink}\nGuess the number between {min_number} and {max_number} (You have {remaining_attempts} attempts){reset_style}")

    while remaining_attempts > 0:
        player_input = input(f"Attempt {difficulty - remaining_attempts + 1}: Guess the number: ")

        if not player_input.isdigit():
            print(f"{bold_pink}Invalid input. Please enter a number.{reset_style}")
            continue

        player_number = int(player_input)

        if player_number == computer_number:
            end_time = time.time()
            elapsed_time = round(end_time - start_time, 2)
            print(f"{bold_pink}Congratulations! You guessed the number {computer_number} correctly in {elapsed_time} seconds!{reset_style}")

            if high_score is None or elapsed_time < high_score:
                high_score = elapsed_time
            break
        elif player_number > computer_number:
            print(f"{bold_pink}Too high! Try a smaller number.{reset_style}")
        else:
            print(f"{bold_pink}Too low! Try a larger number.{reset_style}")

        remaining_attempts -= 1

    if remaining_attempts == 0:
        print(f"{bold_pink}Sorry, you've used all your attempts! The correct number was {computer_number}.{reset_style}")

    print(f"{bold_pink}Your fastest time is: {high_score} seconds!{reset_style}")

    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again != "y":
        print(f"{bold_pink}Thanks for playing!{reset_style}")
        break

    print(f"{bold_pink}Level {level} complete!{reset_style}")
    level += 1
    min_number = max_number + 1
    max_number *= 2

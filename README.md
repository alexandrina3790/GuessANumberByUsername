# GuessANumberByAlexandrina
This is a simple console game "Guess A Number"

## Project Goals

The **Number Guessing Game** is a fun and interactive game that challenges players to guess a randomly generated number within a range of numbers. The game supports multiple difficulty levels, a custom difficulty option, and keeps track of the player's fastest time (high score). The game increases in difficulty with each level by expanding the range of numbers.

## Solution

The game is implemented in Python and uses the following key concepts:
- **Random number generation** to select a secret number within a specified range.
- **Timed game** to challenge players to guess the number as quickly as possible.
- **Difficulty levels** to adjust the number of attempts and the range of numbers.
- **High score tracking** to keep track of the fastest guess time.

### Libraries Used
- `random`: For generating random numbers.
- `time`: For tracking the time taken to guess the number.

The code is structured to provide:
- A choice of difficulty levels (easy, medium, hard) or a custom difficulty.
- A feature to track the fastest guess time and allow players to play multiple rounds.

## How the Game Works

1. The player is asked to choose a difficulty level:
   - Easy: 10 attempts
   - Medium: 7 attempts
   - Hard: 5 attempts
   - Custom: Choose a number of attempts between 5 and 20
2. The game generates a random number within the defined range and asks the player to guess it.
3. The player has a limited number of attempts to guess the number.
4. Feedback is provided after each guess (too high or too low).
5. The game tracks the fastest time it takes to guess the number correctly and displays it as the high score.
6. After completing a level, the difficulty increases by expanding the range of numbers.
7. The player can choose to play again or exit the game.


## Live Demo

Unfortunately, this game is a terminal-based game and doesn't have a live demo available for one-click play. However, you can clone or download the repository and run the game locally on your machine.

## How to Play

1. Clone or download the project from the repository.
2. Run the Python script.

# **🎯 Number Guessing Game (1–100)**

**This is a simple Python-based number guessing game where the player has to guess a randomly generated number between 1 and 100 within 7 attempts.**

---

## **📜 Game Rules**

- **You have 7 attempts to guess the correct number.**
- **The number to guess is between 1 and 100 (inclusive).**
- **Enter `Q` at any time to quit the game early.**
- **Entering a number outside 1–100 will end the game immediately.**
- **The game provides hints if your guess is too high or too low.**

---

## **▶️ How to Run**

Make sure you have Python installed. Then run the script from the terminal:

```bash
python guessing_game.py
```

> Replace `guessing_game.py` with your actual Python filename if different.

---

## **🧠 Sample Gameplay**

```
Rule 1: No. of attempts is 7
Rule 2: Guess no. only between 1-100
Guess the target number or Quit (Q): 50
Your guess is too small. Take a bigger guess
Guess the target number or Quit (Q): 75
You guessed too large. Take a smaller guess
Guess the target number or Quit (Q): 65
Congrats! You won
-----GAME OVER-----
```

---

## **📁 File Structure**

```
guessing_game.py     # Main game script
README.md            # Project description and instructions
```

---

## **🛠️ Features to Improve**

- Track and show the number of attempts used.
- Add input validation to handle non-integer values.
- Add a replay option after the game ends.
- Provide feedback if the game ends due to an invalid input.


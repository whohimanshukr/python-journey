# 🔢 Random Number Guessing Game – Mini Project #3

This is the third project in my **Python learning journey**.  
The Number Guessing Game is a console-based interactive game where the user tries to guess a randomly chosen number between 1 and 100.

Built using core Python fundamentals like:
- **while loops**
- **Conditional statements**
- **Random number generation** (`random.randint`)
- **Basic input/output formatting**
- No functions or advanced features used — kept simple and beginner-friendly 💡

---

## 🧠 Learning Objectives

- Practice while loops and looping logic
- Use if-elif-else for multi-branch decision making
- Introduce the random module
- Track attempts and give feedback

---

## 🚀 Features

- 🎲 Random number generated between 1–100
- 🤔 User guesses the number until it's correct
- ✅ Tracks and shows the number of attempts
- 📉 Feedback after each guess: “Too high” / “Too low”
- ❌ Handles out-of-range guesses (but no crash protection yet — see note below)

---

## 🖥️ Sample Output

```
Random Number Guessing Game
=============================================

======= Welcome to Random Number Guessing Game =======
I am guessing a number between 1-100
Can you guess it correctly
Let's Begin

Enter Your Guess(1,100): 23
Too Low!! Try again
Enter Your Guess(1,100): 78
Too High!! Try again
Enter Your Guess(1,100): 42
Congratulations!!!
You guessed the number correctly after 3 attempts

Thank You for choosing Random Number Guessing Game
```

---

## 📌 Notes

- ❗ This version assumes the user will enter valid integers only.
- 🛠 Exception handling (`try-except`) not yet added — will be updated in a future version after learning it.
- 🎯 Great beginner practice for understanding loop control and conditional logic.

---

## 📁 File Structure

📂 03_number_guessing/  
├── number_guessing.py  
└── README.md  

---

## 🧑‍💻 Built With

- Language: Python 3
- IDE: VS Code
- Concepts Used: Random module, While loop, If-Else conditions, User input

---

## 👨‍🎓 Author

> Built with 💻 by **Himanshu Kumar**  
> A beginner Pythonista building cool stuff one mini-project at a time  
> Join the journey → [📁 python-journey](https://github.com/whohimanshukr/python-journey)

---

## ✅ Project Status

> 📌 **Completed** — Built confidently without exception handling (for now), and ready for future upgrades 🔄


# Quizgame-PierreLouisBRUN-CDOF4
It's a Quiz Game

# Quiz Program

This is a simple Python-based quiz program that asks users multiple-choice questions on general knowledge. Users can select their answers from four options, and the program provides feedback on whether their answer is correct.

## Features

- **Randomized questions**: The order of questions is shuffled to make the quiz more engaging.
- **Multiple-choice options**: Each question offers four possible answers.
- **Score tracking**: The program calculates and displays the user's score at the end of the quiz.

## Requirements

- Python 3.6 or later

## How to Use

1. Clone the repository or copy the script to your local machine.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using the command:
   ```bash
   python quiz_program.py
   ```
4. Answer the questions by entering the number corresponding to your choice (1-4).
5. At the end of the quiz, your score will be displayed.

## Example

```
Question 1: What is the largest country in the world by area?
1) China
2) United States
3) Russia
4) Canada
Your answer (1-4): 3
Correct answer!

You have completed the quiz! Your score is 3/3.
```

## Customization

To add more questions, edit the `questions` list in the script. Each question should be added as a dictionary with the following structure:

```python
{
    "question": "Your question text here",
    "options": ["1) Option 1", "2) Option 2", "3) Option 3", "4) Option 4"],
    "correct": <correct option number>
}
```

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

---

Happy quizzing to all the players !
Please leave a star if you enjoyed !



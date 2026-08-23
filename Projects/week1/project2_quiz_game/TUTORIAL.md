# Project 2: Quiz Game Engine
**Week 1 Capstone — Topics: Basics, Conditionals, Sequences, Strings, Iteration, Dictionaries, Functions**

## Goal
Build a multiple-choice quiz game that asks questions from a data set,
scores the user, and shows results at the end.

## What You'll Practice
- Lists of dictionaries as a mini "database" of questions
- Loops to iterate through questions
- Conditionals to check answers
- Functions to organize each piece of logic (ask, score, report)
- String methods to make input matching forgiving (case-insensitive)

## Requirements

1. Store your questions as a list of dictionaries, e.g.:
   ```python
   QUESTIONS = [
       {
           "question": "What data type is used for True/False values?",
           "options": {"A": "int", "B": "bool", "C": "str", "D": "float"},
           "answer": "B",
           "category": "basics",
       },
       ...
   ]
   ```
2. Write a function `ask_question(question_dict)` that:
   - prints the question and its options
   - takes user input (A/B/C/D)
   - returns `True` if correct, `False` if not
3. Write a function `run_quiz(questions)` that:
   - loops through every question
   - keeps a running score
   - returns the final score
4. Write a function `show_results(score, total)` that prints a summary
   message (e.g. "You got 4/5 — Great job!") with different messages
   depending on the percentage correct.
5. (Bonus) Let the user pick a category before the quiz starts, and filter
   `QUESTIONS` down to just that category.

## Step-by-Step Guide

### Step 1 — Build your question bank
Write at least 5 questions as dictionaries in a list.

### Step 2 — Ask a single question
```python
def ask_question(q):
    print(q["question"])
    for key, option in q["options"].items():
        print(f"  {key}. {option}")
    answer = input("Your answer: ").strip().upper()
    return answer == q["answer"]
```

### Step 3 — Loop through all questions
```python
def run_quiz(questions):
    score = 0
    for q in questions:
        if ask_question(q):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer was {q['answer']}.\n")
    return score
```

### Step 4 — Show a results summary
Use conditionals to give different feedback based on percentage score
(e.g. `>= 80%` → "Excellent!", `>= 50%` → "Not bad!", else → "Keep practicing!").

### Step 5 — Tie it together in `main()`

## Stretch Goals (optional)
- Add a timer per question (using the `time` module).
- Shuffle question order each run using `random.shuffle()`.
- Track wrong answers and print a "review" list at the end.

## Testing Checklist
- [ ] Lowercase answers (e.g. "b") are accepted, not just uppercase
- [ ] An invalid option (e.g. "Z") is treated as wrong, not a crash
- [ ] The score is correct at the end (test by getting all right / all wrong)
- [ ] Results message changes appropriately based on score

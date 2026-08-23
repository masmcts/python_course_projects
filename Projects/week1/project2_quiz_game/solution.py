"""
Project 2: Quiz Game Engine - SOLUTION
Week 1 Capstone: Basics, Conditionals, Sequences, Strings, Iteration, Dictionaries, Functions
"""

QUESTIONS = [
    {
        "question": "What data type is used for True/False values?",
        "options": {"A": "int", "B": "bool", "C": "str", "D": "float"},
        "answer": "B",
        "category": "basics",
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": {"A": "func", "B": "define", "C": "def", "D": "function"},
        "answer": "C",
        "category": "functions",
    },
    {
        "question": "What does len([1, 2, 3]) return?",
        "options": {"A": "2", "B": "3", "C": "1", "D": "Error"},
        "answer": "B",
        "category": "sequences",
    },
    {
        "question": "Which method converts a string to lowercase?",
        "options": {"A": ".lower()", "B": ".down()", "C": ".small()", "D": ".min()"},
        "answer": "A",
        "category": "strings",
    },
    {
        "question": "How do you access the value for key 'x' in dict d?",
        "options": {"A": "d.x", "B": "d['x']", "C": "d(x)", "D": "d->x"},
        "answer": "B",
        "category": "dictionaries",
    },
]


def ask_question(q):
    """Print a question and its options, take input, return True if correct."""
    print(q["question"])
    for key, option in q["options"].items():
        print(f"  {key}. {option}")

    answer = input("Your answer: ").strip().upper()
    return answer == q["answer"]


def run_quiz(questions):
    """Loop through all questions, tracking and returning the score."""
    score = 0
    for q in questions:
        if ask_question(q):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer was {q['answer']}.\n")
    return score


def show_results(score, total):
    """Print a summary message based on the percentage of correct answers."""
    percent = (score / total) * 100 if total else 0
    print(f"\nYou scored {score}/{total} ({percent:.0f}%)")

    if percent >= 80:
        print("Excellent work!")
    elif percent >= 50:
        print("Not bad — a little more practice and you'll master it.")
    else:
        print("Keep practicing, you'll get there!")


def filter_by_category(questions, category):
    """Return only the questions matching the given category (case-insensitive)."""
    return [q for q in questions if q["category"].lower() == category.lower()]


def main():
    print("=== Welcome to the Quiz! ===")
    categories = sorted(set(q["category"] for q in QUESTIONS))
    print(f"Available categories: {', '.join(categories)} (or press Enter for all)")

    choice = input("Pick a category: ").strip()
    if choice:
        questions = filter_by_category(QUESTIONS, choice)
        if not questions:
            print(f"No questions found for '{choice}'. Using all questions instead.")
            questions = QUESTIONS
    else:
        questions = QUESTIONS

    score = run_quiz(questions)
    show_results(score, len(questions))


if __name__ == "__main__":
    main()

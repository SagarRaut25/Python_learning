# Math Quiz Game with Functions


import random

def ask_question(question, options, correct_option):
    """
    This function asks a question and returns True if answer is correct, else False.
    """
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    answer = input("Enter the option number (1-4): ")
    
    # Convert input to integer
    if answer.isdigit():
        answer = int(answer)

    else:
        print("Invalid input! Counting as wrong.")
        return False
    
    if answer == correct_option:
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Wrong! Correct answer was {options[correct_option - 1]}")
        return False

def start_quiz():
    """
    This function runs the quiz.
    """
    questions = [
        {
            "question": "What is 5 + 7?",
            "options": ["10", "11", "12", "13"],
            "answer": 3
        },

        {
            "question": "What is 9 - 4?",
            "options": ["5", "6", "7", "4"],
            "answer": 1
        },

        {
            "question": "What is 6 x 3?",
            "options": ["18", "16", "20", "15"],
            "answer": 1
        },
        {
            "question": "What is 15 ÷ 3?",
            "options": ["3", "5", "6", "4"],
            "answer": 2
        },
        {
            "question": "What is 7 + 8?",
            "options": ["14", "15", "16", "17"],
            "answer": 2
        }
    ]
    
    score = 0
    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            score += 1

    print(f"\n🎉 Quiz Over! Your Score: {score}/{len(questions)}")

while True: # Main loop

    print("\n🎓 Welcome to the Math Quiz Game!")
    start_quiz()

    play_again = input("Do you want to play again? (yes/no): ").lower()
    
    if play_again != "yes":
        print("Thank you for playing the Math Quiz Game! Goodbye 👋")
        break
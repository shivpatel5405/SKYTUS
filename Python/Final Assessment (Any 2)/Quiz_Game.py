# Quiz Game

import random
import time

questions = {
    "Python": [
        {"question": "Who created the Python programming language?",
         "options": ["a) James Gosling", "b) Guido van Rossum",
                      "c) Bjarne Stroustrup", "d) Dennis Ritchie"], "answer": "b"},
        {"question": "Which keyword is used to define a function in Python?",
         "options": ["a) func", "b) function", "c) def", "d) define"], "answer": "c"},
        {"question": "What is the output of: print(type(10))?",
         "options": ["a) <class 'float'>", "b) <class 'int'>",
                      "c) <class 'str'>", "d) <class 'number'>"], "answer": "b"},
        {"question": "Which data structure uses key-value pairs in Python?",
         "options": ["a) List", "b) Tuple", "c) Set", "d) Dictionary"], "answer": "d"},
        {"question": "What does 'pip' stand for in Python?",
         "options": ["a) Python Install Package", "b) Pip Installs Packages",
                      "c) Package In Python", "d) Python Integrated Platform"], "answer": "b"},
    ],
    "Java": [
        {"question": "Who developed the Java programming language?",
         "options": ["a) Dennis Ritchie", "b) Guido van Rossum",
                      "c) James Gosling", "d) Bjarne Stroustrup"], "answer": "c"},
        {"question": "What is the entry point method of a Java program?",
         "options": ["a) start()", "b) run()", "c) main()", "d) init()"], "answer": "c"},
        {"question": "Which keyword is used to inherit a class in Java?",
         "options": ["a) implements", "b) inherits", "c) extends", "d) super"], "answer": "c"},
        {"question": "What does JVM stand for?",
         "options": ["a) Java Virtual Machine", "b) Java Variable Method",
                      "c) Java Visual Manager", "d) Java Version Module"], "answer": "a"},
        {"question": "Which of these is NOT a primitive data type in Java?",
         "options": ["a) int", "b) boolean", "c) String", "d) char"], "answer": "c"},
    ],
    "C/C++": [
        {"question": "Who created the C programming language?",
         "options": ["a) James Gosling", "b) Bjarne Stroustrup",
                      "c) Dennis Ritchie", "d) Guido van Rossum"], "answer": "c"},
        {"question": "Which symbol is used to access a pointer's value in C?",
         "options": ["a) &", "b) *", "c) #", "d) @"], "answer": "b"},
        {"question": "What does 'cout' do in C++?",
         "options": ["a) Takes input", "b) Declares a variable",
                      "c) Prints output", "d) Ends the program"], "answer": "c"},
        {"question": "Which header file is needed for printf() in C?",
         "options": ["a) <stdlib.h>", "b) <conio.h>",
                      "c) <stdio.h>", "d) <string.h>"], "answer": "c"},
        {"question": "What is the size of 'int' in C on most 32-bit systems?",
         "options": ["a) 1 byte", "b) 2 bytes", "c) 4 bytes", "d) 8 bytes"], "answer": "c"},
    ],
    "Web Development": [
        {"question": "What does HTML stand for?",
         "options": ["a) Hyper Text Markup Language", "b) High Tech Modern Language",
                      "c) Hyper Transfer Markup Language", "d) Home Tool Markup Language"], "answer": "a"},
        {"question": "Which language is used to style web pages?",
         "options": ["a) HTML", "b) Python", "c) CSS", "d) SQL"], "answer": "c"},
        {"question": "What does the 'DOM' stand for in web development?",
         "options": ["a) Data Object Model", "b) Document Object Model",
                      "c) Digital Output Mode", "d) Display Object Manager"], "answer": "b"},
        {"question": "Which tag is used to add JavaScript in HTML?",
         "options": ["a) <js>", "b) <code>", "c) <script>", "d) <java>"], "answer": "c"},
        {"question": "What does CSS 'flexbox' help with?",
         "options": ["a) Database queries", "b) Page layout and alignment",
                      "c) Server routing", "d) Image editing"], "answer": "b"},
    ],
    "General Programming": [
        {"question": "What does 'IDE' stand for?",
         "options": ["a) Integrated Development Environment", "b) Internal Data Engine",
                      "c) Internet Development Editor", "d) Inline Debug Executor"], "answer": "a"},
        {"question": "Which data structure follows LIFO (Last In, First Out)?",
         "options": ["a) Queue", "b) Array", "c) Stack", "d) Linked List"], "answer": "c"},
        {"question": "What is the time complexity of binary search?",
         "options": ["a) O(n)", "b) O(n^2)", "c) O(log n)", "d) O(1)"], "answer": "c"},
        {"question": "What does 'API' stand for?",
         "options": ["a) Application Programming Interface", "b) Automated Program Interaction",
                      "c) Application Process Integration", "d) Advanced Programming Input"], "answer": "a"},
        {"question": "Which of these is a version control system?",
         "options": ["a) Docker", "b) Git", "c) Node.js", "d) MongoDB"], "answer": "b"},
    ]
}


# ---------- Functions ----------

def display_welcome():
    """Display the welcome screen."""
    print()
    print("=" * 50)
    print("|                                                |")
    print("|     * PROGRAMMING LANGUAGE QUIZ GAME *         |")
    print("|                                                |")
    print("|   Test your coding knowledge and win points!   |")
    print("|   Answer fast and build streaks!               |")
    print("|                                                |")
    print("=" * 50)
    print()


def show_categories():
    """Display available categories and let the player choose."""
    print("Choose a category:")
    print("-" * 30)

    category_list = list(questions.keys())
    for i in range(len(category_list)):
        count = len(questions[category_list[i]])
        print(f"  {i + 1}) {category_list[i]}  ({count} questions)")

    print(f"  {len(category_list) + 1}) Mix of All")
    print("-" * 30)

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(category_list) + 1:
                break
            else:
                print(f"Please enter a number between 1 and {len(category_list) + 1}.")
        except ValueError:
            print("Please enter a valid number.")

    if choice == len(category_list) + 1:
        # Mix all categories
        all_questions = []
        for cat in questions:
            for q in questions[cat]:
                q_copy = dict(q)
                q_copy["category"] = cat
                all_questions.append(q_copy)
        return "Mix of All", all_questions
    else:
        cat_name = category_list[choice - 1]
        cat_questions = []
        for q in questions[cat_name]:
            q_copy = dict(q)
            q_copy["category"] = cat_name
            cat_questions.append(q_copy)
        return cat_name, cat_questions



def ask_question(q_number, total, q_data, streak):
    """
    Display a question and get the answer.
    Returns: (is_correct, time_taken)
    """
    print(f"  [{q_data['category']}]")
    print(f"  Question {q_number} of {total}")
    if streak >= 2:
        print(f"  >> Streak: {streak} in a row! (x{min(streak, 5)} bonus)")
    print()
    print(f"  {q_data['question']}")
    print()

    for opt in q_data["options"]:
        print(f"    {opt}")

    print()
    start_time = time.time()

    while True:
        answer = input("  Your answer: ").lower().strip()

        if answer in ["a", "b", "c", "d"]:
            break
        else:
            print("  Invalid! Enter a, b, c, or d.")

    end_time = time.time()
    time_taken = round(end_time - start_time, 1)

    is_correct = (answer == q_data["answer"])

    return is_correct, time_taken


def show_feedback(is_correct, q_data, time_taken, points_earned):
    """Show whether the answer was right or wrong."""
    if is_correct:
        print(f"  >> Correct! (+{points_earned} pts)  [{time_taken}s]")
    else:
        # Find the full correct option text
        correct_text = ""
        for opt in q_data["options"]:
            if opt.startswith(q_data["answer"] + ")"):
                correct_text = opt
                break
        print(f"  >> Wrong! The answer was: {correct_text}  [{time_taken}s]")


def show_scoreboard(name, score, correct, total, streak_best, time_total, category):
    """Display the final results."""
    percentage = round((correct / total) * 100)

    print()
    print("=" * 50)
    print("|              QUIZ RESULTS                      |")
    print("=" * 50)
    print(f"  Player      : {name}")
    print(f"  Category    : {category}")
    print(f"  Score       : {score} points")
    print(f"  Correct     : {correct} / {total}  ({percentage}%)")
    print(f"  Best Streak : {streak_best} in a row")
    print(f"  Total Time  : {time_total}s")
    print("-" * 50)

    # Progress bar
    filled = int(percentage / 5)  # out of 20 blocks
    empty = 20 - filled
    bar = "[" + "#" * filled + "." * empty + "]"
    print(f"  {bar}  {percentage}%")
    print("-" * 50)

    # Rank
    if percentage == 100:
        print("  Rank: QUIZ MASTER -- Perfect score!")
    elif percentage >= 80:
        print("  Rank: EXPERT -- Impressive knowledge!")
    elif percentage >= 60:
        print("  Rank: GOOD -- Well done, keep going!")
    elif percentage >= 40:
        print("  Rank: AVERAGE -- Room for improvement.")
    else:
        print("  Rank: BEGINNER -- Keep learning!")

    print("=" * 50)
    print()


# ---------- Main Game ----------

def play_quiz():
    """Run the quiz game."""
    playing = True

    while playing:
        display_welcome()

        name = input("Enter your name: ").strip()
        if name == "":
            name = "Player"
        print(f"\nHello {name}! Let's begin.\n")

        # Choose category
        category, selected_questions = show_categories()
        print()

        # Shuffle questions
        random.shuffle(selected_questions)

        # Choose number of questions
        max_q = len(selected_questions)
        while True:
            try:
                num = int(input(f"How many questions? (1 to {max_q}): "))
                if 1 <= num <= max_q:
                    break
                else:
                    print(f"Enter a number between 1 and {max_q}.")
            except ValueError:
                print("Enter a valid number.")

        selected_questions = selected_questions[:num]
        print()

        # Game variables
        score = 0
        correct_count = 0
        streak = 0
        streak_best = 0
        total_time = 0

        # Ask each question
        for i in range(num):
            print("-" * 50)
            is_correct, time_taken = ask_question(
                i + 1, num, selected_questions[i], streak
            )

            total_time += time_taken
        
            # Calculate points
            if is_correct:
                correct_count += 1
                streak += 1
                if streak > streak_best:
                    streak_best = streak

                # Bonus points for streaks (max x5)
                multiplier = min(streak, 5)
                points = 10 * multiplier

                # Speed bonus: under 5 seconds
                if time_taken < 5:
                    points += 5
                    show_feedback(True, selected_questions[i], time_taken, points)
                    print("  >> Speed bonus! +5 pts")
                else:
                    show_feedback(True, selected_questions[i], time_taken, points)

                score += points
            else:
                streak = 0
                show_feedback(False, selected_questions[i], time_taken, 0)

            print(f"  >> Score so far: {score} pts")
            print()

            # Pause between questions
            if i < num - 1:
                input("  Press Enter for the next question...")
                print()

        # Final results
        total_time = round(total_time, 1)
        show_scoreboard(name, score, correct_count, num, streak_best, total_time, category)

        # Play again?
        again = input("Play again? (yes/no): ").lower().strip()
        if again in ["yes", "y"]:
            print()
        else:
            print(f"\nThanks for playing, {name}! See you next time!\n")
            playing = False


# ---------- Start the Game ----------
play_quiz()

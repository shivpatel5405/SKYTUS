# 🎮 Programming Language Quiz Game

A terminal-based multiple-choice quiz game built in Python that tests your knowledge across **five programming categories**. Answer quickly, build streaks, and climb the ranks!

---

## 📋 Table of Contents

- [Features](#features)
- [Categories](#categories)
- [How to Run](#how-to-run)
- [How to Play](#how-to-play)
- [Scoring System](#scoring-system)
- [Ranking System](#ranking-system)
- [Project Structure](#project-structure)
- [Requirements](#requirements)

---

## ✨ Features

- **5 Quiz Categories** — Python, Java, C/C++, Web Development, and General Programming
- **25 Curated Questions** — 5 questions per category, all with 4 multiple-choice options
- **Mix Mode** — Combine all categories into a single randomized quiz
- **Streak System** — Consecutive correct answers earn bonus multipliers (up to x5)
- **Speed Bonus** — Answer in under 5 seconds for extra points
- **Live Score Tracking** — See your score update after every question
- **Performance Ranking** — Get ranked from Beginner to Quiz Master
- **Visual Progress Bar** — ASCII progress bar showing your accuracy
- **Replay Support** — Play multiple rounds without restarting the program
- **Customizable Length** — Choose how many questions you want per round

---

## 📚 Categories

| #   | Category              | Questions |
| --- | --------------------- | --------- |
| 1   | Python                | 5         |
| 2   | Java                  | 5         |
| 3   | C/C++                 | 5         |
| 4   | Web Development       | 5         |
| 5   | General Programming   | 5         |
| 6   | Mix of All            | 25        |

---

## 🚀 How to Run

**Prerequisites:** Python 3.x

```bash
python Quiz_Game.py
```

No external libraries are required — the game uses only the built-in `random` and `time` modules.

---

## 🕹️ How to Play

1. **Enter your name** when prompted
2. **Select a category** (1–5) or choose **Mix of All** (6)
3. **Choose how many questions** you'd like to answer
4. **Answer each question** by typing `a`, `b`, `c`, or `d`
5. **Press Enter** to advance to the next question
6. **View your final scoreboard** with rank, accuracy, and stats
7. **Choose to play again** or exit

---

## 🏆 Scoring System

| Mechanic         | Points                        | Details                                      |
| ---------------- | ----------------------------- | -------------------------------------------- |
| Correct Answer   | 10 × streak multiplier       | Base 10 pts, multiplied by current streak    |
| Streak Bonus     | Up to x5 multiplier          | Builds with consecutive correct answers      |
| Speed Bonus      | +5 pts                       | Awarded for answering in under 5 seconds     |
| Wrong Answer     | 0 pts                        | Resets the streak counter to 0               |

### Streak Multiplier Example

| Streak | Multiplier | Base Points |
| ------ | ---------- | ----------- |
| 1      | x1         | 10 pts      |
| 2      | x2         | 20 pts      |
| 3      | x3         | 30 pts      |
| 4      | x4         | 40 pts      |
| 5+     | x5 (max)   | 50 pts      |

---

## 🎖️ Ranking System

| Accuracy   | Rank          |
| ---------- | ------------- |
| 100%       | Quiz Master   |
| 80 – 99%   | Expert        |
| 60 – 79%   | Good          |
| 40 – 59%   | Average       |
| 0 – 39%    | Beginner      |

---

## 📁 Project Structure

```
Final Assessment (Any 2)/
├── Quiz_Game.py            # Main game script
└── README_Quiz_Game.md     # This file
```

### Key Functions

| Function             | Description                                         |
| -------------------- | --------------------------------------------------- |
| `display_welcome()`  | Renders the ASCII welcome banner                    |
| `show_categories()`  | Lists categories and handles player selection       |
| `ask_question()`     | Displays a question, captures input, tracks time    |
| `show_feedback()`    | Shows correct/incorrect feedback with points earned |
| `show_scoreboard()`  | Displays final results, progress bar, and rank      |
| `play_quiz()`        | Main game loop orchestrating the full quiz flow     |

---

## 📦 Requirements

- **Python** 3.x
- **Modules:** `random`, `time` (both part of the Python standard library)

No installation of third-party packages is needed.

---

## 📝 License

This project was created as part of a Python Final Assessment.

# 🎮 Python Games Collection

Welcome to your first Python game project! This repository contains a collection of fun games that demonstrate various Python programming concepts.

## 🎯 Games Included

### 1. Snake Game 🐍
- Classic Snake game with modern graphics
- Uses pygame for smooth gameplay
- Features score tracking and game over detection
- Demonstrates: game loops, collision detection, event handling

### 2. Tic-Tac-Toe ⭕❌
- Console-based Tic-Tac-Toe game
- Two-player gameplay
- Input validation and game state management
- Demonstrates: 2D arrays, game logic, user input

### 3. Number Guessing Game 🎲
- Interactive number guessing game
- Difficulty levels and hints
- Score tracking and statistics
- Demonstrates: random numbers, loops, conditionals

## 🚀 Getting Started

1. **Activate your virtual environment:**
   ```bash
   # On Windows
   venv\Scripts\activate
   
   # On Mac/Linux
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game launcher:**
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
Brian-s-first/
├── games/
│   ├── __init__.py
│   ├── snake_game.py      # Snake game implementation
│   ├── tic_tac_toe.py     # Tic-tac-toe game
│   └── number_guess.py    # Number guessing game
├── utils/
│   ├── __init__.py
│   ├── colors.py          # Color constants
│   └── helpers.py         # Utility functions
├── assets/                # Game assets (images, sounds)
├── main.py               # Game launcher
├── requirements.txt      # Dependencies
└── README.md            # This file
```

## 🎮 How to Play

### Snake Game
- Use arrow keys to control the snake
- Eat food to grow and increase score
- Avoid hitting walls or yourself
- Press ESC to quit

### Tic-Tac-Toe
- Enter row and column numbers (1-3)
- Try to get three in a row
- Play against a friend!

### Number Guessing
- Choose difficulty level
- Guess the secret number
- Use hints to help you win

## 🛠️ Python Concepts Demonstrated

- **Object-Oriented Programming**: Classes and methods
- **Game Development**: Game loops, collision detection
- **User Interface**: Console input/output, pygame graphics
- **Data Structures**: Lists, dictionaries, 2D arrays
- **Control Flow**: Loops, conditionals, functions
- **Error Handling**: Input validation, exception handling
- **File Organization**: Modules, packages, imports

## 🎨 Future Enhancements

- Add sound effects and music
- Create a high score system
- Add more games (Pong, Tetris, etc.)
- Implement multiplayer features
- Add graphics and animations

Have fun coding and gaming! 🎉

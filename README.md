# Tic Tac Toe

A simple Tic Tac Toe game built with Python and PyQt5. The two players are a red middle finger and a blue middle finger.

## Features

- 3x3 board built with a grid layout and 9 buttons
- Each button works only once
- Turns alternate using odd and even move counts
- SVG icons for both players
- Sound effects for moves, wins and draws
- Winning line highlight and restart button

## Project Structure

```
tictactoe/
├── assets/
│   ├── finger_red.svg
│   ├── finger_blue.svg
│   ├── move.wav
│   ├── win.wav
│   └── draw.wav
├── game_logic.py
├── gui.py
├── .gitignore
└── README.md
```

## Installation

```
pip install PyQt5
```

## Run

```
python gui.py
```

## How It Works

`game_logic.py` stores the moves of each player and loops through the winning cases of that player after every move. If every cell of a case belongs to the player, that player wins. If nine moves are played with no winner, the game is a draw.

`gui.py` draws the board, sets the finger icon on the pressed button, plays sounds and shows the game status.

import sys
from pathlib import Path

from PyQt5.QtCore import QSize, Qt, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from game_logic import TicTacToe

ASSETS = Path(__file__).parent / "assets"

PLAYER_NAMES = {
    "RED": "Red",
    "BLUE": "Blue",
}


def load_sound(name):
    effect = QSoundEffect()
    effect.setSource(QUrl.fromLocalFile(str(ASSETS / name)))
    effect.setVolume(0.6)
    return effect


class TicTacToeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.game = TicTacToe()
        self.icons = {
            "RED": QIcon(str(ASSETS / "finger_red.svg")),
            "BLUE": QIcon(str(ASSETS / "finger_blue.svg")),
        }
        self.sounds = {
            "move": load_sound("move.wav"),
            "win": load_sound("win.wav"),
            "draw": load_sound("draw.wav"),
        }
        self.buttons = []
        self.build_ui()
        self.update_status()



    def build_ui(self):
        self.setWindowTitle("Tic Tac Toe")
        self.setWindowIcon(QIcon(str(ASSETS / "finger_red.svg")))

        layout = QVBoxLayout(self)

        self.status = QLabel()
        self.status.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status)

        grid = QGridLayout()
        for index in range(9):
            row = index // 3
            column = index % 3

            button = QPushButton()
            button.setFixedSize(100, 100)
            button.setIconSize(QSize(70, 70))

            handler = self.make_click_handler(index)
            button.clicked.connect(handler)

            grid.addWidget(button, row, column)
            self.buttons.append(button)
        layout.addLayout(grid)

        restart_button = QPushButton("Restart")
        restart_button.clicked.connect(self.restart)
        layout.addWidget(restart_button)


    def make_click_handler(self, index):
        def handler():
            self.on_cell_clicked(index)

        return handler



    def on_cell_clicked(self, index):
        player = self.game.current_player
        move_accepted = self.game.play(index)
        if not move_accepted:
            return
        self.buttons[index].setIcon(self.icons[player])
        self.after_move()



    def after_move(self):
        if self.game.winner is not None:
            self.highlight(self.game.winning_line)
            self.sounds["win"].play()
        elif self.game.is_draw:
            self.sounds["draw"].play()
        else:
            self.sounds["move"].play()
        self.update_status()



    def highlight(self, line):
        for index in line:
            self.buttons[index].setStyleSheet("background-color: lightgreen;")



    def update_status(self):
        if self.game.winner is not None:
            name = PLAYER_NAMES[self.game.winner]
            self.status.setText(name + " wins!")
        elif self.game.is_draw:
            self.status.setText("Draw!")
        else:
            name = PLAYER_NAMES[self.game.current_player]
            self.status.setText(name + "'s turn")



    def restart(self):
        self.game.reset()
        for button in self.buttons:
            button.setIcon(QIcon())
            button.setStyleSheet("")
        self.update_status()


def main():
    app = QApplication(sys.argv)
    window = TicTacToeWindow()
    window.show()
    exit_code = app.exec_()
    sys.exit(exit_code)



if __name__ == "__main__":
    main()

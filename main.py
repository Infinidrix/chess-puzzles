from model import Model
from config import SAVE_SVG, OPEN_IN_LICHESS

import chess.svg
import subprocess, os, platform, webbrowser

def save_board(filepath, board):
    with open("game.svg", 'w') as f:
        f.write(chess.svg.board(board))
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':    # Windows
        os.startfile(filepath)
    else:                                   # linux variants
        subprocess.call(('xdg-open', filepath))
rounds = 1
for i in range(rounds):
    model = Model()
    best_board = model.get_best_board()
    print("\n" + best_board.fen())
    print(best_board)
    if SAVE_SVG:
        save_board("game.svg", best_board)
    if OPEN_IN_LICHESS:
        webbrowser.open(f"https://lichess.org/analysis/fromPosition/{best_board.fen().replace(' ', '_')}")

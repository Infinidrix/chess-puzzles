import chess
import chess.engine
from utils import array_to_chess_board
from config import PIECE_PENALTY, PIECE_COUNT_PENALTY, MOVES_RANGE, CHESS_ENGINE_PATH

class CostFunction():

    def __init__(self):
        self.engine = chess.engine.SimpleEngine.popen_uci(CHESS_ENGINE_PATH)
    
    def piece_penalty(self, board):
        penalty = 0
        for (piece, color), pen in PIECE_PENALTY.items():
            penalty += (len(board.pieces(piece, color)) * pen)
        return penalty

    def noise_penalty(self, board):
        return len(board.piece_map()) * PIECE_COUNT_PENALTY

    def f(self, X):
        board = array_to_chess_board(X)
        penalty = len(board.piece_map()) * 0.1

        # Penalize invalid boards heavily, we cannot even analyze them
        if not board.is_valid():
            return 10 + penalty


        penalty += self.piece_penalty(board)
        penalty += self.noise_penalty(board)

        # You can tune the depth for performance reasons
        info = self.engine.analyse(board, chess.engine.Limit(depth=8), multipv=2)

        # If there are no moves (meaning the game is over), return a high penalty
        if len(info) < 1:
            return 9 + penalty

        # Also heavily penalize having only 1 move, puzzles are only interesting
        #   if we have a choice to make
        if len(info) < 2:
            return 8 + penalty

        # We're specifically looking for puzzles where White can mate in 3 moves
        #   so we'll penalize cases where white does not have a forced mate
        score = info[0]["score"].white()
        if not score.is_mate() or score.mate() <= 0:
            return 6 + penalty

        # Add a penalty for the distance away from mate in 3
        if not(MOVES_RANGE['low'] <= score.mate() <= MOVES_RANGE['high']):
            avg = (MOVES_RANGE['low'] + MOVES_RANGE['high']) / 2
            penalty += min(3, abs(score.mate() - avg)) / avg

        # Finally, add a high penalty if the second best move is also good.
        # The defining characteristic of a puzzle is that the second best move is bad
        second_move_score = info[1]["score"].white().score(mate_score=1000)
        if second_move_score > 100:
            penalty += min(10.0, second_move_score / 100)

        return penalty
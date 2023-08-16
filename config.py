import chess

# should the output be saved as an svg file and opened.
SAVE_SVG = False
# (recommended) should the puzzle be shown on lichess.com
OPEN_IN_LICHESS = True

# which pieces should be avoided/encouraged
PIECE_PENALTY = {
    (chess.KNIGHT, chess.WHITE): -0.02,
    (chess.BISHOP, chess.WHITE): 0.0,
    (chess.ROOK, chess.WHITE): 0.0,
    (chess.QUEEN, chess.WHITE): 0.1,
    (chess.KING, chess.WHITE): 0.0,
    (chess.PAWN, chess.WHITE): 0.0,
    (chess.PAWN, chess.BLACK): 0.0,
    (chess.KING, chess.BLACK): 0.0,
    (chess.QUEEN, chess.BLACK): 0.0,
    (chess.ROOK, chess.BLACK): 0.0,
    (chess.BISHOP, chess.BLACK): 0.0,
    (chess.KNIGHT, chess.BLACK): -0.01,
}

# penalty for each piece (keeps the board from being cluttered)
PIECE_COUNT_PENALTY = 0.15
# the number of moves till mate
MOVES_RANGE = {"low": 3, "high": 3}
# the dir path to stockfish
CHESS_ENGINE_PATH = "C:\\Users\\sebir\\Downloads\\stockfish-windows-x86-64-avx2\\stockfish\\stockfish-windows-x86-64-avx2"

# genetic algorithm params (increase max_num_iteration for better results at the expense of time).
ALGORITHM_PARAMS = {'max_num_iteration': 50000,
                   'population_size': 20,
                   'mutation_probability': 0.07,
                   'elit_ratio': 0.01,
                   'parents_portion': 0.3,
                   'crossover_type': 'two_point',
                   'max_iteration_without_improv': 5000}
                   
# minimum penalty for a good enough puzzle (to save additional computation)
GOOD_ENOUGH_SCORE = 2.5
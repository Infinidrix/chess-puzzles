import chess

def value_to_piece(value):
    if value == 0:
        return None
    elif value <= 6:
        # Pieces have values 1 through 6
        return chess.Piece(value, chess.WHITE)
    else:
        return chess.Piece(value - 6, chess.BLACK)

def array_to_chess_board(arr):
    # construct an empty chess board
    board = chess.Board(fen='8/8/8/8/8/8/8/8 w - - 0 1')
    for i, value in enumerate(arr):
        piece = value_to_piece(value)
        if piece:
            board.set_piece_at(i, piece)
    return board
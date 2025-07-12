"""
AI.py

This module contains the AI logic for selecting moves in a chess game.
*Main contribution:* Improved evaluate() function to better assess board states.

Author: [Your Name]

Note: This file builds on provided starter code. My work focuses on developing
a more effective evaluation function to enhance the playing strength of the AI.
"""

def evaluate(board):
    """
    Evaluates the given board state and returns a numerical score.
    Positive scores favor white; negative scores favor black.

    Args:
        board (ChessBoard): Current state of the chess game.

    Returns:
        int: Evaluation score.
    """
    # Piece values
    piece_values = {
        'P': 1,
        'N': 3,
        'B': 3,
        'R': 5,
        'Q': 9,
        'K': 0
    }

    score = 0

    for row in board.tiles:
        for tile in row:
            piece = tile.piece
            if piece and not piece.is_null():
                value = piece_values.get(piece.name.upper(), 0)
                if piece.color == "white":
                    score += value
                else:
                    score -= value

    # Custom heuristics
    # Example: encourage central control
    central_squares = [(3,3), (3,4), (4,3), (4,4)]
    for r, c in central_squares:
        piece = board.tiles[r][c].piece
        if piece and not piece.is_null():
            if piece.color == "white":
                score += 0.5
            else:
                score -= 0.5

    return score

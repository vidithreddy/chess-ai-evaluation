# Chess AI Evaluation (chess-ai-evaluation)

## Purpose and Motivation
This project demonstrates designing and tuning an evaluation function for a chess-playing AI. Built on top of a provided starter codebase modeling the game board, pieces, and move generation, my work focused on building a better evaluator capable of challenging and defeating entry-level chess engines.

The main goal was to go beyond a simple material-count heuristic and design an evaluation function that could consistently outperform a ~700-rated Chess.com bot. This required understanding classic chess AI principles, weighting piece values, and adding custom heuristics like central control.

## My Contribution
- Developed and tuned the `evaluate()` function in `AI.py`.
- Improved scoring logic from basic material count to include positional heuristics.
- Tested against low-rated chess bots to benchmark improvements.
- Demonstrated ability to understand, modify, and extend existing codebases.

## Starter Code Acknowledgement
This project uses a provided chess framework for:
- Board representation
- Piece movement rules
- Move legality checking

My main contribution focuses on the **AI evaluation logic** in `AI.py`.

## Features Demonstrated
- Reading and understanding a large existing codebase
- Clean, modular AI logic design
- Adding custom heuristics beyond material value
- Emphasizing central control and positional play
- Improving AI performance through targeted tuning

## Real-World Use Case
Tuning evaluation functions is at the core of building effective chess engines. This project demonstrates how to move beyond simple material counting toward more nuanced scoring, with practical improvements benchmarked against real online chess bots.
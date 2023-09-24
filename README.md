# An Implementation of Checkers with a Minimax AI
This project aimed to create a fully playable checkers game that can be played against an AI.\
The AI is implemented using a minimax algorithm without alpha-beta pruning.\
This version of checkers does not have support for multiple jumps per turn.\
Otherwise, the game is played according to the regular rules of checkers.

## Gameplay
The player plays as black and has the first move.\
Lowercase letters `b` and `r` represent regular pieces while uppercase `B` and `R` represent king pieces.\
The player is first prompted for the position of the piece they want to move. They are then prompted for the space they want to move the piece to.
The input must be formatted with the capital letter followed by the number. If the input is invalid, the player is prompted again to input a valid move.

An example of a valid input in-game:
<pre>
    A   B   C   D   E   F   G   H
  ┌───┬───┬───┬───┬───┬───┬───┬───┐
1 │   │ b │   │ b │   │ b │   │ b │
  ├───┼───┼───┼───┼───┼───┼───┼───┤
2 │ b │   │ b │   │ b │   │ b │   │
  ├───┼───┼───┼───┼───┼───┼───┼───┤
3 │   │ b │   │   │   │   │   │ b │
  ├───┼───┼───┼───┼───┼───┼───┼───┤
4 │   │   │ r │   │   │   │ b │   │
  ├───┼───┼───┼───┼───┼───┼───┼───┤
5 │   │ r │   │   │   │ b │   │   │
  ├───┼───┼───┼───┼───┼───┼───┼───┤
6 │   │   │ r │   │   │   │ r │   │
  ├───┼───┼───┼───┼───┼───┼───┼───┤
7 │   │ r │   │ r │   │ r │   │ r │
  ├───┼───┼───┼───┼───┼───┼───┼───┤
8 │ r │   │ r │   │ r │   │ r │   │
  └───┴───┴───┴───┴───┴───┴───┴───┘
Black Player please make your move:
Please choose the position of the piece you want to move
<b>E2</b>
Please choose the position you want to move the piece to
<b>D3</b>
</pre>

If the player wishes to resign, they can at any time enter `exit` into either the first or second inputs to end the game.

## Notes
Due to issues running Python code containing Unicode characters in VSCode using the built-in Run, it might produce an error. This can be remedied by simply running the program in the terminal. Alternatively, changing the `"python"` line in `settings.json` to
```
"python": "set PYTHONIOENCODING=utf8 && python -u",
```
should allow you to use the built-in Run.

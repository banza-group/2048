"""Play the game."""

import engine
import numpy as np

board = engine.createBoard(4)

message1 = "Use the keys to move (L)eft (R)ight (U)p (D)own."
message2 = "Press (Q) to quit:"
while True:
    print(np.array(engine.showBoard(board)))
    inputValue = input("{} {} ".format(message1, message2))
    inputValue = str(inputValue).upper()
    if inputValue == "Q":
        break
    else:
        engine.move(inputValue, board)

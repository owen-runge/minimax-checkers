def main():
    # main function

    # create board
    gameboard = [[" ", "b", " ", "b", " ", "b", " ", "b"],
                 ["b", " ", "b", " ", "b", " ", "b", " "],
                 [" ", "b", " ", "b", " ", "b", " ", "b"],
                 [" ", " ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " ", " "],
                 ["r", " ", "r", " ", "r", " ", "r", " "],
                 [" ", "r", " ", "r", " ", "r", " ", "r"],
                 ["r", " ", "r", " ", "r", " ", "r", " "]]

    printBoard(gameboard)
    print(f'All available moves for black in this board state are: \n{availableMoves(gameboard,"black")}')
    return 0


def availableMoves(gameboard, turn):
    all_moves = []
    if turn == "black":
        # iterate through board
        for i in range(8):
            for j in range(8):
                # set current piece and check if occupied by black
                # if not, continue to next space
                curr_space = gameboard[i][j]
                if not (ord(curr_space) == 66 or ord(curr_space) == 98):
                    continue

                # create `move` to be added to `all_moves`
                move = []

                # check first two moves, valid for all black pieces king or not
                try:
                    if gameboard[i+1][j-1] == " ":
                        move = [chr(j+65)+str(i+1),[],chr(j+64)+str(i+2)]
                        all_moves.append(move)
                except IndexError:
                    pass
                try:
                    if gameboard[i+1][j+1] == " ":
                        move = [chr(j+65)+str(i+1),[],chr(j+66)+str(i+2)]
                        all_moves.append(move)
                except IndexError:
                    pass

                # check jumps valid for all black pieces
                try:
                    if gameboard[i+1][j-1] in {"r", "R"} and gameboard[i+2][j-2] == " ":
                        move = [chr(j+65)+str(i+1),[chr(j+64)+str(i+2)],chr(j+63)+str(i+3)]
                        all_moves.append(move)
                except IndexError:
                    pass
                try:
                    if gameboard[i+1][j+1] in {"r", "R"} and gameboard[i+2][j+2] == " ":
                        move = [chr(j+65)+str(i+1),[chr(j+66)+str(i+2)],chr(j+67)+str(i+3)]
                        all_moves.append(move)
                except IndexError:
                    pass
                
                if ord(curr_space) == 66:
                    # check last two directions, for kings only
                    try:
                        if gameboard[i-1][j-1] == " ":
                            move = [chr(j+65)+str(i+1),[],chr(j+64)+str(i)]
                            all_moves.append(move)
                    except IndexError:
                        pass
                    try:
                        if gameboard[i-1][j+1] == " ":
                            move = [chr(j+65)+str(i+1),[],chr(j+66)+str(i)]
                            all_moves.append(move)
                    except IndexError:
                        pass
                    # check jumps for kings only in last two directions
                    try:
                        if gameboard[i-1][j-1] in {"r", "R"} and gameboard[i-2][j-2] == " ":
                            move = [chr(j+65)+str(i+1),[chr(j+64)+str(i)],chr(j+63)+str(i-1)]
                            all_moves.append(move)
                    except IndexError:
                        pass
                    try:
                        if gameboard[i-1][j+1] in {"r", "R"} and gameboard[i-2][j+2] == " ":
                            move = [chr(j+65)+str(i+1),[chr(j+66)+str(i)],chr(j+67)+str(i-1)]
                            all_moves.append(move)
                    except IndexError:
                        pass
    else:
        pass

    return all_moves



def printBoard(gameboard):
    print('    A    B    C    D    E    F    G    H')
    count = 1
    for row in gameboard:
        print(f'{count} {row}')
        count += 1

main()
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
    #print(f'All available moves for black in this board state are: \n{availableMoves(gameboard,"black")}')
    #print(f'All available moves for black in this board state are: \n{availableMoves(gameboard,"red")}')
    #checkValidMove(gameboard, "F3", "H5", "black")
    #checkValidMove(gameboard, "G6", "E4", "red")
    #checkValidMove(gameboard, "C6", "A8", "red")
    #checkValidMove(gameboard, "D3", "B1", "black")
    return 0


def availableMoves(gameboard, turn):
    """
    availableMoves()

    parameters:
    - gameboard: full checkers board
    - turn: the side you want to find the available moves for, can be either 'red' or 'black'

    returns:
    - an array of available moves with the following layout:
    [current_position_of_piece, [list_of_positions_jumped], end_position_of_piece]

    """

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
                    if j-1 >= 0:
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
                    if j-1 >= 0:
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
                        if j-1 >= 0:
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
                        if j-1 >= 0:
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

    elif turn == "red":
        # iterate through board
        for i in range(8):
            for j in range(8):
                # set current piece and check if occupied by red
                # if not, continue to next space
                curr_space = gameboard[i][j]
                if not (ord(curr_space) == 82 or ord(curr_space) == 114):
                    continue

                # create `move` to be added to `all_moves`
                move = []

                # check first two moves, valid for all red pieces king or not
                try:
                    if j-1 >= 0:
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

                # check jumps valid for all red pieces
                try:
                    if j-1 >= 0:
                        if gameboard[i-1][j-1] in {"b", "B"} and gameboard[i-2][j-2] == " ":
                            move = [chr(j+65)+str(i+1),[chr(j+64)+str(i)],chr(j+63)+str(i-1)]
                            all_moves.append(move)
                except IndexError:
                    pass
                try:
                    if gameboard[i-1][j+1] in {"b", "B"} and gameboard[i-2][j+2] == " ":
                        move = [chr(j+65)+str(i+1),[chr(j+66)+str(i)],chr(j+67)+str(i-1)]
                        all_moves.append(move)
                except IndexError:
                    pass

                if ord(curr_space) == 82:
                    # check last two directions, for kings only
                    try:
                        if j-1 >= 0:
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
                    # check jumps for kings only in last two directions
                    try:
                        if j-1 >= 0:
                            if gameboard[i+1][j-1] in {"b", "B"} and gameboard[i+2][j-2] == " ":
                                move = [chr(j+65)+str(i+1),[chr(j+64)+str(i+2)],chr(j+63)+str(i+3)]
                                all_moves.append(move)
                    except IndexError:
                        pass
                    try:
                        if gameboard[i+1][j+1] in {"b", "B"} and gameboard[i+2][j+2] == " ":
                            move = [chr(j+65)+str(i+1),[chr(j+66)+str(i+2)],chr(j+67)+str(i+3)]
                            all_moves.append(move)
                    except IndexError:
                        pass


    return all_moves


def checkValidMove(gameboard, curr_pos, end_pos, turn):
    """
    checkValidMove()

    parameters:
    - gameboard: full checkers board
    - curr_pos: the current position of the piece to be moved
    - end_pos: the desired end position of the piece to be moved
    - turn: the side you want to find the available moves for, can be either 'red' or 'black'

    returns:
    - a boolean which says whether or not it's a valid move

    """
    curr_coords = (int(curr_pos[1])-1, int(ord(curr_pos[0]))-65)
    end_coords = (int(end_pos[1])-1, int(ord(end_pos[0]))-65)
    curr_piece = gameboard[curr_coords[0]][curr_coords[1]]
    print(f'curr_coords: {curr_coords}, curr_piece: {curr_piece}, end_coords: {end_coords}')

    if curr_piece == " ":
        # check to see if there is a piece in in curr_pos
        print("There is no piece there!")
        return False
    elif gameboard[end_coords[0]][end_coords[1]] != " ":
        # check if end_pos is occupied by another piece
        print("You are trying to move to a space that's occupied!")
        return False
    elif not (abs(curr_coords[0]-end_coords[0]) == abs(curr_coords[1]-end_coords[1]) and abs(curr_coords[0]-end_coords[0]) <= 2):
        # check if move follows rules for checkers
        print("You're attemping an invalid move!")
        return False
    elif turn == "black" and curr_piece in {"b", "B"}:
        # check to see if current piece matches the turn of the person that's playing (black)
        diff = (curr_coords[0]-end_coords[0], curr_coords[1]-end_coords[1])

        if abs(diff[0]*diff[1]) == 1:
            # if end_pos is one space away diagonally from curr_pos
            if curr_piece == "b" and diff[0] < 0:
                return True
            elif curr_piece == "B":
                return True
            else:
                print("That piece is not a king!")
                return False
        else:
            # if end_pos is 2 spaces away diagonally from curr_pos
            jumped_piece = gameboard[int(curr_coords[0]+(diff[0]*-0.5))][int(curr_coords[1]+(diff[1]*-0.5))]
            if curr_piece == "b" and diff[0] < 0 and jumped_piece in {"r", "R"}:
                return True
            elif curr_piece == "B" and jumped_piece in {"r", "R"}:
                return True
            elif jumped_piece in {"b", "B", " "}:
                print("You are trying to jump your own piece or an empty space!")
                return False
            else:
                print("That piece is not a king!")
                return False
            
    elif turn == "red" and curr_piece in {"r", "R"}:
        # check to see if current piece matches the turn of the person that's playing (red)
        diff = (curr_coords[0]-end_coords[0], curr_coords[1]-end_coords[1])

        if abs(diff[0]*diff[1]) == 1:
            # if end_pos is one space away diagonally from curr_pos
            if curr_piece == "r" and diff[0] > 0:
                return True
            elif curr_piece == "R":
                return True
            else:
                print("That piece is not a king!")
                return False
        else:
            # if end_pos is 2 spaces away diagonally from curr_pos
            jumped_piece = gameboard[int(curr_coords[0]+(diff[0]*-0.5))][int(curr_coords[1]+(diff[1]*-0.5))]
            if curr_piece == "r" and diff[0] > 0 and jumped_piece in {"b", "B"}:
                return True
            elif curr_piece == "R" and jumped_piece in {"b", "B"}:
                return True
            elif jumped_piece in {"r", "R", " "}:
                print("You are trying to jump your own piece or an empty space!")
                return False
            else:
                print("That piece is not a king!")
                return False
        
    else:
        # final case is if player is trying to play for the other person
        print("You cannot move for the other person!")
        return False


def printBoard(gameboard):
    print('    A    B    C    D    E    F    G    H')
    count = 1
    for row in gameboard:
        print(f'{count} {row}')
        count += 1

main()
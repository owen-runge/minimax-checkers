import sys

#nonlocal variables
capture_moves_check = 40

def main():
    # main function
    print("Welcome to a Game of Checkers\n")
    print("This is your starting board state:")
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
    #return 0
    #playing the game 
    #boolean to check if game is over
    game_over = False
    player_move = "black"
    #while loop until game ends
    while not game_over :                 
        if player_move == "black" :           
            print("Black Player please make your move:")
            print("Please choose the position of the piece you want to move")
            piece_initial_position = input()
            print("Please choose the position you want to move the piece to")
            piece_final_position = input()
            #checking for valid move
            valid_move, jumps = checkValidMove(gameboard, piece_initial_position, piece_final_position, player_move)
            while not valid_move:
                printBoard(gameboard)
                print("Please again choose the position of the piece you want to move")
                piece_initial_position = input()
                print("Please again choose the position you want to move the piece to")
                piece_final_position = input()
                valid_move, jumps = checkValidMove(gameboard, piece_initial_position, piece_final_position, player_move)
            #update board
            gameboard = updateBoard(gameboard, jumps, piece_initial_position, piece_final_position)
            #next player move
            player_move = "red"     
            #checkWin
            game_over = checkWin(gameboard, player_move, jumps)            
        else :           
            print("Red Player please make your move:")
            print("Please choose the position of the piece you want to move")
            piece_initial_position = input()
            print("Please choose the position you want to move the piece to")
            piece_final_position = input()
            #checking for valid move
            valid_move, jumps = checkValidMove(gameboard, piece_initial_position, piece_final_position, player_move)
            while not valid_move:
                printBoard(gameboard)
                print("Please again choose the position of the piece you want to move")
                piece_initial_position = input()
                print("Please again choose the position you want to move the piece to")
                piece_final_position = input()
                valid_move, jumps = checkValidMove(gameboard, piece_initial_position, piece_final_position, player_move)
            #update board
            gameboard = updateBoard(gameboard, jumps, piece_initial_position, piece_final_position)
            #next player move 
            player_move = "black"
            #checkWin
            game_over = checkWin(gameboard, player_move, jumps)        
        printBoard(gameboard)

def checkWin(gameboard, nextTurn, jumps):
      
    """
    checkWin()

    parameters:
    - gameboard: full checkers board
    - nextTurn : the player who is expected to make the next move
    - jumps : all the jumps made by the piece the list    

    returns:
    - boolean of True and False if game is over or not
    """    
    #use nonlocal variable for 40 move capture check
    global capture_moves_check
    if len(jumps) == 0:
        capture_moves_check -= 1
        if capture_moves_check == 0 :
            print("Game Drawn Due to No Capture in 40 Moves")
            return True
    else:
        capture_moves_check = 40        
   
    #checking if there are still moves to be made
    all_availableMoves = availableMoves(gameboard, nextTurn)
    if len(all_availableMoves) == 0:
        if nextTurn == "red":
            print("Black Player Wins")
            return True
        else:
            print("Red Player Wins")
            return True
    
    return False    
        

def updateBoard(gameboard, jump_move_list, curr_pos, end_pos):  
     
    """
    updateBoard()

    parameters:
    - gameboard: full checkers board
    - jump_move_list : all the jumps made by the piece the list
    - curr_pos: the current position of the piece to be moved
    - end_pos: the desired end position of the piece to be moved

    returns:
    - gameboard
    """
    #the cord of each jump_move
    #start move board update   
    start_coords = (int(curr_pos[1])-1, int(ord(curr_pos[0]))-65)  
    piece_type = gameboard[start_coords[0]][start_coords[1]] 
    gameboard[start_coords[0]][start_coords[1]] = " "
    for cord in jump_move_list:
        jump_coords = (int(cord[1])-1, int(ord(cord[0]))-65)
        gameboard[jump_coords[0]][jump_coords[1]] = " "
    #end move board update
    end_coords = (int(end_pos[1])-1, int(ord(end_pos[0]))-65)  
    #update King Board
    if end_coords[0] == 0 and piece_type == "r":
        gameboard[end_coords[0]][end_coords[1]] = "R"
    elif end_coords[0] == len(gameboard) - 1 and piece_type == "b":
        gameboard[end_coords[0]][end_coords[1]] = "B"
    else:
        gameboard[end_coords[0]][end_coords[1]] = piece_type    
    return gameboard


def revertBoard(gameboard, jump_move_list, curr_pos, end_pos, jumped_piece):
    """
    revertBoard()

    parameters:
    - gameboard: full checkers board
    - jump_move_list : all the jumps made by the piece the list
    - curr_pos: the current position of the piece to be moved
    - end_pos: the desired end position of the piece to be moved
    - jumped_piece: the piece jumped to make the turn, if there was one

    returns:
    - gameboard
    """

    # the cord of each jump_move
    # start move board update   
    start_coords = (int(curr_pos[1])-1, int(ord(curr_pos[0]))-65)  
    piece_type = gameboard[start_coords[0]][start_coords[1]] 
    gameboard[start_coords[0]][start_coords[1]] = " "
    for cord in jump_move_list:
        jump_coords = (int(cord[1])-1, int(ord(cord[0]))-65)
        gameboard[jump_coords[0]][jump_coords[1]] = jumped_piece
    # end move board update
    end_coords = (int(end_pos[1])-1, int(ord(end_pos[0]))-65)  
    # update King Board
    if end_coords[0] == 0 and piece_type == "r":
        gameboard[end_coords[0]][end_coords[1]] = "R"
    elif end_coords[0] == len(gameboard) - 1 and piece_type == "b":
        gameboard[end_coords[0]][end_coords[1]] = "B"
    else:
        gameboard[end_coords[0]][end_coords[1]] = piece_type    
    return gameboard
  
  
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
    - a list containing jumps if there are any

    """
    curr_coords = (int(curr_pos[1])-1, int(ord(curr_pos[0]))-65)
    end_coords = (int(end_pos[1])-1, int(ord(end_pos[0]))-65)
    curr_piece = gameboard[curr_coords[0]][curr_coords[1]]
    #print(f'curr_coords: {curr_coords}, curr_piece: {curr_piece}, end_coords: {end_coords}')

    if curr_piece == " ":
        # check to see if there is a piece in in curr_pos
        print("There is no piece there!")
        return (False, [])
    elif gameboard[end_coords[0]][end_coords[1]] != " ":
        # check if end_pos is occupied by another piece
        print("You are trying to move to a space that's occupied!")
        return (False, [])
    elif not (abs(curr_coords[0]-end_coords[0]) == abs(curr_coords[1]-end_coords[1]) and abs(curr_coords[0]-end_coords[0]) <= 2):
        # check if move follows rules for checkers
        print("You're attemping an invalid move!")
        return (False, [])
    elif turn == "black" and curr_piece in {"b", "B"}:
        # check to see if current piece matches the turn of the person that's playing (black)
        diff = (curr_coords[0]-end_coords[0], curr_coords[1]-end_coords[1])

        if abs(diff[0]*diff[1]) == 1:
            # if end_pos is one space away diagonally from curr_pos
            if curr_piece == "b" and diff[0] < 0:
                return (True, [])
            elif curr_piece == "B":
                return (True, [])
            else:
                print("That piece is not a king!")
                return (False, [])
        else:
            # if end_pos is 2 spaces away diagonally from curr_pos
            jumped_coords = (int(curr_coords[0]+(diff[0]*-0.5)),int(curr_coords[1]+(diff[1]*-0.5)))
            jumped_piece = gameboard[jumped_coords[0]][jumped_coords[1]]
            if curr_piece == "b" and diff[0] < 0 and jumped_piece in {"r", "R"}:
                return (True, [chr(jumped_coords[1]+65)+str(jumped_coords[0]+1)])
            elif curr_piece == "B" and jumped_piece in {"r", "R"}:
                return (True, [chr(jumped_coords[1]+65)+str(jumped_coords[0]+1)])
            elif jumped_piece in {"b", "B", " "}:
                print("You are trying to jump your own piece or an empty space!")
                return (False, [])
            else:
                print("That piece is not a king!")
                return (False, [])
            
    elif turn == "red" and curr_piece in {"r", "R"}:
        # check to see if current piece matches the turn of the person that's playing (red)
        diff = (curr_coords[0]-end_coords[0], curr_coords[1]-end_coords[1])

        if abs(diff[0]*diff[1]) == 1:
            # if end_pos is one space away diagonally from curr_pos
            if curr_piece == "r" and diff[0] > 0:
                return (True, [])
            elif curr_piece == "R":
                return (True, [])
            else:
                print("That piece is not a king!")
                return (False, [])
        else:
            # if end_pos is 2 spaces away diagonally from curr_pos
            jumped_coords = (int(curr_coords[0]+(diff[0]*-0.5)),int(curr_coords[1]+(diff[1]*-0.5)))
            jumped_piece = gameboard[jumped_coords[0]][jumped_coords[1]]
            if curr_piece == "r" and diff[0] > 0 and jumped_piece in {"b", "B"}:
                return (True, [chr(jumped_coords[1]+65)+str(jumped_coords[0]+1)])
            elif curr_piece == "R" and jumped_piece in {"b", "B"}:
                return (True, [chr(jumped_coords[1]+65)+str(jumped_coords[0]+1)])
            elif jumped_piece in {"r", "R", " "}:
                print("You are trying to jump your own piece or an empty space!")
                return (False, [])
            else:
                print("That piece is not a king!")
                return (False, [])
        
    else:
        # final case is if player is trying to play for the other person
        print("You cannot move for the other person!")
        return (False, [])


def findScore(gameboard, turn):
    """
    findScore()

    parameters:
    - gameboard: full checkers board
    - turn: the side you want to find the available moves for, can be either 'red' or 'black'

    returns:
    -

    """
    score = 0
    return score


def minimax(gameboard, turn, turnsplayed, jumps):
    """
    minimax()

    parameters:
    - gameboard: full checkers board
    - turn: the side you want to find the available moves for, can be either 'red' or 'black'
    - turnsplayed: the depth of the recursion
    - jumps: the jumps made during the turn being examined

    returns:
    - the best score the `turn` can achieve

    """
    
    # base cases
    if turn == "black":
        # `turn` is black
        winner = checkWin(gameboard, "red", jumps)
        if winner == 0:
            # return for a draw
            return 0
        elif winner == 1:
            # return for a black win
            return 100-turnsplayed
    else:
        # `turn` is red
        winner = checkWin(gameboard, "black", jumps)
        if winner == 0:
            # return for a draw
            return 0
        elif winner == 2:
            # return for a red win
            return turnsplayed-100
        
    if turnsplayed == 3:
        # only doing a 3 ply system due to the size of the tree
        return findScore(gameboard, turn)
    

    if turn == "black":
        maxscore = -sys.maxsize
        for move in availableMoves(gameboard, "black"):
            # save jumped piece to be added back after calling minimax
            if len(move[1]) > 0:
                jumped_coords = (int(move[1][0][1])-1, int(ord(move[1][0][0]))-65)
                jumped_piece = gameboard[jumped_coords[0]][jumped_coords[1]]
            else:
                jumped_piece = " "
            gameboard = updateBoard(gameboard, move[1], move[0], move[2])
            score = minimax(gameboard, "red", turnsplayed+1, move[1])
            gameboard = revertBoard(gameboard, move[1], move[2], move[0], jumped_piece)
            maxscore = max(maxscore, score)
        return maxscore
    else:
        minscore = sys.maxsize
        for move in availableMoves(gameboard, "red"):
            # save jumped piece to be added back after calling minimax
            if len(move[1]) > 0:
                jumped_coords = (int(move[1][0][1])-1, int(ord(move[1][0][0]))-65)
                jumped_piece = gameboard[jumped_coords[0]][jumped_coords[1]]
            else:
                jumped_piece = " "
            gameboard = updateBoard(gameboard, move[1], move[0], move[2])
            score = minimax(gameboard, "black", turnsplayed+1, move[1])
            gameboard = revertBoard(gameboard, move[1], move[2], move[0], jumped_piece)
            minscore = min(minscore, score)
        return minscore
    

def getBestMove(gameboard):
    """
    getBestMove()

    parameters:
    - gameboard: full checkers board

    returns:
    - the best move as evaluated by minimax

    """

    minscore = sys.maxsize
    bestmove = None

    for move in availableMoves(gameboard, "red"):
        # save jumped piece to be added back after calling minimax
        if len(move[1]) > 0:
            jumped_coords = (int(move[1][0][1])-1, int(ord(move[1][0][0]))-65)
            jumped_piece = gameboard[jumped_coords[0]][jumped_coords[1]]
        else:
            jumped_piece = " "
        gameboard = updateBoard(gameboard, move[1], move[0], move[2])
        score = minimax(gameboard, "black", 0, move[1])
        gameboard = revertBoard(gameboard, move[1], move[2], move[0], jumped_piece)

        if score < minscore:
            minscore = score
            bestmove = move

    return bestmove


def printBoard(gameboard):
    """
    printBoard()

    parameters:
    - gameboard: full checkers board

    function:
    - prints board

    returns:
    - no returns
    """
    print('    A   B   C   D   E   F   G   H')
    print('  \u250C\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u252C\u2500\u2500\u2500'+
          '\u252C\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u252C\u2500\u2500\u2500\u2510')
    count = 1
    for row in gameboard:
        print(f'{count} \u2502', end='')
        for space in row:
            print(f' {space} \u2502', end='')
        count += 1
        if count < 9:
            print('\n  \u251C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500'+
                  '\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2524')
    print('\n  \u2514\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2534\u2500\u2500\u2500'+
          '\u2534\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2534\u2500\u2500\u2500\u2518')

main()

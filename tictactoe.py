"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    x_counter = 0
        
    for curr_list in board:
        for element in curr_list:
            if element == X:
                x_counter += 1
            elif element == O:
                x_counter -= 1  
        
    if x_counter == 0:
        return X
    
    return O       
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    possible_moves = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
              possible_moves.add((i,j))  

    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    result_board = []
    
    for list in board:
        newList = []
        for elements in list:
            newList.append(elements)
        result_board.append(newList) 
        
    if action[0] >= 0 and action[0] < 3 and action[1] >= 0 and action[1] < 3:
        
        if result_board[action[0]][action[1]] == EMPTY:
            
            move = ""
            if (player(board) == X):
                move = X
            else:
                move = O
            
            result_board[action[0]][action[1]] = move
            
            return result_board
   
    raise Exception("ccwrcerfreferf")
    
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    #horizental check
    for curr_list in board:
        
        first_val = curr_list[0]
        if first_val != EMPTY:
            for i in range(1, len(board)):
                if curr_list[i] != first_val:
                    break
                
                elif i == len(board) - 1:
                    return first_val
    
    
    #vertical check
    for j in range(len(board)):
        
        first_val = board[0][j]
        if first_val != EMPTY:
            for i in range(1, len(board)):
                if board[i][j] != first_val:
                    break
                elif i == len(board) - 1:
                    return first_val
                
    #left-to-right diongonal           
    first_val = board[0][0]
    for i in range(1,len(board)):
        if first_val == EMPTY or first_val != board[i][i]:
            break
    
        elif i == len(board) - 1:
            return first_val
        
    #right-to-left diongonal 
    first_val = board[0][len(board) -1]
    for j in range(len(board) - 1, -1, -1):
        i = len(board) - j - 1
        if first_val == EMPTY or first_val != board[i][j]:
            break
        
        elif j == 0:
            return first_val
        
        
    return None
        
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return len(actions(board= board)) == 0 or winner(board= board) != None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    winner_of_game = winner(board= board)
    
    if winner_of_game == X:
        return 1
    elif winner_of_game == O:
        return -1
    else:
        return 0
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board= board):
        return None
    
    move = (None, None, None)
    
    if player(board= board) == X:
        
        move = finding_max_move(board= board)    
    else:
        
        move = finding_min_move(board= board)
        
        
    
    return (move[0], move[1])
    
 

def finding_max_move(board):
    
    if terminal(board= board):
        return (None, None, utility(board= board))
    
    
    best_util = float("-inf")
    final_move = (None, None, -1)
    
    for action in actions(board= board):
        
        new_board = result(board= board, action= action)
        curr_move = finding_min_move(new_board)
        
        if curr_move[2] == 1:
            final_move = (action[0], action[1], 1)
            break
        
        
        
        if best_util < curr_move[2]:
                best_util = curr_move[2]
                final_move = (action[0], action[1], best_util)
                
    return final_move


def finding_min_move(board):
    
    if terminal(board= board):
        return (None, None, utility(board= board))
    
    
    best_util = float("inf")
    final_move = (None, None, 1)
    
    for action in actions(board= board):
        
        new_board = result(board= board, action= action)
        curr_move = finding_max_move(new_board)
        
        if curr_move[2] == -1:
            final_move = (action[0], action[1], -1)
            break
        
        if best_util > curr_move[2]:
                best_util = curr_move[2]
                final_move = (action[0], action[1], best_util)
                
    return final_move





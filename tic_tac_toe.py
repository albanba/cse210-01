'''
Tic-Tac-Toe: A Solution
Author: Alban Barrantes 
'''

# This dictionary contains the keys and initial numbers for all squares in the grid
sqrs = {
  1: 1,
  2: 2,
  3: 3,
  4: 4,
  5: 5,
  6: 6,
  7: 7,
  8: 8,
  9: 9,    
}

# These function prints the grid with the initial values and then it prints the grid with 
# new marks as they are entered by users


def print_grid(sqrs):
    row1 = (f'{sqrs.get(1)} | {sqrs.get(2)} | {sqrs.get(3)}')  
    row2 = (f'{sqrs.get(4)} | {sqrs.get(5)} | {sqrs.get(6)}')
    row3 = (f'{sqrs.get(7)} | {sqrs.get(8)} | {sqrs.get(9)}')  
    separator = ("---------")
    separator1 = ("---------")

    
    print (row1)
    print (separator)
    print (row2)
    print (separator1)
    print (row3)



#This function determines the type of mark to be entered in the grid
#"O" or "X" and what square to use to enter the mark based on the user input and 
# the turn variable  

def place_mark(turn):
    if turn != 0: 
        mark = "O"
    else:
        mark = "X"
       
    sqr_pick = int(input("Please enter a number from the grid to place your mark: "))
    
    sqrs[sqr_pick] = mark
    
    print_grid(sqrs)

    return mark

# This dictionary contains the rows, diagonals, and columns to evaluate 
# if there is a winner or a draw yet. The lists are organized on the possible 
# winning scenarios.
def status_dic(sqrs):
    status = {
    "row1": [sqrs.get(1), sqrs.get(2), sqrs.get(3)],
    "row2": [sqrs.get(4), sqrs.get(5), sqrs.get(6)],
    "row3": [sqrs.get(7), sqrs.get(8), sqrs.get(9)],
    "column1": [sqrs.get(1), sqrs.get(4), sqrs.get(7)],
    "column2": [sqrs.get(2), sqrs.get(5), sqrs.get(8)],
    "column3": [sqrs.get(3), sqrs.get(6), sqrs.get(9)],
    "diagonal1": [sqrs.get(1), sqrs.get(5), sqrs.get(9)],
    "diagonal2": [sqrs.get(7), sqrs.get(5), sqrs.get(3)]
    }

    return status 
    

#This function evaluates if if there is a winner or a draw by looping 
# once through the status dictionary to determine if any list matches 
# a winning scenario. If there is a winner the function will anounce it 

def winner(status, player):
    winner_counter = 0
    winner = "" 
    while winner_counter != 8: 
        for i in status:
            three_values =status.get(i)
            if three_values == ["X", "X", "X"] or three_values == ["O", "O", "O"]:
                winner = ("Yes")
            else:
                round = ("keep playing")

            winner_counter += 1
        
    if winner == "Yes":
        round = "stop"
        print (f'{player} wins the game')

    return round



def main():
    
    round = ("keep playing")
    counter = 0
    turn = 0
    player = ""

    print_grid(sqrs)
    
    while round == "keep playing" and counter < 9:
        
        player = place_mark(turn)

        status = status_dic(sqrs)

        round = winner(status, player)

        counter += 1
        turn = counter % 2

    # print ("The game is a draw")

main()

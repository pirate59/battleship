from random import randint
w = 800
h = 700

z = 0

board = []
print "==========================="
print "== Welcome to Battleship =="
print "==========================="

z = 10
#while z < 5  or z > 10:
#    xaa = False
#    while xaa == False:
#        try:
#            z = int(raw_input("How big will the board be (5-10)?"))
#        except ValueError:
#            print "Invalid input. Try again"
#        else:
#            xaa = True
#    if z < 5 or z > 10:
#        print "Out of range"

userx = 0
while userx < 1 or userx > z:
    xab = False
    while xab == False:
        try:
            userx = int(raw_input("Which row do you want you your ship to be on?"))
        except ValueError:
            print "Invalid input. Try again"
        else:
            xab = True
    if userx < 1 or userx > z:
        print "Out of range"

userx -= 1
        
usery = 0
while usery < 1 or usery > z:
    xac = False
    while xac == False:
        try:
            usery = int(raw_input("Which column do you want you your ship to be on?"))
        except ValueError:
            print "Invalid input. Try again"
        else:
            xac = True
    if usery < 1 or usery > z:
        print "Out of range"
usery-= 1



### Look at creating a limit to the size of te board. Maybe 20? ###
# Create the grid called board (creates a series of lists in a list
for x in range(int(z)): #repeat for each row
    board.append(["O"] * int(z)) # add in "O" for each record in the list for the length of the list

board[userx][usery] = "U" # add in the users ship position on the board

def print_board(board): # print the board
    print "Legend: X - Miss O - Ocean U - You"
    for row in board: 
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)



def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


#print ship_row + 1
#print ship_col + 1

for turn in range(200):
    print "This is turn number: " + str(turn + 1)
    guess_row = 0
    while guess_row < 1  or guess_row > z:
        xad = False
        while xad == False:
            try:
                guess_row = int(raw_input("Guess Row:"))
            except ValueError:
                print "Invalid input. Try again"
            else:
                xad = True
        if guess_row < 1 or guess_row > z:
            print "Out of range"

    guess_col = 0
    while guess_col < 1  or guess_col > z:
        xad = False
        while xad == False:
            try:
                guess_col = int(raw_input("Guess Column:"))
            except ValueError:
                print "Invalid input. Try again"
            else:
                xad = True
        if guess_col < 1 or guess_col > z:
            print "Out of range"

            
    # while guess_row == 0:
      #   guess_row = raw_input("Guess Row:")
    # while guess_col == 0:    
      #   guess_col = raw_input("Guess Col:")
    guess_row -= 1
    guess_col -= 1
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    
    if (guess_row < 0 or guess_row > (z - 1)) or (guess_col < 0 or guess_col > z):
        print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X"):
        print "That one was guessed already."
    elif (board[guess_row][guess_col] == "U"):
        print "You blew up yourself!"
        break
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
        

    #place computer guess code here.
    #user the random_row() and random_col() to generate computer guess.
    #comp_row = random_row(board)
    #comp_col = random_col(board)
    comp_guess = False
    loss = False
    while comp_guess == False:
        
        comp_row = random_row(board)
        comp_col = random_col(board)

                                    
        if board[comp_row][comp_col] == "O":
            if comp_row == ship_row and comp_col == ship_col:
                print "Computer is still thinking"
            else:
                print "Computer guessed " +str(comp_row +1) + ", " + str(comp_col +1) + "."
                comp_guess = True

        if board[comp_row][comp_col] == "U":
            print "Computer guessed " +str(comp_row +1) + ", " + str(comp_col +1) + "."
            print "It got you!"
            loss = True # tag to exit the mail loop once the while is finished
            comp_guess = True
           
    if loss == True:
        break

    board[comp_row][comp_col] = "X"
    print_board(board)

print "Game Over."
1
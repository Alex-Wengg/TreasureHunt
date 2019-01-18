"""Han Weng
    05/02/2018
    This is a treasure hunt game, where the user gets 
    10 guesses to guess where all three treasures are on the board """
#For random numbers to make treasures
import random
def hideTreasure(board):
    """Accepts number of rows and cols from the board and hides 3 treasures in unique postions 
    using T to represent a treasure """
    stop = 0
    # Generate three unique coordinates to mark as treasure coordinates
    while stop != 3:
        row_treasure = random.randrange(0, len(board))
        col_treasure = random.randrange(0, len(board[0]))
        # if the spot is empty space then add a treasure on to it until there are 3
        if board[row_treasure][col_treasure] == " ":
          board[row_treasure][col_treasure] = "T"
          stop += 1
def displayBoard( board, show_treasure= False):
    """generates the number of rows and cols as requested by the user and hides the 
    tresure by replacing them with blacnk spaces"""
    dash = " | "
    #starts the number of cols from 0 to whatever amount the user wanted
    for display in range(len(board[0])):
      print ("  %d" %display,)
    print ("")
    #displays the treasure if the users found it 
    if show_treasure == False:
      for row in range(len(board)):
        print (str(row) + ": "+ dash.join(board[row]).replace("T", " "))
        print ("  " + "---+"*(len(board[0])))
    #if the player cant find it, then the treasures will be revealed
    else:
      for row in range(len(board)):
        print (str(row) + ": "+ dash.join(board[row]))
        print ("  " + "---+"*(len(board[0])))
def makeUserMove(board):
    """players can make a coordinate input and it checks if the player has entered the correct 
    row and col for a treasure.
    ! = player has a position near a treasure 
    $ = the player has found a treasure
    X = nothing, no treasures or ones nearby"""
    #starting variables
    player_turn = True
    row_limit = len(board) 
    col_limit = len(board[0]) 
    #checks the postion for !, T or X
    while player_turn:
        #what coordinate the player wants to examine
        try:
          print ("What row would you like to search (0- %d ): " %(row_limit))
          row_choice = int(input())
          print ("What col would you like to search (0- %d ): " %col_limit)
          col_choice = int(input())
        #retry the inputs when the inputs are not integers
        except:
            print ("\nERROR: Invalid coordinate! Please enter integers as input. between the range")
            continue
        #Are the inputs new ones and not already selected
        if (0<=row_choice<row_limit) and (0<=col_choice< col_limit):
            if board[row_choice][col_choice] not in '$X!':
            #Coordinates are valid now time to see if they found a treasure
                #the player has found the treasure "T" and now it will be converted to $
                if board[row_choice][col_choice] == "T":
                    show_treasure = True
                    print ("\n You found a treasure\n")
                    board[row_choice][col_choice] = "$"
                    player_turn = False
                    return True
                #look for the closest treasure spot and ! for nearby ones
                else:
                    big_row = 2
                    big_col = 2
                    small_row = -1
                    small_col=-1
                    if col_choice+1 == len(board[0]):
                        big_col = 1
                    if row_choice+1 == len(board):
                        big_row = 1
                    if row_choice == 0:
                        small_row = 0
                    if col_choice ==0:
                        small_col = 0
                    for row_hint in range(small_row+row_choice, big_row+row_choice):
                        for col_hint in range(small_col+col_choice, big_col+col_choice):
                            #the coordinate has a treasure nearby
                            if board[row_hint][col_hint] == "T":
                                board[row_choice][col_choice] = "!"
                                print ("oh a treasure close by")
                                break
                    if board[row_choice][col_choice] != "!":
                        board[row_choice][col_choice] = "X"
                    break
                    return False   
            else:
                # spots been taken
                print ("spots been taken")
        else:   
            #rows or cols not being between the len(board) or len(board[0])
            print ("\nSorry, invalid square. Please try again!"    )
def hall_of_fame():
    """this is for adding the winner who found all 3 treasures and name will be added to a file"""
    winner = input("damn, you must good as the legendary Mr. Rao, what is your name")
    exist = False
    try:
        #See if name already exists
        read_file = open("winners.txt", "r")
        for line in read_file:
            if line.strip() == winner:
                exist = True
    except IOError:
        #does not exist so exist = False to inform the later program
        pass
    #exist = False means the program must make a new file
    if exist == False:
        
        winners = open("winners.txt", "a")    
        winners.write(winner+"\n")
        winners.close()
    else:
        # remind them the name already has made
        print ("\nYou are already in the Hall Of Fame!")
def main():
    """this is where all the variables came from, sort of like a CPU unit for this Coordinates
    or the heart where all the functions are used in their respective role"""
    #This is a reminder for the users to try to find all the treasures to be on this awesome list of fame
    noone = True
    #Print the winners
    print (" HALL OF FAME")
    print ("==============")
    #shows the badasses who are apart of this wicked HALL
    try:
        winners = open("winners.txt", "r")
        for line in winners:
            print (line.strip())
            noone = False
        #Close file
        winners.close()     
    except IOError:
        #this means no one is on the list
        noone = True
    if noone:
        print ("no one rn......")
    board = []
    treasure_found = 0
    guess = 10
    #show what game the players are playing
    print ("WELCOME TO TREASURE HUNT!\n")

    correct = True
    while correct:
        #players input how many rows and cols they would like their board to have 
        try:
            rows = int(input("enter the number of rows (3-10): "))
            cols = int(input("How many columns would you like (3-10): "))
        except ValueError:
            #to talk players the limit they can have for cols and rows
            print("\nInvalid input, please enter an integer between 3-10.\n")
            continue
        if (2 < rows < 11 and 3 <= cols <= 10):
            #ok so they entered the right amount so we dont need this loop anymore
            correct = False
        else:
            print ("range 3-10 for both row and col")
    #creates the board with the number of col and row requested
    for number_of_rows in range(rows):
        board.append([]) 
        for col in range(cols):
          board[number_of_rows].append(" ")    
    #hides all the treasures from the users sight
    hideTreasure(board)    
    #this is how the game will keep going until all the treasures are found or no more guesses
    while treasure_found < 3 and (guess > 0):
        print ("You have %d guesses and found %d /3 treasures.\n" %(guess, treasure_found)) 
        #shows the board
        displayBoard( board, show_treasure = False)
        guess -= 1
        #the player makes a move and that move return true and thus a treasure is found
        if makeUserMove(board):
            treasure_found += 1
    #when the game is done, we are shown the final part with all the treasures found
    displayBoard(board, show_treasure= True)
    #when all the secrets are discovered and thus they will be added onto the file 
    if treasure_found == 3:
        hall_of_fame()
    else:
        #no oh, you didnt win:( 
        print ("feels bad man, ye found not all the treasures")
# Runs the game.
main()

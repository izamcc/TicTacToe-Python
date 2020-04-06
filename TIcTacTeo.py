#TicTacToe
import random
counter =0.0
board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
tag1="nun"
tag2="nun"



#NewGame fun. is responsible for ending the game or a replay
def NewGame ():
    print("wanna Play again ? ( Y / N ) ")
    d = input("- ")
    if d == "Y" or d == "y":
        start()
    elif d == "N" or d == "n":
        print(" THANK YOU FOR PLAYING ")
        print(" COME BACK SOON .. ")
    else:
        print("invalid input, try again ")
        NewGame()


#Round fun. is to orgnise the process and sequance of actions in a round or contenueing to next round 
def Round ():
    global counter
    display()
    counter +=1
    if counter > 4:
        check()
    else:
        find ()


#check fun. is to check the status of the game .. anyone wining or is it a draw 
def check ():
    if board[1] == board[2] == board[0] or board[0] == board[4] == board[8] or board[0] == board[3] == board[6]:
        print("Congrats Player ",board[0] ," Won The Game !!! ")
        NewGame()
    elif board[1] == board[4] == board[7] or board[3] == board[4] == board[5]:
        print("Congrats Player ",board[4] ," Won The Game !!! ")
        NewGame()
    elif board[2] == board[5] == board[8] or board[6] == board[7] == board[8]:
        print("Congrats Player ",board[8] ," Won The Game !!! ")
        NewGame()
    elif board[2] == board[4] == board[6]:
        print("Congrats Player ",board[2] ," Won The Game !!! ")
        NewGame()
    elif counter > 8:
        print("waw It seems we have a DRAW ! ")
        NewGame()
    else:
        find()


#display fun. is to display the board
def display():
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])


#find is to find the input location for each player and assigne its value the choosin location
def find ():
    choice = int(input("- "))
    if choice > 8:
        print("input invalid !!")
        print("please choose from 0 to 8 only")
        find()    
    else:
        if board[choice] == tag1 or board[choice] == tag2:
            print("this location is alrady taken")
            display()
            find()
        elif counter % 2 == 0:
            board[choice] = tag2
            Round()
        else:
            board[choice] = tag1
            Round()



#the start fun. is to  introduce the players to the game & set a tag for each player
def start ():
    print("willcom to TicTacToe ")
    print("please choose X or O : ")
    global tag1 , tag2
    while True:
        tag1 = input("- ")
        if tag1 == "x" or tag1 == "X":
            tag1 = "X"
            tag2 = "O"
            break
        elif tag1 == "o" or tag1 == "O":
            tag1 = "O"
            tag2 = "X"
            break
        else:
            print("invalid Entry !!!")
            print("you should choose between X & O only")

    print("player 1 tag is: ", tag1," & player 2 tag is: ", tag2 )
    print("Choose a location on the Board:")


#the first running functions
start()
Round()

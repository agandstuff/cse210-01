# CSE 210-01 Tic Tac Toe Game
# Amanda Stokes

#setting up the game board
def gameGrid(values):
    #top three spaces
    print('\n\t   |   |')
    print('\t {} | {} | {}'.format(values[0], values[1], values[2]))
    print('\t___|___|___')

    #middle three spaces
    print('\t   |   |')
    print('\t {} | {} | {}'.format(values[3], values[4], values[5]))
    print('\t___|___|___')

    #bottom three spaces
    print('\t   |   |')
    print('\t {} | {} | {}'.format(values[6], values[7], values[8]))
    print('\t   |   |   \n')

#check to see if player has won
def checkWinner(currentPlayer, playerPostion):
    #possible winning combinations
    possWins = [
                    [1,2,3],
                    [4,5,6],
                    [7,8,9],
                    [1,4,7],
                    [2,5,8],
                    [3,6,9],
                    [1,5,9],
                    [3,5,7]
                ]

    #loops through possWins to check for any possible wins currently in game
    for i in possWins:
        if all(j in playerPostion[currentPlayer] for j in i):
            #if any matches are found, boolean True is returned
            return True

    #if no matcbes were found, boolean False is returned
    return False

#check for draw game
def drawGame(playerPosition):
    #counts how many times each player position occurs and counts to see if it equals the game grid
    if len(playerPosition['X']) + len(playerPosition['O']) == 9:
        return True

    return False

#definition for the game itself
def ticTacToe(currentPlayer):
    #starting values of the game board
    values = [' ' for x in range(9)]

    #stores player position
    playerPosition = {'X':[], 'O':[]}

    #looping through the game
    while True:
        print('\nPlease choose a number between 1 and 9 to pick your spot!\n')
        #printing board with blank values to start
        gameGrid(values)

        #try/exception for validating user input
        try: 
            print('Player ', currentPlayer, ', your turn. Where would you like to play? ', end = '')
            userInput = int(input())
        except ValueError:
            print("Invalid input, please enter a number between 1 and 9.")
            continue

        #validating user input
        if userInput < 1 or userInput > 9:
            print('Number outside of range, please enter a number between 1 and 9.')
            continue

        if values[userInput - 1] != ' ':
            print("Space already taken, please choose another.")
            continue

        #updating game grid
        values[userInput - 1] = currentPlayer

        playerPosition[currentPlayer].append(userInput)

        #check for winner or draw
        if checkWinner(currentPlayer, playerPosition):
            gameGrid(values)
            print('Player', currentPlayer, ' wins! Congrats!\n')
            return currentPlayer

        if drawGame(playerPosition):
            gameGrid(values)
            print('Draw Game...try again?\n')
            return

        if currentPlayer == 'X':
            currentPlayer = 'O'
        else:
            currentPlayer = 'X'

if __name__ == "__main__":

    while True:

        print('To start game, first player choose either X or O: ')
        userInput = str(input())

        if userInput == 'X' or userInput == 'x':
            currentPlayer = 'X'
            break
        elif userInput == 'O' or userInput == 'o':
            currentPlayer = 'O'
            break
        else:
            print('Invalid input, please enter either X or O: ')

    ticTacToe(currentPlayer)
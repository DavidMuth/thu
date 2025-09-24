"""
    Basic tic tac toe game.
    Lacks input validation, draw and overwrite prevention.
"""

def getPlayerNames():
    names = []
    i = 1
    while i <= 2:
        name: str
        validInput = False
        while validInput == False:
            name =input(f"Player {i}. Enter a letter: ")
            if len(name) == 1:
                validInput = True
            else:
                print("Invalid name. Only use ONE letter.")
        
        names.append(name)
        i += 1
    
    return names

def printBoard(board: list):
    for row in board:
        for col in row:
            print(col, end= " ")
        print()

def play(board: list, currentPlayer: str):
    printBoard(board)

    print(f"\nCurrent Player: {currentPlayer}")
    column = int(input("Enter column (0,1,2): "))
    row = int(input("Enter row (0,1,2): "))
    
    return column, row

def updateBoard(column: int, row: int, board: list, player: str) -> list:
    board[row][column] = player
    return board

def flattenList(list: list):
    flatList = []
    for row in list:
        flatList.extend(row)
    return flatList

        
def checkWinner(board: list, player: str):
    # rows
    for row in board:
        if all(cell == player for cell in row):
            return True
        
    # columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
        
    # diagonal
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def main():
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    players = getPlayerNames()
    
    winner = ""
    while winner == "":
        for player in players:
            column, row = play(board, player)
            print()
            board = updateBoard(column, row, board, player)
            if checkWinner(board, player):
                printBoard(board)
                print(f"\n\n{player} wins!\n\n")
                return
        

if __name__ == "__main__":
    main()
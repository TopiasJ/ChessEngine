#python main
from Chessnut import Game


#main Loop
def main():
    chessgame = Game()
    while(True):
        
        visualizeBoard(str(chessgame.board))
        print(chessgame.get_moves())
        print("please give a move")
        move = input()
        chessgame.apply_move(move)

def visualizeBoard(board):
    boardRows = board.split('/')
    for row in boardRows:
        rowSquares = [char for char in row]
        strRow = ""
        for square in rowSquares:
            strRow += getPieceSymbol(square)
        print(strRow)

def getPieceSymbol(code):
    if code == "p":
        return "\u265F "
    elif code == "r":
        return "\u265C "
    elif code == "n":
        return "\u265E "
    elif code == "b":
        return "\u265D "
    elif code == "k":
        return "\u265A "        
    elif code == "q":
        return "\u265B " 
    elif code == "P":
        return "\u2659 "  
    elif code == "R":
        return "\u2656 "  
    elif code == "N":
        return "\u2658 "  
    elif code == "B":
        return "\u2657 "  
    elif code == "K":
        return "\u2654 "  
    elif code == "Q":
        return "\u2655 "  
    else: ## it is a number instead
        emptySpaces = ''
        for _ in range(int(code)):
            emptySpaces += "  "
        return emptySpaces



    #WHITE EMPTY = "\u25FB"
    #BLACK EMPTY = "\u25FC"

#run
main()

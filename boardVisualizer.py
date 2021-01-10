
class Visualizer(object):
    def visualizeBoard(self, board):
        boardRows = board.split('/')
        rowNumber = 8
        for row in boardRows:
            rowSquares = [char for char in row]
            strRow = ""

            for square in rowSquares:
                strRow += self.getPieceSymbol(square)
            
            print(str(rowNumber) + ' ' + strRow)
            rowNumber -= 1
    
        print('  a b c d e f g h')

    def getPieceSymbol(self, code):
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
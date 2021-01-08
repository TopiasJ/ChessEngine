#python main
from Chessnut import Game
from evaluator import Evaluator
from negaMaxAlgorithm import NegaMax
from alphaBetaAlgorithm import AlphaBeta
import time

#main Loop
def main():
    chessgame = Game()
    ev = Evaluator()
    #alg = NegaMax()
    alg = AlphaBeta()
    while(chessgame.status != chessgame.CHECKMATE or chessgame.status != chessgame.STALEMATE):
        print(chessgame.move_history)
        visualizeBoard(str(chessgame.board))
        print(chessgame.get_moves())
        print('current eval: ' + str(ev.evaluate(str(chessgame.board))))
        print("please give a move")
        
        move = input()
        chessgame.apply_move(move)
        visualizeBoard(str(chessgame.board))
        if(chessgame.status == chessgame.CHECKMATE or chessgame.status == chessgame.STALEMATE):
            break
        #ai turn
        start_time = time.time()
        aimove = alg.getBestmove(chessgame)
        elapsed_time = time.time() - start_time
        print('timeelapsed:' + str(elapsed_time) +" ai move: " + aimove)
        chessgame.apply_move(aimove)
    if chessgame.status == chessgame.CHECKMATE:
        print('CHECKMATE')
    elif chessgame.status == chessgame.STALEMATE:
        print('STALEMATE')
    print(chessgame.status)


def visualizeBoard(board):
    boardRows = board.split('/')
    rowNumber = 8
    for row in boardRows:
        rowSquares = [char for char in row]
        strRow = ""

        for square in rowSquares:
            strRow += getPieceSymbol(square)
        
        print(str(rowNumber) + ' ' + strRow)
        rowNumber -= 1
 
    print('  a b c d e f g h')

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

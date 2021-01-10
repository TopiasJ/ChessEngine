#python main
from Chessnut import Game
from evaluator import Evaluator
from negaMaxAlgorithm import NegaMax
from alphaBetaAlgorithm import AlphaBeta
from boardVisualizer import Visualizer
import time

#main Loop
def main():
    chessgame = Game()
    #ev = Evaluator()
    visualiser = Visualizer()
    #alg = NegaMax()
    alg = AlphaBeta()

    #MAIN LOOP
    while(True):
        #draw board and available moves
        visualiser.visualizeBoard(str(chessgame.board))
        #print(chessgame.get_moves())
        
        #WHITE TO MOVE
        #print('current eval: ' + str(ev.evaluate(str(chessgame.board))))
        #print("please give a move")
        #move = input()
        print('white moving next')
        move = alg.getBestmove(chessgame, 2)        
        chessgame.apply_move(move)
        visualiser.visualizeBoard(str(chessgame.board))
        if(chessgame.status == chessgame.CHECKMATE or chessgame.status == chessgame.STALEMATE):
            if chessgame.status == chessgame.CHECKMATE:
                print('CHECKMATE!! White won!!')
            break


        #BLACK TO MOVE
        #ai turn
        print('black moving next')
        start_time = time.time()
        aimove = alg.getBestmove(chessgame,2)
        elapsed_time = time.time() - start_time
        print('timeelapsed:' + str(elapsed_time) +" ai move: " + aimove)
        
        chessgame.apply_move(aimove)

        if(chessgame.status == chessgame.CHECKMATE or chessgame.status == chessgame.STALEMATE):
            if chessgame.status == chessgame.CHECKMATE:
                print('CHECKMATE!! Black won!!')
            break
    #END OF MAIN LOOP

    #final visualisation
    visualiser.visualizeBoard(str(chessgame.board))
    if chessgame.status == chessgame.STALEMATE:
        print('STALEMATE')

def test():
    
    chessgame = Game('8/8/k7/2K5/8/8/8/1R6 w - - 0 1') ##white mate 5?
    #chessgame = Game('k7/2K5/8/8/8/8/8/1R6 w - - 0 1') ##white mate 1
    #chessgame = Game('8/k7/2K5/8/8/8/8/1R6 w - - 0 1')
    
    chessgame.apply_move('b1b2')
    chessgame.apply_move('a6a7')
    #chessgame = Game('8/8/K7/2k5/8/8/8/1r6 b - - 0 1')
    visualiser = Visualizer()
    visualiser.visualizeBoard(str(chessgame.board))
    #alg = NegaMax()
    alg = AlphaBeta()
    move = alg.getBestmove(chessgame, 5)
    print(move)


#run the software
main()
#test()
#tournament()
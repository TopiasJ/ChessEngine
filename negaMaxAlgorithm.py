from evaluator import Evaluator
from Chessnut import Game
from Algorithm import Algorithm
import threading
import copy
import random

class NegaMax(Algorithm):
    ev = Evaluator()
    scores = []
    def getBestmove(self, game, depth = 2 ):
        moves = game.get_moves()
        self.scores = []
        #threads = []
        for move in moves:
            testGame = Game(fen=game.get_fen(), validate=False)
            testGame.apply_move(move)

            self.calcOneMove(move, testGame,depth)
            #t = threading.Thread(target = self.calcOneMove, args=(move, testGame,))
            #threads.append(t)
            #t.start()
        
        #for thr in threads:
        #    thr.join()
        if(testGame.state.player == 'w'):
            self.scores.sort()
        else:
            self.scores.sort(reverse=True)
        print(self.scores)
        bestScore = self.scores[0][0]
        print('best score:' + str(bestScore))

        i = 0
        for x in self.scores:
            if x[0] != bestScore:
                break
            i += 1
        print("number of best scores:" + str(i))
        selectedmove = random.randint(0, i-1)
        print(selectedmove)
        print('selected move: ' + str(self.scores[selectedmove]))
        return self.scores[selectedmove][1]

        #self.scores.sort()
        #return self.scores[0][1]

    def calcOneMove(self, move, fen, depth):
            score = self.negaMax(fen, depth)
            #print(move + ' ' + str(score))
            self.scores.append((score,move))
            return



    def negaMax(self, game, depth=2):
        if ( depth == 0 ):
            return self.ev.evaluate(str(game.board))
        max = -999999
        moves = game.get_moves()

        for move in moves:
            #print("testing move" + move + " depth:" + str(depth))
            testGame = Game(fen=game.get_fen(), validate=False)
            testGame.apply_move(move)
            score = -self.negaMax(testGame, depth = depth-1 )
            if score > max:
                max = score
        return max

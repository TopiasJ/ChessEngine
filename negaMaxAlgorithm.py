from evaluator import Evaluator
from Chessnut import Game
from Algorithm import Algorithm
import threading
import copy

class NegaMax(Algorithm):
    ev = Evaluator()
    scores = []
    def getBestmove(self, game):
        moves = game.get_moves()
        self.scores = []
        threads = []
        for move in moves:
            testGame = Game(fen=game.get_fen(), validate=False)
            testGame.apply_move(move)

            #self.calcOneMove(move, testGame.get_fen())
            t = threading.Thread(target = self.calcOneMove, args=(move, testGame,))
            threads.append(t)
            t.start()
        
        for thr in threads:
            thr.join()


        self.scores.sort()
        return self.scores[0][1]

    def calcOneMove(self, move, fen):
            score = self.negaMax(fen)
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

     
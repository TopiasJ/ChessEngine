from evaluator import Evaluator
from Chessnut import Game
import threading
import copy

class NegaMax(object):
    ev = Evaluator()
    scores = []
    def getBestmove(self, game):
        moves = game.get_moves()
        self.scores = []
        threads = []
        for move in moves:
            testGame = Game(fen=game.get_fen())
            testGame.apply_move(move)

            #self.calcOneMove(move, testGame.get_fen())
            t = threading.Thread(target = self.calcOneMove, args=(move, testGame.get_fen(),))
            threads.append(t)
            t.start()
        
        for thr in threads:
            thr.join()


        self.scores.sort()
        return self.scores[0][1]

    def calcOneMove(self, move, fen):
            score = self.negaMax(fen)
            print(move + ' ' + str(score))
            self.scores.append((score,move))
            return



    def negaMax(self, fen, depth=2):
        game = Game(fen=fen)
        if ( depth == 0 ):
            return self.ev.evaluate(str(game.board))
        max = -999999
        moves = game.get_moves()

        for move in moves:
            #print("testing move" + move + " depth:" + str(depth))
            testGame = Game(fen=game.get_fen())
            testGame.apply_move(move)
            score = -self.negaMax(testGame.get_fen(), depth = depth-1 )
            if score > max:
                max = score
        return max

     
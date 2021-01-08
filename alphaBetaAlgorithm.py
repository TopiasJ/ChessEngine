#https://www.chessprogramming.org/Alpha-Beta
from evaluator import Evaluator
from Chessnut import Game
from Algorithm import Algorithm

class AlphaBeta(Algorithm):
    ev = Evaluator()

    
    scores = []
    def getBestmove(self, game):
        moves = game.get_moves()
        self.scores = []
        #threads = []
        for move in moves:
            testGame = Game(fen=game.get_fen(),validate=False)
            testGame.apply_move(move)
            score = self.alphaBetaMax(testGame, -999999,9999999, 4)
            self.scores.append((score,move))
    #        t = threading.Thread(target = self.calcOneMove, args=(move, testGame,))
   #         threads.append(t)
  #          t.start()
        
#        for thr in threads:
 #           thr.join()

        print(self.scores)
        self.scores.sort()
        return self.scores[0][1]


    def alphaBetaMax(self, game, alpha, beta, depthleft):
        if depthleft == 0:
            return self.ev.evaluate(str(game.board))
        moves = game.get_moves()
        for move in moves:
            testGame = Game(fen=game.get_fen(),validate=False)
            testGame.apply_move(move)
            score = self.alphaBetaMin(testGame,alpha, beta, depthleft - 1 )
            if score >= beta:
                return beta   # fail hard beta-cutoff
            if score > alpha:
                alpha = score # alpha acts like max in MiniMax
        return alpha

    def alphaBetaMin(self,game, alpha, beta, depthleft ):
        if ( depthleft == 0 ):
            return -self.ev.evaluate(str(game.board))
        moves = game.get_moves()
        for move in moves:
            testGame = Game(fen=game.get_fen(),validate=False)
            testGame.apply_move(move)
            score = self.alphaBetaMax(testGame, alpha, beta, depthleft - 1)
            if score <= alpha:
                return alpha # fail hard alpha-cutoff
            if score < beta:
                beta = score # beta acts like min in MiniMax
        return beta
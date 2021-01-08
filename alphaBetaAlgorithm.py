#https://www.chessprogramming.org/Alpha-Beta
from evaluator import Evaluator
from Chessnut import Game

class AlphaBetaAlgorithm(object):
    ev = Evaluator()

    
    def runAlg(self, game, depth):
        print(Game(game).state.player)
        print(game)
        self.alphaBetaMax(game, 9999999,9999999,depth)
        
        return bestmove

    def alphaBetaMax(self, game, alpha, beta, depthleft) :
        if depthleft == 0:
            return ev.evaluate(str(chessgame.board))
        for all moves:
            score = alphaBetaMin(alpha, beta, depthleft - 1 )
            if score >= beta:
                return beta   # fail hard beta-cutoff
            if score > alpha:
                alpha = score; # alpha acts like max in MiniMax
        return alpha

    def alphaBetaMin(self, alpha, beta, depthleft ):
        if ( depthleft == 0 ):
            return -ev.evaluate(str(chessgame.board));
        for all moves:
            score = alphaBetaMax( alpha, beta, depthleft - 1)
            if score <= alpha:
                return alpha # fail hard alpha-cutoff
            if score < beta:
                beta = score # beta acts like min in MiniMax
        return beta;
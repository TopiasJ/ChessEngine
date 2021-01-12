#https://www.chessprogramming.org/Alpha-Beta
from evaluator import Evaluator
from Chessnut import Game
from Algorithm import Algorithm
import threading
import random

class AlphaBeta(Algorithm):
    ev = Evaluator()
    scores = []

    def getBestmove(self, game, depth=2, evGene=ev):
        moves = game.get_moves()
        self.scores = []
        for move in moves:
            testGame = Game(fen=game.get_fen(),validate=False)
            testGame.apply_move(move)
            self.calcOneMove(move,testGame,depth, evGene)

        if(testGame.state.player == 'w'):
            self.scores.sort()
        else:
            self.scores.sort(reverse=True)
        #print(self.scores)
        bestScore = self.scores[0][0]
        #print('best score:' + str(bestScore))

        i = 0
        for x in self.scores:
            if x[0] != bestScore:
                break
            i += 1
        #print("number of best scores:" + str(i))
        selectedmove = random.randint(0, i-1)
        #print(selectedmove)
        #print('selected move: ' + str(self.scores[selectedmove]))
        return self.scores[selectedmove][1]

    def calcOneMove(self,move, testGame, depth, evGene):
            if testGame.state.player == 'w':
                score = self.alphaBetaMax(testGame, -999999,999999, depth, evGene)
            else:
                score = self.alphaBetaMin(testGame, -999999,999999, depth, evGene)
            self.scores.append((score,move))
            return    

    def alphaBetaMax(self, game, alpha, beta, depthleft, evGene):
        moves = game.get_moves()
        if not moves:
            depthleft = 0
        if depthleft == 0:
            return evGene.evaluate(str(game.board))
        
        for move in moves:
            testGame = Game(fen=game.get_fen(),validate=False)
            testGame.apply_move(move)
            score = self.alphaBetaMin(testGame,alpha, beta, depthleft - 1, evGene )
            if score >= beta:
                #print('beta cutoff')
                return beta   # fail hard beta-cutoff
            if score > alpha:
                alpha = score # alpha acts like max in MiniMax
        return alpha

    def alphaBetaMin(self,game, alpha, beta, depthleft, evGene ):
        moves = game.get_moves()
        if not moves:
            depthleft = 0
        if ( depthleft == 0 ):
            return evGene.evaluate(str(game.board))
        for move in moves:
            testGame = Game(fen=game.get_fen(),validate=False)
            testGame.apply_move(move)
            score = self.alphaBetaMax(testGame, alpha, beta, depthleft - 1, evGene)
            if score <= alpha:
                #print('alpha cutoff')
                return alpha # fail hard alpha-cutoff
            if score < beta:
                beta = score # beta acts like min in MiniMax
        return beta
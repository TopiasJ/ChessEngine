from evaluatorGene import EvaluatorGene
from multiprocessing import Process
from Chessnut import Game
from evaluator import Evaluator
from negaMaxAlgorithm import NegaMax
from alphaBetaAlgorithm import AlphaBeta
from boardVisualizer import Visualizer

import random
import os.path



class Tournament(object):
    tournamentWinners = []
    
    def startTournament(self, newGenesCount):
        processList = []
        self.tournamentWinners = []
        playerGenes = self.initializeNewGenes(amount=newGenesCount, variance=0.3)
        opponents = self.randomizeOpponents(playerGenes)
            

        
        for x in opponents:
            p = Process(target=self.playChessMatch, args=(x,))
            processList.append(p)
            p.start()
        
        for process in processList:
            process.join()
        self.saveWinners(self.tournamentWinners)
        return

    def initializeNewGenes(self, amount, variance):
        geneList = []
        for _ in range(amount):
            gene = EvaluatorGene() 
            gene.randomizeInitialValues(variance)
            geneList.append(gene)
        return geneList
    def breedWinners(self, winners):
        newborns = []
        previous = None
        for winner in winners :
            if previous == None:
                previous = winner
            else:
                newborns.append(winner.crossover(previous))
                previous = None
        return newborns
    def saveWinners(self, winners):
        #exists = os.path.isfile('tournamentWinners.txt')
        f = open("tournamentWinners.txt", "a")
        for winner in winners:
            f.write(str(winner.getPieceValue('R')) +','+ str(winner.getPieceValue('N')) +','+ str(winner.getPieceValue('B'))+','+ str(winner.getPieceValue('Q')) + '\n' )
        f.close()
        return

    def randomizeOpponents(self, players):
        previous = None
        opponents = []
        random.shuffle(players)
        for player in players :
            if previous == None:
                previous = player
            else:
                opponents.append((player, previous))
                previous = None
        return opponents

    def playChessMatch(self, opponents, calcDepth = 3):
        chessgame = Game()
        visualiser = Visualizer()
        alg = AlphaBeta()
        movecount = 0
        #MAIN LOOP
        while(True):
            #WHITE TO MOVE
            #print('white moving next')
            move = alg.getBestmove(chessgame, calcDepth)        
            chessgame.apply_move(move)
            if(chessgame.status == chessgame.CHECKMATE or chessgame.status == chessgame.STALEMATE):
                if chessgame.status == chessgame.CHECKMATE:
                    print('WHITE WON')
                    return self.tournamentWinners.append(opponents[0])
                break


            #BLACK TO MOVE
            #print('black moving next')
            aimove = alg.getBestmove(chessgame,calcDepth)
            chessgame.apply_move(aimove)
            movecount += 1
            visualiser.visualizeBoard(str(chessgame.board))
            print('move count: ' + str(movecount))

            if(chessgame.status == chessgame.CHECKMATE or chessgame.status == chessgame.STALEMATE):
                if chessgame.status == chessgame.CHECKMATE:
                    print('BLACK WON')
                    return self.tournamentWinners.append(opponents[1])
                break
            if(movecount > 10):
                return self.tournamentWinners.append(self.getWinnerByPieceValue(opponents, chessgame.board))
                
        #END OF MAIN LOOP

        #final visualisation
        
        visualiser.visualizeBoard(str(chessgame.board))
        if chessgame.status == chessgame.STALEMATE:
            print('STALEMATE')
        return self.tournamentWinners.append(self.getWinnerByPieceValue(opponents, chessgame.board))


    def getWinnerByPieceValue(self, opponents, board):
        ev = Evaluator()
        evaluation = ev.evaluate(str(board))
        if(evaluation < 0):
            print('BLACK WON!!!')
            return opponents[1] #black won
        else:
            print('WHITE WON!!!')
            return opponents[0] #white won
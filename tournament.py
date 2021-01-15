from evaluatorGene import EvaluatorGene
from multiprocessing import Process
from Chessnut import Game
from evaluator import Evaluator
from negaMaxAlgorithm import NegaMax
from alphaBetaAlgorithm import AlphaBeta
from boardVisualizer import Visualizer

import os
import random
import os.path
import datetime 
import copy


class Tournament(object):
    file = 'tournamentWinners.txt'
    def startTournament(self, wantedGenesCount, depth):
        oldGenes=self.loadOldGenes()
        processList = []
        tournamentWinners = []
        oldGenAmount = len(oldGenes)
        print('amount before tournament:' + str(oldGenAmount))

        playerGenes = self.initializeNewGenes(amount=(wantedGenesCount-oldGenAmount), variance=0.3)
        playerGenes.extend(oldGenes)

        opponents = self.randomizeOpponents(playerGenes)

        for x in opponents:
            #self.playBestOfMatch(x,depth)
            p = Process(target=self.playBestOfMatch, args=(x,depth,))
            processList.append(p)
            p.start()
        
        for process in processList:
            process.join()
        
        
        tournamentWinners=self.loadOldGenes(renameOld=False)    
        processList = []
        opponents = self.randomizeOpponents(tournamentWinners)
        
        print('--------------------- Winners round between ' + str(len(opponents)*2))
        for x in opponents:
            p = Process(target=self.playBestOfMatch, args=(x,depth))
            processList.append(p)
            p.start()
        for process in processList:
            process.join()
        
        tournamentWinners = self.loadOldGenes(renameOld=True, extra='.tournamentdump')
        self.doCrossoverAndMutation(tournamentWinners,wantedGenesCount)
        return

    def doCrossoverAndMutation(self, winnerGenes, wantedGenesCount):
        previous = None
        currentGeneCount = 0
        for gene in winnerGenes:
            if previous == None:
                previous = gene
            else:
                othergene = gene.crossover(previous)
                gene.mutation()
                othergene.mutation()
                self.saveWinners([gene,othergene])
                previous = None
                currentGeneCount += 2
        while(currentGeneCount < wantedGenesCount):
            random.shuffle(winnerGenes)
            gene1 = copy.deepcopy(winnerGenes[0])
            gene2 = copy.deepcopy(winnerGenes[1])
            gene2 = gene1.crossover(gene2)
            gene1.mutation()
            gene2.mutation()
            self.saveWinners([gene1,gene2])
            currentGeneCount += 2


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
        f = open(self.file, "a")
        for winner in winners:
            f.write(str(winner.getPieceValue('R')) +','+ str(winner.getPieceValue('N')) +','+ str(winner.getPieceValue('B'))+','+ str(winner.getPieceValue('Q')) + '\n' )
        f.close()
        return

    def loadOldGenes(self, renameOld = True, extra = ''):
        oldies = []
        file  = open(self.file, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            if(line != '\n'):
                line = line.replace("\n", "")
                l = line.split(',')
                gene = EvaluatorGene()
                gene.loadValues(int(l[0]),int(l[1]),int(l[2]),int(l[3]))
                oldies.append(gene)
        current_time = datetime.datetime.now()
        if(renameOld):
            os.rename(self.file, 'tournamentWinners-' + str(current_time.day) +'-' + str(current_time.hour) +'-'+str(current_time.minute) +extra+ '.txt')
        return oldies

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

    def playBestOfMatch(self, opponents, calcDepth = 3 ):
        score = 0
        ##opponent[0] as white
        score = self.playChessMatch(opponents, calcDepth, True)
        print('Score: ' +str(score)) 
        ##opponent[1] as white
        score += self.playChessMatch(opponents, calcDepth, False)
        print('Score: ' +str(score))
        ##decider opponent[0] as white
        if(score == 0):
            score += self.playChessMatch(opponents, calcDepth-1, True)
            print('AFTER DECIDER Score: ' +str(score))
        if(score > 0):
            self.saveWinners([opponents[0]])
            print('player 1 won' + str(opponents[0].getPieceValue('R')) +','+ str(opponents[0].getPieceValue('N')) +','+ str(opponents[0].getPieceValue('B'))+','+ str(opponents[0].getPieceValue('Q')) )
        else:
            self.saveWinners([opponents[1]])
            print('player 2 won'  + str(opponents[1].getPieceValue('R')) +','+ str(opponents[1].getPieceValue('N')) +','+ str(opponents[1].getPieceValue('B'))+','+ str(opponents[1].getPieceValue('Q')))
        return

    def playChessMatch(self, opponents, calcDepth = 3, playerOneWhite = True):
        chessgame = Game()
        visualiser = Visualizer()
        alg = AlphaBeta()
        movecount = 0
        if(playerOneWhite):
            whitePlayer = opponents[0]
            blackPlayer = opponents[1]
        else:
            whitePlayer = opponents[1]
            blackPlayer = opponents[0]

        #MAIN LOOP
        while(True):
            #WHITE TO MOVE
            #print('white moving next')
            aimove = alg.getBestmove(chessgame, calcDepth, whitePlayer)        
            chessgame.apply_move(aimove)
            if(chessgame.status == chessgame.CHECKMATE or chessgame.status == chessgame.STALEMATE):
                if chessgame.status == chessgame.CHECKMATE:
                    print('WHITE WON!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                    if(playerOneWhite):
                        return 1
                    else:
                        return -1
                    #self.saveWinners([opponents[0]])
                break
                    # return self.tournamentWinners.append(opponents[0])

            #BLACK TO MOVE
            #print('black moving next')
            aimove = alg.getBestmove(chessgame,calcDepth, blackPlayer)
            chessgame.apply_move(aimove)
            movecount += 1
            #visualiser.visualizeBoard(str(chessgame.board))
            print('move count: ' + str(movecount))

            if(chessgame.status == chessgame.CHECKMATE or chessgame.status == chessgame.STALEMATE):
                if chessgame.status == chessgame.CHECKMATE:
                    print('BLACK WON!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                    if(not playerOneWhite):
                        return 1
                    else:
                        return -1
                    
                    #self.saveWinners([opponents[1]])
                    #return self.tournamentWinners.append(opponents[1])
                break
            if(movecount > 75):
                winner = self.getWinnerByPieceValue(chessgame.board)
                if(playerOneWhite):
                    return winner
                else:
                    return winner*-1
                #self.saveWinners([self.getWinnerByPieceValue(opponents, chessgame.board)])
                #return self.tournamentWinners.append(self.getWinnerByPieceValue(opponents, chessgame.board))
                
        #END OF MAIN LOOP

        #final visualisation
        
        visualiser.visualizeBoard(str(chessgame.board))
        if chessgame.status == chessgame.STALEMATE:
            print('STALEMATE')
        
        winner = self.getWinnerByPieceValue(chessgame.board)
        if(playerOneWhite):
            return winner
        else:
            return winner*-1

        #self.saveWinners([self.getWinnerByPieceValue(opponents, chessgame.board)])   
        #return self.tournamentWinners.append(self.getWinnerByPieceValue(opponents, chessgame.board))


    def getWinnerByPieceValue(self, board):
        ev = Evaluator()
        evaluation = ev.evaluate(str(board))
        if(evaluation < 0):
            print('BLACK WON!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! by evaluation')
            return -1 #black won
        else:
            print('WHITE WON!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! by evaluation')
            return 1 #white won
    
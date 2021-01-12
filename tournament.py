from evaluatorGene import EvaluatorGene
import os.path

class Tournament(object):

    def startTournament(self, newGenesCount):
        playerGenes = self.initializeNewGenes(amount=newGenesCount, variance=0.3)

        return
    def initializeNewGenes(self, amount, variance):
        geneList = []
        for x in range(amount):
            gene = EvaluatorGene() 
            gene.randomizeInitialValues(variance)
            geneList.append(gene)
        return geneList
    def breedWinners(self, winners):
        newborns = []
        previous = None
        for winner in winners : #round down
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
            f.writelines(winner.getPieceValue('R') +','+ winner.getPieceValue('N') +','+ winner.getPieceValue('B')+','+ winner.getPieceValue('Q') )
        f.close()
        return
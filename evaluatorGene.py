from evaluator import Evaluator
import random
class EvaluatorGene(Evaluator):
    pawnValue = 100
    rookValue = 500
    knighValue = 300
    bishopValue = 300
    queenValue = 900
    kingValue = 10000
    def getPieceValue(self, piece):
        isWhite = piece.isupper()
        piece = piece.lower()
        value = 0
        if piece == 'p':
            value = self.pawnValue
        elif piece == 'r':
            value = self.rookValue
        elif piece == 'n':
            value = self.knighValue
        elif piece == 'b':
            value = self.bishopValue
        elif piece == 'q':
            value = self.queenValue
        elif piece == 'k':
            value = self.kingValue
        else:
            value = 0
        
        if isWhite:
            return value 
        else:
            return value * -1

    def randomizeInitialValues(self, variance = 0.3):
        self.rookValue = random.randint(self.rookValue - int(self.rookValue*variance), self.rookValue + int(self.rookValue*variance))
        self.knighValue = random.randint(self.knighValue - int(self.knighValue*variance), self.knighValue + int(self.knighValue*variance))
        self.bishopValue = random.randint(self.bishopValue - int(self.bishopValue*variance), self.bishopValue + int(self.bishopValue*variance))
        self.queenValue = random.randint(self.queenValue - int(self.queenValue*variance), self.queenValue + int(self.queenValue*variance))
        return self
    
    def loadValues(self,r,n,b,q):
        self.rookValue = r
        self.knighValue = n
        self.bishopValue = b
        self.queenValue = q
        return 
        
    def crossover(self, anotherGene):
        whatToCross = random.randint(1,4)
        if whatToCross == 1:
            print('doing crossover for rook, original values gene 1:' + str(self.rookValue) + '-- gene2:' + str(anotherGene.rookValue) )
            originalValue = self.rookValue
            self.rookValue = anotherGene.rookValue
            anotherGene.rookValue = originalValue
            print('after crossover rook values gene 1:' + str(self.rookValue) + '-- gene2:' + str(anotherGene.rookValue) )
        elif whatToCross == 2:
            print('doing crossover for knight, original values gene 1:' + str(self.knighValue) + '-- gene2:' + str(anotherGene.knighValue) )
            originalValue = self.knighValue
            self.knighValue = anotherGene.knighValue
            anotherGene.knighValue = originalValue
            print('after crossover knigh values gene 1:' + str(self.knighValue) + '-- gene2:' + str(anotherGene.knighValue) )
        elif whatToCross == 3:
            print('doing crossover for bishop, original values gene 1:' + str(self.bishopValue) + '-- gene2:' + str(anotherGene.bishopValue) )
            originalValue = self.bishopValue
            self.bishopValue = anotherGene.bishopValue
            anotherGene.bishopValue = originalValue
            print('after crossover bishop values gene 1:' + str(self.bishopValue) + '-- gene2:' + str(anotherGene.bishopValue) )
        else:
            print('doing crossover for queen, original values gene 1:' + str(self.queenValue) + '-- gene2:' + str(anotherGene.queenValue) )
            originalValue = self.queenValue
            self.queenValue = anotherGene.queenValue
            anotherGene.queenValue = originalValue
            print('after crossover queen values gene 1:' + str(self.queenValue) + '-- gene2:' + str(anotherGene.queenValue) )
        return anotherGene
    
    def mutation(self, mutationChance = 0.10):
        rando = random.randint(0, 100)
        doMutation = rando <= mutationChance*100 #chance 25% by default
        if doMutation:
            whatToMutate = random.randint(1,4)
            if whatToMutate == 1:
                originalValue = self.rookValue
                self.rookValue = random.randint(originalValue - int(originalValue/2), originalValue+ int(originalValue*2))
                print('doing mutation for rook:' + str(originalValue) + ' --- mutatedvalue: ' + str(self.rookValue))
            elif whatToMutate == 2:
                originalValue = self.knighValue
                self.knighValue = random.randint(originalValue - int(originalValue/2), originalValue+ int(originalValue*2))
                print('doing mutation for knight:' + str(originalValue) + ' --- mutatedvalue: ' + str(self.knighValue))
            elif whatToMutate == 3:
                originalValue = self.bishopValue
                self.bishopValue = random.randint(originalValue - int(originalValue/2), originalValue+ int(originalValue*2))
                print('doing mutation for bishop:' + str(originalValue) + ' --- mutatedvalue: ' + str(self.bishopValue))
            else:
                originalValue = self.queenValue
                self.queenValue = random.randint(originalValue - int(originalValue/2), originalValue+ int(originalValue*2))
                print('doing mutation for queen:' + str(originalValue) + ' --- mutatedvalue: ' + str(self.queenValue))

        return

    

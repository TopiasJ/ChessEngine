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
        self.rookValue = random.randint(self.rookValue - self.rookValue*variance, self.rookValue + self.rookValue*variance)
        self.knighValue = random.randint(self.knighValue - self.knighValue*variance, self.knighValue + self.knighValue*variance)
        self.bishopValue = random.randint(self.bishopValue - self.bishopValue*variance, self.bishopValue + self.bishopValue*variance)
        self.queenValue = random.randint(self.queenValue - self.queenValue*variance, self.queenValue + self.queenValue*variance)
        return self
    
    def loadValues(self,r,n,b,q):
        self.rookValue = r
        self.knighValue = n
        self.bishopValue = b
        self.queenValue = q
        return 
        
    def crossover(self, anotherGene):
        
        return
    
    def mutation(self):
        return

    

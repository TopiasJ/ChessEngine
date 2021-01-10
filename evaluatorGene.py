from evaluator import Evaluator
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
    def saveValuesFile(self):
        return

    def randomizeInitialValues(self):
        return
    
    def crossover(self, anotherGene):
        return
    
    def mutation(self):
        return


class Evaluator(object):
    def evaluate(self, boardState):
        currentScore = self.getBoardValue(boardState)
        return currentScore

    def getPieceValue(self, piece):
        isWhite = piece.isupper()
        piece = piece.lower()
        value = 0
        if piece == 'p':
            value = 100
        elif piece == 'r':
            value = 500
        elif piece == 'n':
            value = 300
        elif piece == 'b':
            value = 300
        elif piece == 'q':
            value = 900
        elif piece == 'k':
            value = 10000
        else:
            value = 0
        
        if isWhite:
            return value 
        else:
            return value * -1

    def getBoardValue(self, boardState):
        currentScore = 0
        allChars = [char for char in boardState]
        for square in allChars:
            currentScore += self.getPieceValue(square)
        return currentScore
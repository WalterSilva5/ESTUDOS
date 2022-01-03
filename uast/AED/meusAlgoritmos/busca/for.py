def forE(posI, posFinal):
    if posI<posFinal:
        print (posI)
        return forE(posI+1, posFinal)
        

forE(0, 10)

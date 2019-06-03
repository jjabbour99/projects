#!usr/bin/python3
import Piece
class Chessboard:

    def __init__(self,msize,nsize):
        self.pnum=0
        self.m=msize
        self.n=nsize
        self.plist=[]
        self.amt=int(msize)*int(nsize)

    def getSize(self):
        return self.amt

    def getN(self):
        return(int(self.n))

    def getM(self):
        return(int(self.m))

    def getDimensions(self):
        return m+"x"+n

    def addPiece(self,Piece):
        pnum+=1
        plist.append(Piece)

    def getSquareNumber(self,mloc,nloc):
        mloc=int(mloc)
        nloc=int(nloc)
        n=int(self.n)
        m=int(self.m)
        return (mloc*m)+nloc+1

    def onBoard(self,loc):
        if loc<0 or loc>self.n*self.m:
            return False
        else:
            return True

    def printBoard(self):
        for i in range(m):
            print("|")
            for j in range(n):
                print("---")
                for k in plist:
                    if str(i) and str(j) in k.getLocation():
                        print(k.getType()+" ")
            print('\n')

    def checkgetS(self):
        for x in range(self.m):
            for y in range(self.n):
                print(str(self.getSquareNumber(str(x),str(y)))+ " ")
            print('\n')



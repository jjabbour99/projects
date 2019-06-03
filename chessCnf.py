#!/usr/bin/python3
from Chessboard import *
import sys
def main(argv):
    if len(argv)<4: #filter command line arguments
        print("USAGE: chessCnf mdim ndim knights")
        exit(1)
    m=int(argv[1])
    n=int(argv[2])
    kn=int(argv[3])
    board=Chessboard(m,n)
    size=str(board.getSize())
    clauses=str(board.getSize()*2)
    cnf=""
    for x in range(2,m-2):
        for y in range(2,n-2):
            cnf+=toprint(board,scopes(board,x,y))
    f=open('nknights.cnf','w+')
    f.write("p cnf "+size+" "+clauses+"\n")
    f.write(cnf)
    f.close()
#returns all possible locations a knight can move
def scopes(board,mloc,nloc):
    validpositions=[]
    mvmt=[(-2,-1),(-2,+1),(+2,-1),(+2,+1),(-1,-2),(-1,+2),(+1,-2),(+1,+2)]
    for (x,y) in mvmt:
        validpositions.append([mloc+x,nloc+y])
    return validpositions

#sets up clauses and adds them to string
def toprint(board,scopelist):
    a=""
    for (x,y) in scopelist:
        number=str(board.getSquareNumber(x,y))
        a+=(number+" ")
    a+=('0'+'\n')
    for (b,c) in scopelist:
        neg="-"+str(board.getSquareNumber(b,c))
        a+=(neg+" ")
    a+=('0'+'\n')
    return a

main(sys.argv)

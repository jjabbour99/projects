#!/usr/bin/python3
from Chessboard import *
from BDD import *
import sys
def main(argv):
    if len(argv)<4: #filter command line arguments
        print("USAGE: chessCnf mdim ndim knights")
        exit(1)
    m=int(argv[1])
    n=int(argv[2])
    kn=int(argv[3])
    board=Chessboard(m,n)
    board.checkgetS()
    variables=0
    clauses=0
    cnf=""
    for x in range(m):
        for y in range(m):
            cnf+=assertN(board,kn)
            cnf+=moves(board,scopes(board,x,y),x,y,kn)
            variables+=15
            clauses+=9
    f=open('nknights.cnf','w+')
    f.write("p cnf "+str(variables)+" "+str(clauses)+"\n")
    f.write(cnf)
    f.close()
#returns all possible locations a knight can move
def scopes(board,mloc,nloc):
    validpositions=[]
    mvmt=[(-2,-1),(-2,+1),(+2,-1),(+2,+1),(-1,-2),(-1,+2),(+1,-2),(+1,+2)]
    for (x,y) in mvmt:
        if board.onBoard(board.getSquareNumber(mloc+x,nloc+y)):
            validpositions.append([mloc+x,nloc+y])
    return validpositions

#sets up location clauses and adds them to string
def moves(board,scopelist,nloc,mloc,kn):
    a=""
    for (b,c) in scopelist:
        clause="-"+str(board.getSquareNumber(nloc,mloc))+" -"+str(board.getSquareNumber(b,c))
        a+=(clause+" 0\n")
    return a
#sets up knight clauses per square and adds them to string
#def square(board,nloc,mloc,kn):
 #   a=""
  #  for x in range(1,kn+1):
   #     a+=str((board.getSquareNumber(nloc,mloc)*kn)+x)+" "
    #a+=("0\n")
   # return a
def assertN(board,kn):
    a=""
    bdd=BDD(board.getN()*board.getM(),kn)
    bdd.decideValidity()
    a+=bdd.writeAllClauses()
    
    

         
            




main(sys.argv)

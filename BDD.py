#/usr/bin/python3
from BDDVariable import *

class BDD:
    def __init__(self,levels,assertion):
        self._depth=levels
        self._truths=assertion
        self._nodes=getNodes()
        self._variables=getVariables()

    #finds amount of variables in BDD
    def getNodes(self):
        amt=0
        for x in range(self.depth):
            amt+=x
        return amt

    #sets all node variables with parameters (state,truthlevel,validity=false)
    def getVariables(self):
        varlist=[]
        numvar=0
        for layer in range(1,self.depth+1):
            for variable in range(layer):
                numvar+=1
                var=BDDVariable(numvar,variable,layer,False)
                varlist.append(var)

    #takes two adjacent nodes and returns their adjacency
    #TP if the adjacency is completed using a truth
    #FP if the adjacency is completed using a false
    #none if the two are not adjacent
    def Adjacency(self,node1,node2):
        if (abs(node1.getLevel()-node2.getLevel())==1):
            return "TP"
        elif(node1.getLevel()==node2.getLevel()):
            return "FP"
        else:
            return "None"

    #finds an adjacent variable to a node given parameters
    #a true or false path and a direction up or down the diagram
    #where direction 1 goes upward losing depth and direction 0
    #goes downward, gaining depth
    def findAdjacent(self,node1,path,direction):
        for node in self.variables:
            if (path=="TP" and direction==1):
                for data in findVariables(node1.getLevel()-1):
                    if(node1.getState()==node.getState()-(node1.getLevel()+1)):
                        return data
                        
            elif (path=="TP" and direction==0):
                for data in findVariables(node1.getLevel()+1):
                    if(node1.getState()==node.getState()+(node1.getLevel()+1)):
                        return data

            elif (path=="FP" and direction==1):
                count=0
                varlist=findVariables(node1.getLevel())
                for data in varlist:
                    count+=1
                    if (data==node1):
                        return varlist[count-1]

            elif (path=="FP" and direction==0):
                count=0
                varlist=findVariables(node1.getLevel())
                for data in varlist:
                    count+=1
                    if(data==node1):
                        return varlist[count+1]

            else:
                print("¯\_(ツ)_/¯")

    #finds all variables of a certain truth level and returns
    #a list of them
    def findVariables(self, tlevel):
        ofTruths=[]
        for node in self.variables:
            if (node.getLevel()==tlevel):
                ofTruths.append(node)
        return ofTruths
    
    #using the truth assertion, decides which variables are needed
    #to assert the certain amount of truths specified
    #True if valid, False otherwise
    def decideValidity(self):
        goalVars=findVariables(self.truths)
        varlist=[]
        countvar=0
        for variable in goalVars:
            countvar+=1
            variable.setValidity(True)
            varlist.append(variable)
            for amt in range(1,self.truths+1):
                varlist.append(findAdjacent(varlist[(countvar*amt)-1])
                varlist[countvar*amt].setValidity(True)

    #writes CNF clauses using valid assertion variables 
    def writeClausesPerNode(self,node):
        cnf=""
        #f=ite(chooser,true adjacent node, false adjacent node)
        #cnf clauses in form:
        #(-f -choose true)
        #(-f choose false)
        #(f choose -false)
        #(f -choose -true)
        #where f is the initial node
        #need to get variable name for chooser variable
        choose=len(self.variables)+node.getLayer()
        a=str(choose)
        if (node.checkValid):
            trueAdj=findAdjacent(node,'TP',0)
            falseAdj=findAdjacent(node,'FP',0)
            b=str(trueAdj.getState())
            c=str(falseAdj.getState())
            f=str(node.getState())
            if (!falseAdj.getValidity):
                cnf+=("-"+f+" "+a+" "+c+" 0\n")
                cnf+=(f+" "+a+" 0\n")
            else:
                cnf+=("-"+f+" -"+a+" "+b+" 0\n")
                cnf+=("-"+f+" "+a+" "+c+" 0\n")
                cnf+=(f+" "+a+" -"+c+" 0\n")
                cnf+=(f+" -"+a+" -"+b+" 0\n")
        return cnf

    def writeAllClauses(self):
        cnf=""
        for variable in range(self.variables):
            cnf+=writeClausesPerNode(variable)
        return cnf



            




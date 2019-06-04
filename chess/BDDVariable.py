#!/usr/bin/python3

class BDDVariable:
    def __init__(self, statvar,truth,layer,valid):
        self.state=statvar
        self.truthlevel=truth
        self.validity=valid
        self.ch=layer

    def __str__(self):
        return "BDDVariable with state %s, Truth Level %s, Layer %s, Validity %s" %(self.state,self.truthlevel, self.ch, self.validity)

    def getState(self):
        return self.state

    def getLevel(self):
        return self.truthlevel

    #-1=null, 0=false, 1=true
    def checkValid(self):
        if (self.validity):
            return True
        else:
            return False
    
    def setValidity(self, val):
        self.validity=val

    def getLayer(self):
        return self.ch

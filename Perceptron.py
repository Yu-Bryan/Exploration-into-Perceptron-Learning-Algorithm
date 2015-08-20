import numpy as np
import random
import csv
import time

class Perceptron:
    
    def __init__(self, 
                 dataset, 
                 weight,
                 filename = None
                ):
        if ( filename == None ):
            self.dataset = dataset
        else:
            with open(filename,'rb') as f:
                self.dataset = [ map(int,point) for point in list(csv.reader(f)) ] 

        self.weight = weight;
        self.x = [[1,i[0],i[1]] for i in self.dataset]
        self.y = [i[2] for i in self.dataset]
        self.y_hat = [0]* len(self.y)
        self.x_coord = [ i[0] for i in self.dataset]
        self.y_coord = [ i[1] for i in self.dataset]
        self.colors = map(lambda y: 'r' if y  == -1 else 'k' , self.y)

    def _update_weights(self,y_hat, y, weight,x):
        if y_hat != y:
            self.weight = self.weight + np.dot(x,y)

    def _sign(self,num):
        if num > 0:
            return 1
        else:
            return -1

    def _hypothesis_eq(self):
        intercept= self.weight[0]/ - self.weight[2] * 1.0
        slope = self.weight[1]/ - self.weight[2] * 1.0
        return slope,intercept
 
    def update(self):
#        self.y_hat = [ self._sign(np.dot(row,self.weight)) for row in self.x ]
#        for estimate,true,features in zip(self.y_hat, self.y, self.x):
#            self._update_weights(estimate,true,self.weight,features)    
#        return self._hypothesis_eq()

        self.y_hat = [ self._sign(np.dot(row,self.weight)) for row in self.x ]
        pick = [ (yh,y,x) for (yh,y,x) in zip(self.y_hat,self.y,self.x) if  yh != y ]
        if len(pick) > 0:
            yh,y,x = random.choice(pick)
        self._update_weights(yh,y,self.weight,x)
        return self._hypothesis_eq()
    
    def solve(self):
        while self.y_hat != self.y:
            self.update()            
        return self._hypothesis_eq()

    def print_data(self):
        print self.dataset
        print self.x
        print self.y
        print self.y_hat
        print self.x_coord
        print self.y_coord
        print self.colors
    
    def getXCoords(self):
        return self.x_coord

    def getYCoords(self):
        return self.y_coord
    
    def getColors(self):
        return self.colors

    def getYHat(self):
        return self.y_hat

    def getY(self):
        return self.y


import numpy as np

class Generator:
    
    def __init__(self,
                 lowerx = -1,
                 upperx = 1,
                 lowery = -1,
                 uppery = 1,
                 sampleSize = 1,
                 point1 = None,
                 point2 = None
                ):
        self.lowerx = lowerx
        self.lowery = lowery
        self.upperx = upperx
        self.uppery = uppery        

        if ( point1 == None and point2 == None ):
           self.point1,self.point2 = self._GeneratePoint()
        else:
            self.point1 = point1
            self.point2 = point2

        self.slope = self._CalculateSlope()
        self.intercept = self._CalculateIntercept()
        self.samples = self._GenerateSamples(sampleSize)
    
    def _GeneratePoint(self):
            xCoords = np.random.uniform(self.lowerx,self.upperx,(1,2))
            yCoords = np.random.uniform(self.lowery,self.uppery,(1,2))
            return (xCoords[0][0],yCoords[0][0]), (xCoords[0][1],yCoords[0][1])

    
    def _CalculateSlope(self):
        return (self.point2[1] - self.point1[1])/( self.point2[0] - self.point1[0])

    def _CalculateIntercept(self):
        return -self.slope * self.point1[0] + self.point1[1]
    
    def _GenerateSamples(self,n):
        return map(lambda (x,y): (x,y,1) if x*self.slope + self.intercept > y else (x,y,-1), np.random.uniform(-1,1,(n,2)))

    def reInit(self):
        self.point1, self.point2 = self._GeneratePoint()
        self.slope = self._CalculateSlope()
        self.intercept = self._CalculateIntercept()
        self.samples = self._GenerateSamples(sampleSize)

    def getPoints(self):
        return self.point1, self.point2

    def getSlope(self):
        return self.slope

    def getIntercept(self):
        return self.intercept

    def getSamples(self):
        return self.samples
    
    def getLine(self):
        return self.slope, self.intercept

    def outputLine(self,filename):
        f = open(filename,'w')
        f.write(str(self.slope) + ',' + str(self.intercept) + '\n') 
        f.close()
    
    def outputSample(self,filename):
        f = open(filename,'w')
        for (x,y,z) in self.samples:
            f.write( str(x) + ',' + str(y) + ',' + str(z) + '\n')
        f.close()


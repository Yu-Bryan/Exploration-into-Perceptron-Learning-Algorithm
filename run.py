from Perceptron import Perceptron
from Generator import Generator
import matplotlib.pyplot as plt
import time
import numpy as np

sampleSize = 10
searchSpace = [-1,1,-1,1]
rd = [-2,2,-2,2]
weights = [0.000001,0.000001,0.000001]
searchIterations = []
diff = []
rounds = 1000
lw = 3
ecSampleNum = 20
graph = False


for i in range(0,rounds):
    iterCount = 1
    g = Generator(lowerx=searchSpace[0],
                  upperx=searchSpace[1],
                  lowery=searchSpace[2],
                  uppery=searchSpace[3],
                  sampleSize=sampleSize
                )
    tSlope,tIntercept = g.getLine()
    trueFunction = map(lambda x: tSlope*x+tIntercept, range(rd[0],rd[1]+1))

    p = Perceptron(g.getSamples(),weights)

    xCoords = p.getXCoords()
    yCoords = p.getYCoords()
    colors = p.getColors()

    x = range(rd[0],rd[1]+1)
    y_val = map(lambda x : 0 ,range(rd[0],rd[1]+1))

    if graph == True:
        plt.ion()
        fig = plt.figure()
        ax = plt.subplot()
        ax.axis(rd)
        ax.axhline(0, color='black')
        ax.axvline(0, color='black')

        ax.scatter(xCoords,yCoords,s=40,c=colors)
        g1, = ax.plot(x,trueFunction,linewidth=lw)
        g2, = ax.plot(x,y_val,linewidth=lw)

        fig.canvas.draw()
    while( p.getYHat() != p.getY() ):
        iterCount += 1
        hSlope,hIntercept= p.update()
           
        if graph == True: 
            time.sleep(1)
            y_val = map(lambda x: hSlope * x + hIntercept, range(rd[0],rd[1]+1))
            g2.set_ydata(y_val)
            fig.canvas.draw()
        
    
    searchIterations.append(iterCount)

    testX = np.random.uniform(searchSpace[0],searchSpace[1],ecSampleNum)
    testY = np.random.uniform(searchSpace[2],searchSpace[3],ecSampleNum)
    testPoint = zip(testX,testY)
    true_y = map(lambda (x,y): 1 if y > (tSlope * x + tIntercept) else -1, testPoint)
    h_y = map(lambda (x,y): 1 if y > (hSlope * x + hIntercept) else -1, testPoint)
    diff.append(sum([1 for (yt,yh) in zip(true_y,h_y) if yt != yh ])*1.0 / len(testPoint)*1.0)

    plt.close()

print 'Average Iteration: ', np.mean(searchIterations)
print 'Feature - Hypothesis space: ', np.mean(diff)

f = open('Results.dat','w')
for i,d in zip(searchIterations,diff):
    f.write(str(i) + ',' + str(d) + '\n')
f.close()

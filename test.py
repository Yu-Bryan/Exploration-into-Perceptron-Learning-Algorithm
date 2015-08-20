from Generator import Generator

g = Generator(point1=(1.0,1.0),
              point2=(2.0,2.0),
              sampleSize = 2
            )

print g.getSlope()
print g.getIntercept()
print g.getSamples()

g.outputLine('out.csv')
g.outputSample('sample.csv')

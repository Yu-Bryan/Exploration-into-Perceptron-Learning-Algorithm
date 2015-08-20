from Generator import Generator
import unittest

class TestGenerator(unittest.TestCase):

    def testCase1(self):
        g = Generator(point1=(1.0,1.0),
                      point2=(2.0,2.0))
        self.assertEqual(g.getSlope(),1.0)
        self.assertEqual(g.getIntercept(),0.0)

    def testCase2(self):
        g = Generator(point1=(3.0,3.0),
                      point2=(7.0,7.0))
        self.assertEqual(g.getSlope(),1.0)
        self.assertEqual(g.getIntercept(),0.0)

    def testCase3(self):
        g = Generator(point1=(0.0,5.0),
                      point2=(1.0,7.0))
        self.assertEqual(g.getPoints(),((0.0,5.0),(1.0,7.0)))
        self.assertEqual(g.getSlope(),2.0)
        self.assertEqual(g.getIntercept(),5.0)
    
    def testCase4(self):
        g = Generator()
        self.assertIsNotNone(g.getPoints())
        self.assertIsNotNone(g.getSlope())
        self.assertIsNotNone(g.getIntercept())

if __name__ == '__main__':
    unittest.main()

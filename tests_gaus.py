import unittest
import gaus


class TestGaus(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_noSolutions(self):
        testMatrix = [[1.0, 1.25, 1.5],
                      [0.0, 1.0, 1.5],
                      [0.0, 0.0, -0.375]]
        resultFlag, resultMatrix = gaus.gaus([[0, 2, 3],
                                              [4, 5, 6],
                                              [7, 8, 9]])
        self.assertEqual(testMatrix, resultMatrix)
        self.assertEqual(False, resultFlag)

    def test_1_10(self):
        testMatrix = [[1.0, 0.0, 0.0, 0.0, -8.348385418172363],
                      [0.0, 1.0, 0.0, 0.0, -47.45685293862567],
                      [0.0, 0.0, 1.0, 0.0, -17.986036830389416],
                      [0.0, 0.0, 0.0, 1.0, -44.088809227833856]]

        resultFlag, resultMatrix = gaus.gaus([[0.32, -0.05, 0.11, -0.08, 1.25],
                                              [0.11, 0.16, -0.28, -0.06, -0.83],
                                              [0.08, -0.15, 0.0, 0.12, 1.16],
                                              [-0.21, 0.13, -0.27, 0, 0.44]])
        self.assertEqual(testMatrix, resultMatrix)
        self.assertEqual(True, resultFlag)

    def test_Test3(self):
        testMatrix = [[1.0, 0.0, -1.0],
                      [-0.0, 1.0, 2.0],
                      [0, 0, 0]]
        resultFlag, resultMatrix = gaus.gaus([[1, 2, 3],
                                              [4, 5, 6],
                                              [7, 8, 9]])
        self.assertEqual(testMatrix, resultMatrix)
        self.assertEqual(True, resultFlag)

if __name__ == '__main__':
    unittest.main()

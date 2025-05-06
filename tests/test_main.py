import unittest

from src.main import *

class TestMathOperation:

    def test_add(self):
        self.assertEqual(add(2,3),5)

    def test_sub(self):
        self.assertEqual(sub(9,7),2)
    
    def test_mul(self):
        self.assertEqual(mul(2,3),6)

    def test_div(self):
        self.assertEqual(div(3,1),3)

if __name__ == '__main__':
    unittest.main()

from calculator import add,sub,mul,div 
import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
    def test_sub(self):
            self.assertEqual(sub(8,3),5)
    def test_nul(self):
            self.assertEqual(mul(2,3),6)
    def test_div(self):
            self.assertEqual(div(8,4),2)
if __name__=="__main__":
      unittest.main()
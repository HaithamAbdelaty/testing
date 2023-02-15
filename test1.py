import unittest
from dgree import degree
class TestCar(unittest.TestCase):
    def test_deg1(self):
        self.assertEqual(degree(-1),"invalid")
    def test_deg2(self):
        self.assertEqual(degree(0),"invalid")
    def test_deg3(self):
        self.assertEqual(degree(1),"faild")
    def test_deg4(self):
        self.assertEqual(degree(49),"faild")
    def test_deg5(self):
        self.assertEqual(degree(50),"passed")
    def test_deg6(self):
        self.assertEqual(degree(51),"passed")
    def test_deg7(self):
        self.assertEqual(degree(64),"good")
    def test_deg8(self):
        self.assertEqual(degree(65),"good")
    def test_deg9(self):
        self.assertEqual(degree(66),"good")
    def test_deg10(self):
        self.assertEqual(degree(74),"v.good")
    def test_deg11(self):
        self.assertEqual(degree(75),"v.good")
    def test_deg12(self):
        self.assertEqual(degree(76),"v.good")
    def test_deg13(self):
        self.assertEqual(degree(84),"excellent")
    def test_deg14(self):
        self.assertEqual(degree(85),"excellent")
    def test_deg15(self):
        self.assertEqual(degree(86),"excellent")  
    def test_deg16(self):
        self.assertEqual(degree(99),"excellent")  
    def test_deg17(self):
        self.assertEqual(degree(100),"in")  
    def test_deg18(self):
        self.assertEqual(degree(101),"in")  
   
if __name__ == '__main__':
    unittest.main()
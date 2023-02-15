import unittest
from car import car
class TestCar(unittest.TestCase):
    def test_car1(self):
        self.assertEqual(car(-1),"invalid")
    def test_car2(self):
        self.assertEqual(car(0),"invalid")
    def test_car3(self):
        self.assertEqual(car(1),"low")
    def test_car4(self):
        self.assertEqual(car(39),"low")
    def test_car5(self):
        self.assertEqual(car(40),"normal")
    def test_car6(self):
        self.assertEqual(car(41),"normal")
    def test_car7(self):
        self.assertEqual(car(119),"normal")
    def test_car8(self):
        self.assertEqual(car(120),"high")
    def test_car9(self):
        self.assertEqual(car(121),"normal")
    def test_car10(self):
        self.assertEqual(car(199),"high")
    def test_car11(self):
        self.assertEqual(car(200),"high")
    def test_car12(self):
        self.assertEqual(car(201),"v.high")
    def test_car13(self):
        self.assertEqual(car(219),"v.high")
    def test_car14(self):
        self.assertEqual(car(220),"invalid")
    def test_car15(self):
        self.assertEqual(car(221),"invalid")  

if __name__ == '__main__':
    unittest.main()
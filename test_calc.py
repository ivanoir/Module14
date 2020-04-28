import unittest
from calc import calc_me

class CalcTest(unittest.TestCase):
    def test_add(self):
        "Сложение"
        self.assertEqual(calc_me(1, 2,"+"), 3)
        
    def test_sub(self):
        "Вычитание"
        self.assertEqual(calc_me(4, 2,"-"), 2)
        
    def test_mul(self):
        "Умножение"
        self.assertEqual(calc_me(12345679, 8,"*"), 98765432)
        
    def test_div(self):
        "Деление"
        self.assertEqual(calc_me(111111111, 9,"/"), 12345679)

    def test_exponentiation(self):
        """Возведение в степень"""
        self.assertEqual(calc_me(4, 2,"^"), 16)

    def test_div_neg(self):
        """Негативный, деление на ноль"""
        self.assertEqual(calc_me(12, 0,"/"), 'ERROR: Divide by zero!')
  
    def test_oper_neg1(self):
        """Cимвол в переменной Число1"""
        self.assertEqual(calc_me("$", 2,"+"), 'ERROR: now it is does not supported')

    def test_oper_neg2(self):
        """Cимвол в переменной Число2"""
        self.assertEqual(calc_me(4,"$","+"), 'ERROR: now it is does not supported')

    def test_oper_neg3(self):
        """Без переменной Число1"""
        self.assertEqual(calc_me(None,1,"+"), 'ERROR: send me Number1')

    def test_oper_neg4(self):
        """Без переменной Число2"""
        self.assertEqual(calc_me(1,None,"+"), 'ERROR: send me Number2')

if __name__ == '__main__':
    unittest.main(verbosity=2)

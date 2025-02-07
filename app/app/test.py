"""sample test"""

from app import calc
from django.test import SimpleTestCase


class CalcTest(SimpleTestCase):

    """test calc module"""

    def test_add_numbers(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_multiply_numbers(self):
        res = calc.multiply(5, 6)
        self.assertEqual(res, 30)

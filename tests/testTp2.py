import unittest

from Tp2 import Tp2


class TestModel(unittest.TestCase):
    # class attributes
    def setUp(self):
        self.tp1 = Tp2()

    def test_divide_nominal_case_success(self):
        # given
        # refer to setup method
        number1 = 10
        number2 = 2
        expected_result = 5

        # when
        actual_result = self.tp1.divide(number1, number2)

        # then
        self.assertEqual(expected_result, actual_result)

    def test_divide_by_zero_Exception(self):
        # given
        # refer to setup method
        number1 = 10
        number2 = 0
        expected_result = 5

        # when
        with self.assertRaises(ZeroDivisionError):
            actual_result = self.tp1.divide(number1, number2)

        # then


if __name__ == '__main__':
    unittest.main()

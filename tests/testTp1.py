import unittest

import null

from Tp1 import Tp1


class TestModel(unittest.TestCase):
    # class attributes
    tp1 = null

    def setUp(self):
        self.tp1 = Tp1()

    def test_add_nominal_case_success(self):
        # given
        # refer to setup method
        number1 = 5
        number2 = 7
        expected_result = 12

        # when
        actual_result = self.tp1.add(number1, number2)

        # then
        self.assertEqual(expected_result, actual_result)

    def test_subtract_nominal_case_success(self):
        # given
        # refer to setup method
        number1 = 5
        number2 = 7
        expected_result = -2

        # when
        actual_result = self.tp1.subtract(number1, number2)

        # then
        self.assertEqual(expected_result, actual_result)

    def test_triple_nominal_case_success(self):
        # given
        # refer to setup method
        number = 5
        expected_result = 15

        # when
        actual_result = self.tp1.triple(number)

        # then
        self.assertEqual(expected_result, actual_result)

    def test_average_nominal_case_success(self):
        # given
        # refer to setup method
        number1 = 5
        number2 = 10
        number3 = 15
        expected_result = 10

        # when
        actual_result = self.tp1.average(number1, number2, number3)

        # then
        self.assertEqual(expected_result, actual_result)

    def test_is_peer_true_success(self):
        # given
        # refer to setup method
        number = 6

        # when
        # event will be called directly by the assertion

        # then
        self.assertTrue(self.tp1.is_peer(number))

    def test_is_peer_false_success(self):
        # given
        # refer to setup method
        number = 5

        # when
        # event will be called directly by the assertion

        # then
        self.assertFalse(self.tp1.is_peer(number))

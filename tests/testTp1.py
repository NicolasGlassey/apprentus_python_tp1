import unittest

from Tp1 import Tp1


class TestModel(unittest.TestCase):
    # class attributes
    def setUp(self):
        self.tp1 = Tp1()

    # region Bonus
    # Bonus
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

    # Bonus
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

    # Bonus
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

    # endregion Bonus

    # Question 1
    def test_triple_nominal_case_success(self):
        # given
        # refer to setup method
        number = 5
        expected_result = 15

        # when
        actual_result = self.tp1.triple(number)

        # then
        self.assertEqual(expected_result, actual_result)

    # Question 2
    def test_is_peer_true_success(self):
        # given
        # refer to setup method
        number = 6

        # when
        # event will be called directly by the assertion

        # then
        self.assertTrue(self.tp1.is_peer(number))

    # Question 2
    def test_is_peer_false_success(self):
        # given
        # refer to setup method
        number = 5

        # when
        # event will be called directly by the assertion

        # then
        self.assertFalse(self.tp1.is_peer(number))

    # Question 3
    def test_multiply_nominal_case_success(self):
        # given
        multiplicand = 5
        multiplier = 3
        expected_result = 15

        # when
        actual_result = self.tp1.multiply(multiplicand, multiplier)

        # then
        self.assertEqual(actual_result, expected_result)

    # Question 4
    def test_unpair_range_nominal_case_success(self):
        # given
        range_upper_limit = 10
        expected_result = list((1, 3, 5, 7, 9))

        # when
        actual_result = self.tp1.unpair_range(range_upper_limit)

        # then
        self.assertCountEqual(expected_result, actual_result)

    # Question 5
    def test_triple_range_nominal_case_success(self):
        # given
        range_upper_limit = 10
        expected_result = list((3, 6, 9, 12, 15, 18, 21, 24, 27, 30))

        # when
        actual_result = self.tp1.triple_range(range_upper_limit)

        # then
        self.assertEqual(expected_result, actual_result)

    # Question 6
    # TODO

    # Question 7
    # TODO

    # Question 8
    def test_factorial_nominal_case_success(self):
        # given
        number = 4
        expected_result = 24

        # when
        actual_result = self.tp1.factorial(number)

        # then
        self.assertEqual(expected_result, actual_result)

    # Question 9
    def test_integer_to_boolean_nominal_case_success(self):
        # given
        numbers = list((1, 4, 3, 7))
        expected_result = list(((1, False), (4, True), (3, False), (7, False)))

        # when
        actual_result = self.tp1.integer_to_boolean(numbers)

        # then
        self.assertCountEqual(expected_result, actual_result)

    # Question 10
    def test_population_average_by_city_nominal_case_success(self):
        # given
        cities = list((('Zürich', 409241), ('Genève', 200548), ('Basel', 171513), ('Bern', 133798)))
        expected_result = 228775

        # when
        actual_result = self.tp1.population_average_by_city(cities)

        # then
        self.assertEqual(expected_result, actual_result)

    # Question 11 a
    def test_find_value_bigger_than_minimal_nominal_case_success(self):
        # given
        numbers = list((7, 1, 4, 0))
        min_value = 3
        expected_result = 4

        # when
        actual_result = self.tp1.find_value_bigger_than_minimal(numbers, min_value)

        # then
        self.assertEqual(expected_result, actual_result)

    # Question 11 b
    def test_find_value_bigger_than_minimal_none_success(self):
        # given
        numbers = list((7, 1, 4, 0))
        min_value = 8
        expected_result = None

        # when
        actual_result = self.tp1.find_value_bigger_than_minimal(numbers, min_value)

        # then
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()

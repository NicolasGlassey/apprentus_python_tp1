import unittest

import null

from Tp1 import Tp1


class TestModel(unittest.TestCase):
    # class attributes
    tp1 = null

    def setUp(self):
        self.tp1 = Tp1()

    def test_triple_nominalCase_success(self):
        # given
        # refer to setup method
        operand = 3
        actual_result = 0
        expected_result = 9

        # when
        actual_result = self.tp1.triple(operand)

        # then
        self.assertEqual(expected_result, actual_result);

if __name__ == '__main__':
    unittest.main()

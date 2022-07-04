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
        self.assertEqual(expected_result, actual_result)

    def test_is_peer_true_success(self):
        # given
        # refer to setup method
        operand = 6

        # when
        # event will be called directly by the assertion

        # then
        self.assertTrue(self.tp1.is_peer(operand))

    def test_is_peer_false_success(self):
        # given
        # refer to setup method
        operand = 5

        # when
        # event will be called directly by the assertion

        # then
        self.assertFalse(self.tp1.is_peer(operand))

if __name__ == '__main__':
    unittest.main()

import builtins
import unittest
from unittest import TestCase
from unittest.mock import patch, call

import bitcoin

class TestBitcoin(TestCase):

    @patch('builtins.input', side_effect=['10'])
    def test_bitcoin_amount_to_convert(self, mock_input):
        amount = bitcoin.get_amount()
        self.assertEqual('10', amount)

    def test_bitcoin_amount_to_convert_int_type(self):
        amount = bitcoin.get_input_value('10')
        self.assertEqual(10, amount)

    # @patch('builtins.print')
    # def test_show_results(self, mock_print):
    #     bitcoin.show_results(25)
    #     mock_print.assert_called_once_with('Your 25 bitcoins are equal to XXX.XXXXX dollars')

if __name__== "__main__":
    bitcoin.main()
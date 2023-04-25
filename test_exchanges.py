import unittest
import exchanges


class ExchangesTest(unittest.TestCase):

    def test_get_average_exchange_rate(self):
        code = 'USD'
        date = '2023-02-06'
        func = exchanges.get_average_exchange_rate(code, date)
        self.assertEqual(func, {'avg': 4.3833})

    def test_get_average_exchange_rate_type(self):
        code = 'USD'
        date = '2023-02-06'
        func = exchanges.get_average_exchange_rate(code, date)
        self.assertIsInstance(func, dict)


if __name__ == "__main__":
    unittest.main()
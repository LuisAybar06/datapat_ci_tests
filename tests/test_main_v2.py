import unittest
from my_app.main_v2 import process_numbers

class TestMain(unittest.TestCase):
    def test_process_numbers(self):
        result = process_numbers(1, 2, 3, 4, 5, 6)
        self.assertEqual(result['sum'], 21) 
        self.assertEqual(result['product'], 720) 
        self.assertEqual(result['average'], 3.5) 
        self.assertEqual(result['max'], 6) 
        self.assertEqual(result['min'], 1)

        result = process_numbers(-1, 1, -1, 1, -1, 1)
        self.assertEqual(result['sum'], 0)
        self.assertEqual(result['product'], 1)
        self.assertEqual(result['average'], 0)
        self.assertEqual(result['max'], 1)
        self.assertEqual(result['min'], -1)

        result = process_numbers(0, 0, 0, 0, 0, 0)
        self.assertEqual(result['sum'], 0)
        self.assertEqual(result['product'], 0)
        self.assertEqual(result['average'], 0)
        self.assertEqual(result['max'], 0)
        self.assertEqual(result['min'], 0)

if __name__ == '__main__':
    unittest.main()

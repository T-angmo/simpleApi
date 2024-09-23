import unittest
from app import plus

class TestAPI(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(plus(5, 6), '11')

if __name__ == '__main__':
    unittest.main()
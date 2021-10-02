import unittest
import main


class SillyNamesGeneratorTestCase(unittest.TestCase):
    def test_firstnames(self):
        self.assertIsNotNone(main.firstnames())  # add assertion here


if __name__ == '__main__':
    unittest.main()

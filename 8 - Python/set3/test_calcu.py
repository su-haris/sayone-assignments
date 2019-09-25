import unittest

from set3.calcu import Calcu


class Test(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calcu.add(self, 5, 10), 15)

    def test_sub(self):
        self.assertEqual(Calcu.sub(self, 10, 10), 0)

    def test_mul(self):
        self.assertEqual(Calcu.mul(self, 5, 10), 50)

    def test_div(self):
        self.assertEqual(Calcu.div(self, 10, 5), 2)


if __name__ == '__main__':
    unittest.main()

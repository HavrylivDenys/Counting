from counting_holes import counting_holes
import unittest


class TestCount(unittest.TestCase):
    def test_input(self):
        self.assertEqual(counting_holes([]), "Error")
        self.assertEqual(counting_holes(20.4), "Error")
        self.assertEqual(counting_holes("20.4"), "Error")
        self.assertEqual(counting_holes({}), "Error")
        self.assertEqual(counting_holes(None), "Error")

    def test_result(self):
        self.assertEqual(counting_holes("08842"), 5)
        self.assertEqual(counting_holes(20), 1)
        self.assertEqual(counting_holes(88), 4)
        self.assertEqual(counting_holes(00), 0)
        self.assertEqual(counting_holes(11), 0)


if __name__ == '__main__':
    unittest.main()

import unittest

def fibo(n):
    """returns first n elements of Fibbonaci sequence"""
    result = [1]
    return result

# [1, 1, 2, 3, 5, 8, 13]

class FiboTest(unittest.TestCase):
    def test_return_list(self):
        self.assertIsInstance(fibo(1), list)

    def test_return_one_for_one(self):
        self.assertEqual(fibo(1), [1])

    ## Test second element 2 -> 1, 1
    ## Test 7 -> [1, 1, 2, 3, 5, 8, 13]
    ## Test input TypeError for negative number

if __name__ == "__main__":
    unittest.main()


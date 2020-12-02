import unittest

def fibo(n):
    """returns first n elements of Fibbonaci sequence"""
    if n < 1:
        raise TypeError
    if n == 1:
        result = [1]
    if n > 1:
        result = [1,1]
        for i in range(n-2):
            result.append(result[-1] + result[-2])
    return result

# [1, 1, 2, 3, 5, 8, 13]

class FiboTest(unittest.TestCase):
    def test_return_list(self):
        self.assertIsInstance(fibo(1), list)

    def test_return_one_for_one(self):
        self.assertEqual(fibo(1), [1])

    ## Test second element 2 -> 1, 1
    def test_return_two_ones_for_two(self):
        self.assertEqual(fibo(2), [1, 1])
        
    ## Test 7 -> [1, 1, 2, 3, 5, 8, 13]
    def test_return_first_seven_elements(self):
        self.assertEqual(fibo(7), [1, 1, 2, 3, 5, 8, 13])

    ## Test input TypeError for negative number
    def test_raises_when_negative(self):
        with self.assertRaises(TypeError):
            fibo(-1)

if __name__ == "__main__":
    unittest.main()


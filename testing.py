import unittest
from vector import Vector

# alternatives:
# - nose
# - pytest
# - doctest - build-in

def return_dict():
    return {"one" : 1, "two" : 2}

class TypesTest(unittest.TestCase):
    def test_testing(self):
        self.assertTrue(True)

    def test_dictionary(self):
        self.assertDictEqual(return_dict(), {"one" : 1, "two" : 2})

class VectorTest(unittest.TestCase):
    def setUp(self):
        self.d = {1: "one"}
        self.pos = 1, 1

    def test_createVector(self):
        v = Vector(*self.pos)
        self.assertIsNotNone(v)

    def test_lenghtVector(self):
        v = Vector(*self.pos)
        self.assertAlmostEqual(v.distance(), 1.4142, 4)

if __name__ == "__main__":
    unittest.main()
import unittest
import random
from cursedsql import PrimeNumbersData


class PrimeNumberDataTest(unittest.TestCase):
    def test_random(self):
        blob = random.randbytes(8)
        self.assertEqual(blob, PrimeNumbersData.deserialize(PrimeNumbersData.serialize(blob)))

    def test_serialize_null(self):
        blob = f"{chr(0)}".encode()
        self.assertEqual((0x101).to_bytes(3), PrimeNumbersData.serialize(blob))

    def test_deserialize_null(self):
        blob = (0x101).to_bytes(3)
        self.assertEqual((0).to_bytes(), PrimeNumbersData.deserialize(blob))

    def test_wrong_type_serialize(self):
        self.assertRaises(TypeError, PrimeNumbersData.serialize, "test")

    def test_wrong_type_deserialize(self):
        self.assertRaises(TypeError, PrimeNumbersData.deserialize, "test")

    def test_random_many(self):
        for _ in range(100):
            self.test_random()

if __name__ == "__main__":
    unittest.main()
# fuck pycharm
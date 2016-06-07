import unittest
from url_shortener.codefy import encode, decode

class CodefyTestCase(unittest.TestCase):
    def test_encode_first_id(self):
        result = encode(1)
        self.assertEquals('1', result)

    def test_encode_id_with_two_digits(self):
        result = encode(82)
        self.assertEquals('k1', result)

    def test_decode_id_with_two_digits(self):
        result = decode('k1')
        self.assertEquals(82, result)


if __name__ == '__main__':
    unittest.main()

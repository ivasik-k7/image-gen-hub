import hashlib
import unittest

from app.utils import encode_string, normalize_string, verify_string


class TestStringEncoding(unittest.TestCase):
    def test_normalize_string(self):
        self.assertEqual(normalize_string("Café"), "cafe")
        self.assertEqual(normalize_string("  Hello World!  "), "hello world!")
        self.assertEqual(normalize_string("Pythôn"), "python")
        self.assertEqual(normalize_string("Çàt"), "cat")
        self.assertEqual(normalize_string(""), "")
        self.assertEqual(normalize_string("AlreadyNormalized"), "alreadynormalized")

    def test_encode_string(self):
        key = "secret"
        value = "message"
        expected_hash = hashlib.sha256(key.encode() + value.encode()).hexdigest()
        self.assertEqual(encode_string(value, key), expected_hash)

        algorithm = "md5"
        expected_hash_md5 = hashlib.md5(key.encode() + value.encode()).hexdigest()
        self.assertEqual(encode_string(value, key, algorithm), expected_hash_md5)

        expected_hash_empty = hashlib.sha256(b"").hexdigest()
        self.assertEqual(encode_string("", ""), expected_hash_empty)

    def test_verify_string(self):
        key = "secret"
        value = "message"

        # SHA256
        expected_hash = hashlib.sha256(key.encode() + value.encode()).hexdigest()
        self.assertTrue(verify_string(value, expected_hash, key))
        self.assertFalse(verify_string(value, "wronghash", key))

        # MD5
        algorithm = "md5"
        expected_hash_md5 = hashlib.md5(key.encode() + value.encode()).hexdigest()
        self.assertTrue(verify_string(value, expected_hash_md5, key, algorithm))
        self.assertFalse(verify_string(value, "wronghash", key, algorithm))

    def test_invalid_key(self):
        with self.assertRaises(ValueError):
            encode_string("message", 123)
        with self.assertRaises(ValueError):
            verify_string("message", "hash", 123)


if __name__ == "__main__":
    unittest.main()

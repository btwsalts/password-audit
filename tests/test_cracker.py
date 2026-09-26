import hashlib
import unittest

from cracker import audit_candidates, hash_password


class TestPasswordAudit(unittest.TestCase):
    def test_hash_password(self):
        expected = hashlib.sha256(b"password123").hexdigest()
        self.assertEqual(hash_password("password123", "sha256"), expected)

    def test_finds_password(self):
        target = hash_password("secret123", "sha256")
        result = audit_candidates(target, ["hello", "secret123", "admin"], "sha256")
        self.assertTrue(result["found"])
        self.assertEqual(result["password"], "secret123")
        self.assertEqual(result["attempts"], 2)

    def test_no_match(self):
        target = hash_password("secret123", "sha256")
        result = audit_candidates(target, ["hello", "admin"], "sha256")
        self.assertFalse(result["found"])
        self.assertIsNone(result["password"])
        self.assertEqual(result["attempts"], 2)


if __name__ == "__main__":
    unittest.main()

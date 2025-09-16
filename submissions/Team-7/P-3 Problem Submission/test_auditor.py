#!/usr/bin/env python3
"""
Unit tests for the Security Code Auditor.
"""

import unittest
import os
import tempfile
from auditor import CodeAuditor, SecurityViolation


class TestCodeAuditor(unittest.TestCase):
    """Test cases for the CodeAuditor class."""

    def setUp(self):
        """Set up test environment."""
        self.auditor = CodeAuditor()

        # Create temporary test files
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        """Clean up after tests."""
        self.temp_dir.cleanup()

    def _create_test_file(self, content):
        """Create a temporary file with the given content."""
        fd, path = tempfile.mkstemp(suffix=".py", dir=self.temp_dir.name)
        with os.fdopen(fd, "w") as f:
            f.write(content)
        return path

    def test_hardcoded_secrets(self):
        """Test detection of hardcoded secrets."""
        code = """
                # This file contains hardcoded secrets
                API_KEY = "sk_test_abcdefg123456"
                password = "super_secret_password"
                """
        file_path = self._create_test_file(code)
        violations = self.auditor.scan_file(file_path)

        self.assertEqual(len(violations), 2)
        self.assertEqual(violations[0].rule_id, "SEC-7.1")
        self.assertEqual(violations[1].rule_id, "SEC-7.1")

    def test_insecure_crypto(self):
        """Test detection of insecure cryptography."""
        code = """
                import hashlib

                def hash_password(password):
                    # Using insecure MD5
                    return hashlib.md5(password.encode()).hexdigest()
                """
        file_path = self._create_test_file(code)
        violations = self.auditor.scan_file(file_path)

        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0].rule_id, "SEC-12.1")

    def test_insecure_deserialization(self):
        """Test detection of insecure deserialization."""
        code = """
                import pickle

                def load_data(file_path):
                    with open(file_path, 'rb') as f:
                        return pickle.load(f)
                        
                data = pickle.loads(some_bytes)
                """
        file_path = self._create_test_file(code)
        violations = self.auditor.scan_file(file_path)

        self.assertEqual(len(violations), 2)
        self.assertEqual(violations[0].rule_id, "SEC-12.2")
        self.assertEqual(violations[1].rule_id, "SEC-12.2")

    def test_sql_injection(self):
        """Test detection of SQL injection vulnerabilities."""
        code = """
                def get_user(username):
                    query = "SELECT * FROM users WHERE username = '" + username + "'"
                    # Execute query...
                """
        file_path = self._create_test_file(code)
        violations = self.auditor.scan_file(file_path)

        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0].rule_id, "SEC-21.1")

    def test_clean_code(self):
        """Test that clean code produces no violations."""
        code = """
                import hashlib
                import os

                def get_api_key():
                    return os.environ.get('API_KEY')
                    
                def hash_password(password):
                    return hashlib.sha256(password.encode()).hexdigest()
                    
                def get_user(username):
                    query = "SELECT * FROM users WHERE username = %s"
                    # Execute query with parameters...
                """
        file_path = self._create_test_file(code)
        violations = self.auditor.scan_file(file_path)

        self.assertEqual(len(violations), 0)


if __name__ == "__main__":
    unittest.main()

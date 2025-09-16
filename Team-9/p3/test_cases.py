import unittest
import tempfile
import os
from auditor import audit_file

class TestAuditScript(unittest.TestCase):
    def create_temp_file(self, content):
        fd, path = tempfile.mkstemp(suffix=".py")
        with os.fdopen(fd, 'w') as tmp:
            tmp.write(content)
        return path

    def test_hardcoded_secret(self):
        code = 'api_key = "12345"\n'
        path = self.create_temp_file(code)
        issues = audit_file(path)
        os.remove(path)
        self.assertTrue(any(i['rule'] == "Hardcoded Secrets" for i in issues))

    def test_deprecated_crypto(self):
        code = 'hashlib.md5(b"test")\n'
        path = self.create_temp_file(code)
        issues = audit_file(path)
        os.remove(path)
        self.assertTrue(any(i['rule'] == "Deprecated Cryptography" for i in issues))

    def test_insecure_deserialization(self):
        code = 'import pickle\npickle.loads(data)\n'
        path = self.create_temp_file(code)
        issues = audit_file(path)
        os.remove(path)
        self.assertTrue(any(i['rule'] == "Insecure Deserialization" for i in issues))

    def test_sql_injection(self):
        code = 'query = "SELECT * FROM users WHERE username = \'" + user_input + "\'"\n'
        path = self.create_temp_file(code)
        issues = audit_file(path)
        os.remove(path)
        self.assertTrue(any(i['rule'] == "SQL Injection" for i in issues))

    def test_no_issues(self):
        code = 'api_key = os.environ.get("API_KEY")\n'
        path = self.create_temp_file(code)
        issues = audit_file(path)
        os.remove(path)
        self.assertEqual(len(issues), 0)

if __name__ == "__main__":
    unittest.main()

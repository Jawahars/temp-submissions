import unittest
import tempfile
import os
from your_module import scan_code_file  # Replace 'your_module' with the actual module name

class TestScanCodeFile(unittest.TestCase):

    def create_temp_file(self, content):
        temp = tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.py')
        temp.write(content)
        temp.close()
        return temp.name

    def test_hardcoded_secret(self):
        code = 'password = "12345"'
        file_path = self.create_temp_file(code)
        violations = scan_code_file(file_path)
        self.assertIn("Hardcoded secrets detected. Use environment variables instead.", violations)
        os.remove(file_path)

    def test_md5_usage(self):
        code = 'import hashlib\nhashlib.md5(b"test")'
        file_path = self.create_temp_file(code)
        violations = scan_code_file(file_path)
        self.assertIn("Use of MD5 detected. Use SHA-256 or higher.", violations)
        os.remove(file_path)

    def test_pickle_usage(self):
        code = 'import pickle\ndata = pickle.loads(b"some_data")'
        file_path = self.create_temp_file(code)
        violations = scan_code_file(file_path)
        self.assertIn("Use of pickle module detected. Use safer formats like JSON instead.", violations)
        os.remove(file_path)

    def test_unsafe_sql_query(self):
        code = 'query = "SELECT * FROM users WHERE name = " + input("Enter name: ")'
        file_path = self.create_temp_file(code)
        violations = scan_code_file(file_path)
        self.assertIn("Unsafe SQL query construction detected. Use parameterized queries instead of string concatenation.", violations)
        os.remove(file_path)

    def test_no_violations(self):
        code = 'import json\napi_key = os.getenv("API_KEY")'
        file_path = self.create_temp_file(code)
        violations = scan_code_file(file_path)
        self.assertEqual(len(violations), 0)
        os.remove(file_path)

if __name__ == '__main__':
    unittest.main()

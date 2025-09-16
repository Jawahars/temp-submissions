# Test Suite Documentation for Security Code Auditor

## Overview

This document describes the test suite for the Security Code Auditor. The test suite validates that the auditor correctly identifies security vulnerabilities in Python code according to the secure coding guidelines.

## Test Structure

The test suite is implemented in `test_auditor.py` using Python's built-in `unittest` framework. It contains a test class `TestCodeAuditor` with multiple test methods, each focusing on a specific security rule.

## Test Environment

Tests are run in an isolated environment using temporary files created with Python's `tempfile` module. This ensures that tests don't interfere with each other and don't leave artifacts in the filesystem.

## Test Cases

### 1. `test_hardcoded_secrets`

Tests the detection of hardcoded secrets (Section 7.1 of the guidelines).

**Test Data:**
```python
# This file contains hardcoded secrets
API_KEY = "sk_test_abcdefg123456"
password = "super_secret_password"
```

**Expected Result:** Two violations of rule SEC-7.1 should be detected.

### 2. `test_insecure_crypto`

Tests the detection of insecure cryptography (Section 12.1 of the guidelines).

**Test Data:**
```python
import hashlib

def hash_password(password):
    # Using insecure MD5
    return hashlib.md5(password.encode()).hexdigest()
```

**Expected Result:** One violation of rule SEC-12.1 should be detected.

### 3. `test_insecure_deserialization`

Tests the detection of insecure deserialization (Section 12.2 of the guidelines).

**Test Data:**
```python
import pickle

def load_data(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)
        
data = pickle.loads(some_bytes)
```

**Expected Result:** Two violations of rule SEC-12.2 should be detected.

### 4. `test_sql_injection`

Tests the detection of SQL injection vulnerabilities (Section 21.1 of the guidelines).

**Test Data:**
```python
def get_user(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    # Execute query...
```

**Expected Result:** One violation of rule SEC-21.1 should be detected.

### 5. `test_clean_code`

Tests that code without security violations is correctly identified as clean.

**Test Data:**
```python
import hashlib
import os

def get_api_key():
    return os.environ.get('API_KEY')
    
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
    
def get_user(username):
    query = "SELECT * FROM users WHERE username = %s"
    # Execute query with parameters...
```

**Expected Result:** No violations should be detected.

## Running the Tests

To run the test suite:

```bash
python3 -m unittest test_auditor.py
```

## Test Helper Methods

### `setUp`

Initializes the test environment by creating a `CodeAuditor` instance and setting up a temporary directory.

### `tearDown`

Cleans up the test environment by removing the temporary directory.

### `_create_test_file`

Creates a temporary file with the given content for testing.

## Extending the Test Suite

To add new tests:

1. Add a new test method to the `TestCodeAuditor` class
2. Create test data that contains the security vulnerability to test
3. Use `self._create_test_file(code)` to create a temporary file with the test data
4. Call `self.auditor.scan_file(file_path)` to scan the file
5. Use assertions to verify that the expected violations are detected

Example:

```python
def test_new_vulnerability(self):
    """Test detection of a new type of vulnerability."""
    code = """
    # Code with the vulnerability
    """
    file_path = self._create_test_file(code)
    violations = self.auditor.scan_file(file_path)
    
    self.assertEqual(len(violations), 1)
    self.assertEqual(violations[0].rule_id, "SEC-X.Y")
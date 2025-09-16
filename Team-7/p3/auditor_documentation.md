# Security Code Auditor Documentation

## Overview

The Security Code Auditor is a Python tool designed to scan Python code for security vulnerabilities based on established secure coding guidelines. It identifies common security issues such as hardcoded secrets, insecure cryptography, insecure deserialization, and SQL injection vulnerabilities.

## Features

- **Automated Security Scanning**: Scans Python files for security violations
- **Rule-Based Detection**: Uses pattern matching to identify potential security issues
- **Detailed Reporting**: Provides line numbers and code snippets for identified vulnerabilities
- **Command-Line Interface**: Easy to use from the terminal

## Security Rules Implemented

The auditor currently checks for the following security violations:

1. **Hardcoded Secrets (SEC-7.1)**
   - Detects passwords, API keys, or tokens hardcoded in source files
   - Pattern: Variables named like "password", "secret", "token", "api_key" with string literals

2. **Insecure Cryptography (SEC-12.1)**
   - Identifies use of deprecated cryptographic functions
   - Currently detects: `hashlib.md5()` usage

3. **Insecure Deserialization (SEC-12.2)**
   - Detects use of the insecure `pickle` module for deserialization
   - Checks for `pickle.loads()` and `pickle.load()` calls

4. **SQL Injection (SEC-21.1)**
   - Identifies potential SQL injection vulnerabilities
   - Detects SQL queries with string concatenation of variables

## Usage

### Command Line

```bash
python auditor.py <file_to_scan>
```

### Example

```bash
python auditor.py vulnerable_code.py
```

### Sample Output

```
Security Audit Report for vulnerable_code.py
==================================================
Found 4 potential security violations:

1. Violation Found: Hardcoded secret detected on line 7.
   Line 7: db_password = "password123!" # Violation 1: Hardcoded Secret

2. Violation Found: Insecure deserialization using pickle module on line 13.
   Line 13: data = pickle.loads(serialized_data) # Violation 2: Insecure Pickle

3. Violation Found: Insecure library 'hashlib.md5' used on line 18.
   Line 18: return hashlib.md5(p.encode()).hexdigest() # Violation 2: Insecure MD5

4. Violation Found: Potential SQL injection vulnerability on line 23.
   Line 23: db_query = "SELECT * FROM products WHERE name = '" + query + "'" # Violation 3: No Input Sanitization
```

## Architecture

### Classes

#### SecurityViolation

Represents a security violation found in code.

**Attributes:**
- `rule_id`: Identifier for the security rule (e.g., "SEC-7.1")
- `description`: Description of the violation
- `line_number`: Line number where the violation was found
- `line_content`: Content of the line containing the violation

#### CodeAuditor

Main class that scans code for security violations.

**Methods:**
- `scan_file(file_path)`: Scans a file for security violations
- `print_report(violations, file_path)`: Prints a report of the violations found

**Private Methods:**
- `_setup_rules()`: Sets up the security rules to check
- `_check_hardcoded_secrets(line, line_number, match)`: Checks for hardcoded secrets
- `_check_insecure_crypto(line, line_number, match)`: Checks for insecure cryptography
- `_check_insecure_deserialization(line, line_number, match)`: Checks for insecure deserialization
- `_check_sql_injection(line, line_number, match)`: Checks for SQL injection vulnerabilities

## Extending the Auditor

To add new security rules:

1. Add a new rule definition in the `_setup_rules()` method:
   ```python
   self.rules.append({
       'id': 'SEC-X.Y',
       'name': 'Rule Name',
       'description': 'Description of the rule',
       'pattern': r'regex_pattern',
       'check_function': self._check_function_name
   })
   ```

2. Implement the corresponding check function:
   ```python
   def _check_function_name(self, line: str, line_number: int, match) -> SecurityViolation:
       return SecurityViolation(
           rule_id="SEC-X.Y",
           description="Description of violation",
           line_number=line_number,
           line_content=line
       )
   ```

## Limitations

- The auditor uses regex pattern matching, which may produce false positives or miss complex vulnerabilities
- Currently only scans Python files
- Limited to the security rules explicitly defined in the code
- Does not perform data flow analysis or context-aware scanning

## Future Enhancements

- Support for additional programming languages
- More comprehensive security rules
- Integration with CI/CD pipelines
- Configuration options for customizing rules
- Severity levels for violations
- Suggestions for fixing identified issues
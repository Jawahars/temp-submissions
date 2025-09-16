import re
import os

# Function to scan a Python file for specific security violations
def scan_code_file(file_path):
    violations = []

    with open(file_path, 'r') as f:
        code = f.read()

    # Section 7: Secret Management - Hardcoded secrets
    if re.search(r'(?i)(password|api[_-]?key|secret)[\s]*=[\s]*["\'][^"\']+["\']', code):
        violations.append("Hardcoded secrets detected. Use environment variables instead.")

    # Section 12: Use of Approved Libraries - MD5 usage
    if re.search(r'hashlib\.md5', code):
        violations.append("Use of MD5 detected. Use SHA-256 or higher.")

    # Section 12: Use of Approved Libraries - Pickle usage
    if re.search(r'import\s+pickle', code) or re.search(r'pickle\.', code):
        violations.append("Use of pickle module detected. Use safer formats like JSON instead.")

    # Section 21: Input Validation - Unsafe SQL query construction
    if re.search(r'(SELECT|INSERT|UPDATE|DELETE).*?\+.*?(input|request)', code, re.IGNORECASE):
        violations.append("Unsafe SQL query construction detected. Use parameterized queries instead of string concatenation.")

    return violations

# Example usage
file_to_scan = 'example_code.py'  # Replace with actual file path
if os.path.exists(file_to_scan):
    results = scan_code_file(file_to_scan)
    if results:
        print("Violations found:")
        for violation in results:
            print(f"- {violation}")
    else:
        print("No violations found.")
else:
    print(f"File '{file_to_scan}' does not exist.")
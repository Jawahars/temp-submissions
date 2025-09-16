# Assisted by watsonx Code Assistant
import os
import pickle
import hashlib
import re
# Key rules extracted manually for PoC
KEY_RULES = {
    "Secret Management": [
        r"(?i)password|api_key|token\s*=\s*['\"](.*?)['\"]",  # Hardcoded secrets
        r"(?i)os\.environ\.get\(\s*\"API_\w+\""  # Using environment variables
    ],
    "Cryptography": [
        r"(?i)hashlib\.md5"  # Insecure MD5
    ],
    "Data Interchange": [
        r"(?i)pickle\.",  # Using pickle
    ],
    "Input Validation": [
        r"(?i)SELECT\s+.*FROM\s+.*WHERE\s+.*=\s*'(.*?)'",  # No input sanitization
    ]
}
def check_for_violations(code, rules):
    violations = []
    for rule_name, patterns in rules.items():
        for pattern in patterns:
            matches = re.findall(pattern, code)
            if matches:
                violations.append({
                    "rule": rule_name,
                    "description": f"Potential violation of '{rule_name}'.",
                    "examples": matches
                })
    return violations
def analyze_code(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()
        violations = check_for_violations(code, KEY_RULES)
        if violations:
            print("Detected potential security violations:")
            for violation in violations:
                print(f"- {violation['rule']}: {violation['description']}")
                print(f"  Examples: {violation['examples']}")
        else:
            print("No potential security violations detected.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
# Replace 'your_script.py' with the path to the Python file you want to analyze
analyze_code('auditor.py')
import re
class Auditor:
    def __init__(self, code_file, rules):
        self.code_file = code_file
        self.rules = rules
    def scan_code(self):
        try:
            with open(self.code_file, 'r') as file:
                code = file.read()
                return self.apply_rules(code)
        except FileNotFoundError:
            print("File not found")
            return []
    def apply_rules(self, code):
        violations = []
        for rule in self.rules:
            for pattern in rule['patterns']:
                if re.search(pattern, code):
                    violations.append(f"Violation of rule '{rule['name']}': {pattern}")
        return violations
# Define rules to check for
rules = [
    {'name': 'Insecure library', 'patterns': [r'import hashlib\.md5', r'hashlib\.md5\(']},
    {'name': 'Hardcoded password', 'patterns': [r'password\s*=\s*["\']']},
    {'name': 'SQL injection (username/password)', 'patterns': [
        r"cursor\.execute\s*\(\s*['\"](SELECT.*)?FROM\s+products\s+WHERE\s+name\s*=\s*['\"](.*?)[\"\']",
    ]}
]
# Initialize auditor and scan code
auditor = Auditor('vulnerable_code.py', rules)  # Replace 'example.py' with your code file
violations = auditor.scan_code()
# Print found violations
for violation in violations:
    print(violation)

# Violation of rule 'Insecure library': hashlib\.md5\(
# Violation of rule 'Hardcoded password': password\s*=\s*["\']

# Violation of rule 'Insecure library': hashlib\.md5\(
# Violation of rule 'Hardcoded password': password\s*=\s*["\']
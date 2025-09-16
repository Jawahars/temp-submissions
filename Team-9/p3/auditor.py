import re
import sys
SECURE_RULES = [
    {
        "name": "Hardcoded Secrets",
        "pattern": re.compile(r'(api_key|password|token)\s*=\s*["\'].*["\']', re.IGNORECASE),
        "message": "Hardcoded secret detected. Use environment variables instead."
    },
    {
        "name": "Deprecated Cryptography",
        "pattern": re.compile(r'hashlib\.md5\s*\('),
        "message": "MD5 is deprecated. Use SHA-256 or higher."
    },
    {
        "name": "Insecure Deserialization",
        "pattern": re.compile(r'(import\s+pickle|pickle\.loads\s*\()'),
        "message": "Insecure deserialization with pickle detected. Use JSON or safer formats."
    },
    {
        "name": "SQL Injection",
        "pattern": re.compile(r'(["\']SELECT.*["\']\s*\+\s*\w+)', re.IGNORECASE),
        "message": "Possible SQL injection risk. Use parameterized queries."
    }
]
def audit_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    issues = []
    for idx, line in enumerate(lines, 1):
        for rule in SECURE_RULES:
            if rule["pattern"].search(line):
                issues.append({
                    "line": idx,
                    "rule": rule["name"],
                    "message": rule["message"],
                    "code": line.strip()
                })
    return issues
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python audit_script.py <source_file.py>")
        sys.exit(1)
    issues = audit_file(sys.argv[1])
    if not issues:
        print("No issues found. Source code complies with secure coding guidelines.")
    else:
        print("Security Audit Report:")
        for issue in issues:
            print(f"Line {issue['line']}: [{issue['rule']}] {issue['message']}")

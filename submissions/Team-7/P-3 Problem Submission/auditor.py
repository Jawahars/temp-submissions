#!/usr/bin/env python3
"""
Security Code Auditor
This script scans Python code for security violations based on secure coding guidelines.
"""

import re
import sys
import os
from typing import List, Dict, Tuple, Any


class SecurityViolation:
    """Represents a security violation found in code."""
    
    def __init__(self, rule_id: str, description: str, line_number: int, line_content: str):
        self.rule_id = rule_id
        self.description = description
        self.line_number = line_number
        self.line_content = line_content
    
    def __str__(self) -> str:
        return f"Violation Found: {self.description} on line {self.line_number}."


class CodeAuditor:
    """Scans code for security violations."""
    
    def __init__(self):
        # Initialize rules
        self.rules = []
        self._setup_rules()
    
    def _setup_rules(self):
        """Set up the security rules to check."""
        # Rule 1: Hardcoded Secrets (Section 7.1)
        self.rules.append({
            'id': 'SEC-7.1',
            'name': 'Hardcoded Secrets',
            'description': 'Hardcoded sensitive information such as passwords, API keys, or tokens',
            'pattern': r'(?i)(?:password|passwd|pwd|secret|token|api_?key)\s*=\s*["\'][^"\']+["\']',
            'check_function': self._check_hardcoded_secrets
        })
        
        # Rule 2: Insecure Cryptography (Section 12.1)
        self.rules.append({
            'id': 'SEC-12.1',
            'name': 'Deprecated Cryptography',
            'description': 'Insecure library \'hashlib.md5\' used',
            'pattern': r'hashlib\.md5\(',
            'check_function': self._check_insecure_crypto
        })
        
        # Rule 3: Insecure Deserialization (Section 12.2)
        self.rules.append({
            'id': 'SEC-12.2',
            'name': 'Insecure Deserialization',
            'description': 'Insecure deserialization using pickle module',
            'pattern': r'pickle\.(loads|load)\(',
            'check_function': self._check_insecure_deserialization
        })
        
        # Rule 4: SQL Injection (Section 21.1)
        self.rules.append({
            'id': 'SEC-21.1',
            'name': 'SQL Injection',
            'description': 'Potential SQL injection vulnerability',
            'pattern': r'(?:SELECT|INSERT|UPDATE|DELETE).*\+\s*(?:\w+|\w+\[.+\])',
            'check_function': self._check_sql_injection
        })
    
    def _check_hardcoded_secrets(self, line: str, line_number: int, match) -> SecurityViolation:
        """Check for hardcoded secrets."""
        return SecurityViolation(
            rule_id="SEC-7.1",
            description="Hardcoded secret detected",
            line_number=line_number,
            line_content=line
        )
    
    def _check_insecure_crypto(self, line: str, line_number: int, match) -> SecurityViolation:
        """Check for insecure cryptography."""
        return SecurityViolation(
            rule_id="SEC-12.1",
            description="Insecure library 'hashlib.md5' used",
            line_number=line_number,
            line_content=line
        )
    
    def _check_insecure_deserialization(self, line: str, line_number: int, match) -> SecurityViolation:
        """Check for insecure deserialization."""
        return SecurityViolation(
            rule_id="SEC-12.2",
            description="Insecure deserialization using pickle module",
            line_number=line_number,
            line_content=line
        )
    
    def _check_sql_injection(self, line: str, line_number: int, match) -> SecurityViolation:
        """Check for SQL injection vulnerabilities."""
        return SecurityViolation(
            rule_id="SEC-21.1",
            description="Potential SQL injection vulnerability",
            line_number=line_number,
            line_content=line
        )
    
    def scan_file(self, file_path: str) -> List[SecurityViolation]:
        """
        Scan a file for security violations.
        
        Args:
            file_path: Path to the file to scan
            
        Returns:
            List of SecurityViolation objects
        """
        violations = []
        
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            for line_number, line in enumerate(lines, 1):
                for rule in self.rules:
                    pattern = rule['pattern']
                    matches = re.finditer(pattern, line)
                    
                    for match in matches:
                        check_function = rule['check_function']
                        violation = check_function(line, line_number, match)
                        violations.append(violation)
                
        except Exception as e:
            print(f"Error scanning file {file_path}: {e}")
            
        return violations
    
    def print_report(self, violations: List[SecurityViolation], file_path: str):
        """Print a report of the violations found."""
        if not violations:
            print(f"No security violations found in {file_path}")
            return
            
        print(f"\nSecurity Audit Report for {file_path}")
        print("=" * 50)
        print(f"Found {len(violations)} potential security violations:\n")
        
        for i, violation in enumerate(violations, 1):
            print(f"{i}. {violation}")
            print(f"   Line {violation.line_number}: {violation.line_content.strip()}")
            print()


def main():
    """Main entry point for the script."""
    if len(sys.argv) < 2:
        print("Usage: python auditor.py <file_to_scan>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
        
    auditor = CodeAuditor()
    violations = auditor.scan_file(file_path)
    auditor.print_report(violations, file_path)


if __name__ == "__main__":
    main()

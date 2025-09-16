import os
import pickle
import hashlib

# WARNING: This file contains intentional security vulnerabilities for testing purposes.

db_password = "password123!" # Violation 1: Hardcoded Secret

def get_user_data(user_id):
    # This function is supposed to get data from a legacy system
    # It uses a deprecated and insecure library
    serialized_data = b'\x80\x04\x95\x1a\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x04John\x94\x8c\x04age\x94K\x1e\x94u.'
    data = pickle.loads(serialized_data) # Violation 2: Insecure Pickle
    return data

def hash_password(p):
    # Using an outdated hashing algorithm
    return hashlib.md5(p.encode()).hexdigest() # Violation 2: Insecure MD5

def search_products(query):
    # This function is vulnerable to injection
    # It doesn't sanitize user input before using it in a "database" query
    db_query = "SELECT * FROM products WHERE name = '" + query + "'" # Violation 3: No Input Sanitization
    print(f"Executing: {db_query}")
    # ... database logic would follow
    return []
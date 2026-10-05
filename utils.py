import hashlib
import random

def hash_password(password):
    # INTENTIONAL WEAK HASHING DEMO
    return hashlib.md5(password.encode()).hexdigest()

def generate_random_token():
    # INTENTIONAL INSECURE RANDOMNESS
    return str(random.random())

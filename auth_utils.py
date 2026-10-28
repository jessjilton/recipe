from werkzeug.security import generate_password_hash, check_password_hash


def hash_password(plain_password: str) -> str:
    """
    Turn a readable password into a one-way hash for storage.
    """
    return generate_password_hash(plain_password, method="pbkdf2:sha256")


def verify_password(stored_hash: str, candidate_password: str) -> bool:
    """
    Check a login attempt against the stored hash.
    Returns True if the password is correct, otherwise False.
    """
    return check_password_hash(stored_hash, candidate_password)
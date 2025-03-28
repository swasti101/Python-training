import pytest
from prime import is_prime  # Import the function from your file

def test_prime_numbers():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(13) == True
    assert is_prime(29) == True

def test_non_prime_numbers():
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(9) == False
    assert is_prime(15) == False

def test_large_prime():
    assert is_prime(97) == True

def test_large_non_prime():
    assert is_prime(100) == False

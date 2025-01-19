"""
This script calculates the twin primes up to the users input (which is defined by a slider)
Date: 18-01-2025
Version: 1.00
"""

def sieve_of_eratosthenes(user):
    """
    Uses the Sieve of Eratosthenes method of finding a set of prime numbers
    :param user: users input from slider
    :return: a list containing the set of primes number up to user
    """
    primes = [True for i in range(user + 1)]
    i = 2
    # squaring avoids checking the same number
    # only need to check up to the sqrt of the user because any pf > sqrt of n would already have been found
    while i * i <= user:
        if primes[i]:
            for j in range(i * i, user + 1, i):
                primes[j] = False
        i += 1

    primes = primes[2:len(primes)]
    values = []
    for i in range(0, len(primes)):
        if primes[i]:
            values.append(i + 2)  # adding 2 due to 0 and 1

    return values

def twin_primes(values):
    """
    Finds all twin primes - assuming every value is already a prime
    :param values: list of prime numbers
    :return: a 2D list containing every pair of twin primes
    """
    values = values[1:len(values)]  # take off the 2 because 2,3 is not a twin pair
    pairs = []
    for i in range(0, len(values) - 1):
        if values[i + 1] - values[i] == 2:
            pairs.append([values[i], values[i + 1]])

    return pairs
"""
This script creates a scatter plot of the set of twin primes
Date: 19-01-2025
Version: 1.01
"""

import twin_primes as tp
import matplotlib.pyplot as plt
import numpy as np


def create_plot():
    """
    Creates a scatter plot of the 'coordinates' of a twin prime
    :return: None
    """
    list_of_primes = tp.sieve_of_eratosthenes(256)
    pairs = tp.twin_primes(list_of_primes)

    x = [p[0] for p in pairs]
    y = [p[1] for p in pairs]

    colors = np.arange(len(pairs))
    plt.figure(num='Twin Primes Distribution')
    plt.scatter(x, y, c=colors, cmap='jet', s=15, label='Twin Primes')
    plt.title('Twin Primes', fontsize=12, fontweight='bold')

    plt.xlabel('Prime 1')
    plt.ylabel('Prime 2')
    plt.show()

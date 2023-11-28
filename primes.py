"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

import math

#Checks if number is prime
def isPrime(n):
    if n==2:
        return True
    if n%2==0:
        return False
    sqr = int(math.sqrt(n))+1
    for div in range (3,sqr,2):
        if n%div==0:
             return False
    return True

def primes(number_of_primes):
    if (number_of_primes<1):
        raise ValueError()
        return
    primeList=[]
    number=2 #As 0 and 1 are not prime no need to check
    while len(primeList)<number_of_primes:
        if isPrime(number): primeList.append(number) 
        number+=1
    return primeList

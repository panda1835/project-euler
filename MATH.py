import math

class Prime():

    def is_prime(n):
        """
        Primality test using 6k+-1 optimization.
        """
        if n <= 3:
            return n > 1
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i ** 2 <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def sieve_of_Eratosthenes(n):
        """
        Implement Sieve of Eratosthenes algorithm
        return a list of primes less than n
        """
        numbers = [True for i in range((n+1)//2)]
        primes = [2]
        numbers[0] = False # eliminate 1
        for i in range(1, (n+1)//2):
            num = 2*i + 1
            if numbers[i] == True:
                primes.append(num)
                if (num < math.sqrt(n)):
                    p = 0
                    while num**2 + num*p <= n:
                        numbers[(num**2+p*num)//2] = False 
                        p+= 2
                    
        return primes

class Divisibility():

    def list_divisor(n):
        """
        Find a list of divisors of n
        """
        divisors = []
        for i in range(1, n+1):
            if n%i == 0:
                divisors.append(i)
        return divisors

class Sequence():

    def triangular(n):
        """
        return a list of triangular numbers up to a length
        """
        triangular_numbers = []
        for i in range(n):
            triangular_numbers.append(triangular_at(i+1))
        return triangular_numbers

    def triangular_at(n):
        """
        return a triangular number at position n-th
        """
        return int(n*(n+1)/2)
    
    def collatz(n):
        """
        return a list of Collatz numbers from initial element n
        """
        collatz_numbers = [n]
        while n != 1:
            if n%2 == 0:
                n = n//2
            else:
                n = 3*n+1
            collatz_numbers.append(n)

        return collatz_numbers 
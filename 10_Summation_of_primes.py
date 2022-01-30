from Template import Template
from MATH import Prime
import random

class Problem10(Template):
    def input_generator(self):
        return random.randint(10000, 100000)

    def solution(self, inp):
        """
        Sieve of Eratosthenes
        """
        sum = 0
        for i in Prime.sieve_of_Eratosthenes(inp):
            sum  += i
        return sum

    def solution_1(self, inp):
        """
        Brute force
        """
        sum = 2
        for i in range(3, inp+1, 2):
            if Prime.is_prime(i):
                sum += i
        return sum


solution = Problem10()
solution.run_with_timer(solution.solution, 2000000)

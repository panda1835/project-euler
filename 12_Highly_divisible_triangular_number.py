from Template import Template
from MATH import Sequence
from MATH import Divisibility

class Problem12(Template):
    def solution(self, inp):
        number = 5
        while True:
            current_number = Sequence.triangular_at(number)
            num_divisors = len(Divisibility.list_divisor(current_number))
            # print(current_number, num_divisors)
            if num_divisors > inp:
                return Sequence.triangular_at(number)
            number += 1
    
    

solution = Problem12()
solution.run_with_timer(solution.solution, 500, alarm=True)
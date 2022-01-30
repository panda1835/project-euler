from Template import Template
from MATH import Sequence

class Problem14(Template):
    def solution(self, inp):
        """
        Execution time: 16.7312s
        """
        max_length = 0
        initital = 1
        for i in range(1, inp):
            l = len(Sequence.collatz(i))
            if l > max_length:
                max_length = l
                initital = i
        return initital
    

solution = Problem14()
solution.run_with_timer(solution.solution, 1000000, alarm=True)
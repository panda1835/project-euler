from Template import Template

class Problem09(Template):
    def input_generator(self):
        return 1000

    def solution_1(self, inp):
        for i in range (1, inp):
            for j in range(1, inp):
                for k in range(1, inp):
                    if (i+j+k == inp) and (i**2 + j**2 == k**2):
                        return i*j*k
    
    def solution_2(self, inp):
        for i in range (1, inp//2):
            for j in range(1, inp//2):
                    if (i**2 + j**2 == (inp-i-j)**2):
                        return i*j*(inp-i-j)
    

solution = Problem09()
solution.compare_result(solution.solution_1, solution.solution_2, 2)
print('-----------')
solution.compare_runtime(solution.solution_1, solution.solution_2, 2)

print("Iloveu")
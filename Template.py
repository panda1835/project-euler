import time
import os

class Template():

    def __init__(self):
        pass

    def solution(self, inp):
        # code here
        return

    # ----------------------#
    def run_with_timer(self, solution, inp, alarm = False):
        start_time = time.time()
        print("Result:", solution(inp))
        print("Execution time: %s seconds" % (time.time() - start_time))
        if alarm:
            os.system('spd-say "Done"')


    def timer(self, solution, inp):
        start_time = time.time()
        solution(inp)
        return (time.time() - start_time) 

    def run(self, solution, inp, alarm = False):
        print(solution(inp))
        if alarm:
            os.system('spd-say "Done"')

    def input_generator(self):
        # randomly generate an input
        return

    def compare_result(self, solution_1, solution_2, iteration = 10):
        """
        Compare the result of solution_11 and solution_12 method
        @solution_11 correct method
        @solution_12 alternative approach
        """            
        print(f"COMPARE RESULTS ({iteration} iterations):")
        for i in range(iteration):
            inp = self.input_generator()
            correct = solution_1(inp)
            alter = solution_2(inp)
            if alter == correct:
                print(f"Test {i}: Success with input {inp}")
                print("===================")
            else:
                print(f"   Test {i}: Failed with input {inp}")
                print(f"   The answer is {alter} while it is expected {correct}")
                print("===================")
    
    def compare_runtime(self, solution_1, solution_2, iteration = 10):
        """
        Compare the runtime of solution_1 and solution_2 method
        @solution_1 correct method
        @solution_2 alternative approach
        """            
        print(f"COMPARE RUNTIME solution_1 - solution_2 ({iteration} iterations):")
        for i in range(iteration):
            inp = self.input_generator()
            correct_timer = self.timer(solution_1, inp)
            alter_timer = self.timer(solution_2, inp)
            
            print(f"Test {i}: {round(correct_timer - alter_timer,5)}s with input {inp}")
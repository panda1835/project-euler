import time
import math
import random

def main(pos=10001):
    def is_prime(n):
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True
    counter = 0
    prime = 1
    while counter < pos:
        prime += 1
        if is_prime(prime):
            counter += 1 
    return prime

def main2(pos=10001):
    # another approach 
    return 

# ----------------------#
def timer(main):
    start_time = time.time()
    print(main())
    print("Execution time: %s seconds" % (time.time() - start_time))

def compare(main, main2, interation = 10):
    """
    Compare the result of main1 and main2 method
    @main1 correct method
    @main2 alternative approach
    """
    def input_generator():
        # randomly generate an input
        return random.randint(10, 100000)

    for i in range(interation):
        inp = input_generator()
        correct = main(inp)
        alter = main2(inp)
        if alter == correct:
            print(f"Test {i}: Correct with input {inp}.")
        else:
            print(f"Test {i}: Incorrect with input {inp}.")
            print(f"The answer is {alter} while it is expected {correct}.")

timer(main)
# compare(main, main2)
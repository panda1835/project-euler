from Template import Template

class Problem13(Template):
    def solution(self, inp):
        f = open('Dataset/13.txt', 'r')
        number = f.readlines()
        f.close()
        sum = 0
        for i in number:
            sum += int(i)
        return str(sum)[:inp]
    

solution = Problem13()
solution.run(solution.solution, 10, alarm=True)
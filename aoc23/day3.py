from .solution import Solution, add_solution

class Day3Part1(Solution):
    def solve(self, data, is_sample):
        for line in data:
            r = line.split(".")
            print(r)
            


        return 0
add_solution(3, 1, Day3Part1())

class Day3Part2(Solution):
    def solve(self, data, is_sample):
        return 0
add_solution(3, 2, Day3Part2())

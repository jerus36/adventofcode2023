from .solution import Solution, add_solution
import numpy as np
from functools import reduce

def parse_line(line):
    label,results = line.split(":")
    trials = [t.split(",") for t in results.split(";")]

    data = [[d.strip().split(" ") for d in t] for t in trials]
    ret = list()
    mr = {}
    for d in data:
        r = {}

        for v in d:
            mr[v[1]] = max(mr.get(v[1],0),int(v[0]))
            r[v[1]] = int(v[0])
        
        ret.append((
            r.get('red',0),
            r.get('green',0),
            r.get('blue',0),
        ))
    mv = (mr.get('red',0),mr.get('green',0),mr.get('blue',0))

    return int(label.split(" ")[1]), tuple(ret), mv

class Day2Part1(Solution):
    def solve(self, data, is_sample):
        possible = []

        limit = (12,13,14)

        for line in data:
            label, results,max_vals = parse_line(line)
            if all(np.less_equal(max_vals, limit)):
                possible.append(label)

        return sum(possible)
add_solution(2, 1, Day2Part1())

class Day2Part2(Solution):
    def solve(self, data, is_sample):
        power = []

        for line in data:
            label, results,max_vals = parse_line(line)
            power.append(reduce(lambda x,y: x*y, max_vals))

        return sum(power)
    
add_solution(2, 2, Day2Part2())

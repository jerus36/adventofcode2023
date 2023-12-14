from .solution import Solution, add_solution
import re
import math

def map_match(y,match):
    points = [(x,y) for x in range(*match.span())]
    return (points,match.group(0))

def find_points(data):
    symbols = []
    parts = []
    for y,line in enumerate(data):
        lmb_match = lambda m: map_match(y,m)
        line=line.strip()
        symbols += list(map(lmb_match, re.finditer(r"[^\.0-9]", line)))
        parts += list(map(lmb_match,re.finditer(r"[0-9]+", line)))

    return symbols, parts

def magnitude(p1,p2):
    d_vec = (p2[0]-p1[0], p2[1]-p1[1])
    return abs(d_vec[0]**2 + d_vec[1]**2)

def min_magnitude(part, symbol):
    return min(
        magnitude(p1,p2)
        for p1 in part[0]
        for p2 in symbol[0]
    )

def find_part_numbers(parts, symbols, limit = 2):
    return [
        int(p[1])
        for p in parts
        for s in symbols
        if min_magnitude(p,s) <= limit
    ]

def find_gear_ratios(parts, symbols, limit = 2, target_symbol="*"):
    ratios = []
    for gear in symbols: 
        if gear[1] == target_symbol:
            pg = [int(part[1]) for part in parts if min_magnitude(gear,part) <= limit]
            if len(pg)>1:
                ratios.append(math.prod(pg))
    return ratios
 
class Day3Part1(Solution):
    def solve(self, data, is_sample):
        symbols,parts = find_points(data)
        part_numbers = find_part_numbers(parts, symbols)
        return sum(part_numbers)
    
add_solution(3, 1, Day3Part1())

class Day3Part2(Solution):
    def solve(self, data, is_sample):
        symbols,parts = find_points(data)
        ratios = list(find_gear_ratios(parts, symbols))
        return sum(ratios)

add_solution(3, 2, Day3Part2())

from .solution import Solution, add_solution
import re

# only need the tens place
numbers_map = {
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four" : '4',
    "five" : '5',
    "six" : '6',
    "seven" : '7',
    "eight" : '8',
    "nine" : '9',
    "ten" : '0',
    "eleven" : '1',
    "twelve" : '2',
    "thirteen" : '3',
    "fourteen" : '4',
    "fifteen" : '5',
    "sixteen" : '6',
    "seventeen" : '7',
    "eighteen" : '8',
    "nineteen" : '9',
    "twenty" : '0',
    "thirty" : '0',
    "forty" : '0',
    "fifty" : '0',
    "sixty" : '0',
    "seventy" : '0',
    "eighty" : '0',
    "ninety" : '0',
    "hundred" : '0',
    "thousand" : '0',
    "million" : '0',
    "billion" : '0',
    "trillion" : '0',
}

class Day1Part1(Solution):
    def solve(self, data):
        val = 0
        for d in data:
            res = re.findall(r"[0-9]",d)
            val += int(res[0]+res[-1])

        return val
    
add_solution(1, 1, Day1Part1())

class Day1Part2(Solution):    

    def solve(self, data):
        # This on finds the beginning of the span
        x1 = re.compile(f"[0-9]|(?={'|'.join(numbers_map.keys())})")
        
        # This one matches the whole word
        x2 = re.compile(f"[0-9]|({'|'.join(numbers_map.keys())})")

        val = 0
        for ix, d in enumerate(data):
            found = list(x1.finditer(d))
            f = x2.match(d,found[0].span()[0]).group()
            l = x2.match(d,found[-1].span()[0]).group()

            mf = numbers_map.get(f,f)
            me = numbers_map.get(l,l)

            n = int(mf+me)
            val += n
        return val
            

add_solution(1, 2, Day1Part2())

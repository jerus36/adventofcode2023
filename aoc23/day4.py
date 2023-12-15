from .solution import Solution, add_solution
def calc_score(n):
    if n == 0:
        return 0
    ret = 1
    for i in range(n-1):
        ret += 2**i
    return ret

def parse_line(line):
    line = line.strip()
    label, v1 = line.split(":")
    winners, guesses = v1.split("|")
    winners = set([int(w) for w in winners.strip().split()])
    guesses = set([int(g) for g in guesses.strip().split()])
    return int(label.split()[1]), len(winners.intersection(guesses)), winners, guesses
    
class Day4Part1(Solution):
    def solve(self, data, is_sample):
        cards = [parse_line(c) for c in data]
        scores = []
        for card in cards:
            f = calc_score(card[1])
            scores.append(f)

        return sum(scores)
    
add_solution(4, 1, Day4Part1())

class Dasy4Part2(Solution):
    def solve(self, data, is_sample):
        cards = [parse_line(c) for c in data]
        for ix, card in enumerate(cards):
            ci = card[0]-1
            nc = [cards[ci+r] for r in range(1,card[1]+1)]
            cards += nc
        return len(cards)

add_solution(4, 2, Dasy4Part2())

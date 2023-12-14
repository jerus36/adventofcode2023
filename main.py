from inquirer import prompt,List
from aoc23.solution import get_solutions
import aoc23.day1
import aoc23.day2
import aoc23.day3


def run_solution(key:tuple, sample:bool):
    day, part = key
    solution = get_solutions()[key]
    
    fname = f"input/d{day}p{part}.{'sample' if sample else 'full'}.txt"
    with open(fname) as f:
        data = f.readlines()

    print(f"Day: {day}, Part: {part}")
    print(f"Solution: {solution.solve(data,sample)}")

def main():
    questions = [List(
        "solution",
        message="Select a solution",
        choices=[(f"Day: {day}, Part: {part}", (day,part)) for day, part in get_solutions().keys()],
    ),
    List("sample", message="Select dataset to use?",choices=["Sample","Full"],default="Sample")
    ]

    answers = prompt(questions)
    run_solution(answers["solution"], answers["sample"]=="Sample")

if __name__ == "__main__":
    main()


from abc import ABC, abstractmethod

class Solution:
    @abstractmethod
    def solve(self, data):
        raise NotImplemented()
    
_solutions = {}

def add_solution(day:int, part:int, solution: Solution):
    global _solutions
    _solutions[(day, part)] = solution


def get_solution(day:int, part:int) -> Solution:
    global _solutions
    return _solutions[(day, part)]

def get_solutions() -> dict:
    global _solutions
    return _solutions

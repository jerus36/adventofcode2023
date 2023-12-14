from abc import ABC, abstractmethod

class Solution:
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)

    @abstractmethod
    def solve(self, data, is_sample, **kwargs):
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

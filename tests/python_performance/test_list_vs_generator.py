from python_assignment.python_performance.Exercice_1 import use_generator
from python_assignment.python_performance.Exercice_1 import use_list
from python_assignment.python_performance.time_decorator import time_it

N = 10 ** 7


def test_generator_vs_list():

    _, time_generator = time_it(use_generator)(N)

    _, time_list = time_it(use_list)(N)

    assert time_generator < time_list

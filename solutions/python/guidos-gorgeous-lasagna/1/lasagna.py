"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time required for a number of layers.

    :param number_of_layers: int - number of layers to prepare.
    :return: int - time (in minutes) taken to prepare that number of layers.
    """
    return 2 * number_of_layers


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the time spent on cooking so far.

    :param number_of_layers: int - number of layers that were prepared.
    :param elapsed_bake_time: int - baking time (in minutes) already elapsed.
    :return: int - time (in minutes) that has already elapsed, including preparation time.
    """
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)

"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME: int = 40
PREPERATION_TIME:int = 0
TIME_REQUIRED_PER_LAYER = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time




def preparation_time_in_minutes(number_of_layers):
    """Calculate the time needed to prep the whole lasagna.

    :param number_of_layers: int - the number of layers wanted in the lasagna.
    :return: int - time in minutes required to prep the lasagna.

    Function takes number of layers required for the whole lasagna and calculates the time required in minutes by        multiplying the amount of layers by 2, as two is the amount of minutes required for each layer of lasagna.  
    """
    return number_of_layers * TIME_REQUIRED_PER_LAYER




def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the time needed to prep the whole lasagna.

    :param number_of_layers: int - the number of layers wanted in the lasagna.
    :return: int - time in minutes required to prep the lasagna.

    Function takes number of layers required for the whole lasagna and calculates the time required in minutes by        multiplying the amount of layers by 2, as two is the amount of minutes required for each layer of lasagna.  
    """
    return (number_of_layers*TIME_REQUIRED_PER_LAYER) + elapsed_bake_time

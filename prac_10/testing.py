"""
CP1404 Practical - Testing with assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the given length.

    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run assert tests on functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # Test that Car initialises odometer and fuel correctly
    car = Car()
    assert car._odometer == 0

    car = Car(fuel=10)
    assert car.fuel == 10

    car = Car()
    assert car.fuel == 0


def phrase_to_sentence(phrase):
    """
    Format a phrase as a sentence with a capital and a final full stop.

    >>> phrase_to_sentence('hello')
    'Hello.'
    >>> phrase_to_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> phrase_to_sentence('This subject rocks')
    'This subject rocks.'
    """
    sentence = phrase.capitalize()
    if sentence[-1] != '.':
        sentence = f"{sentence}."
    return sentence


run_tests()
doctest.testmod()

from functools import wraps
from operator import itemgetter
from itertools import groupby, chain


VOWELS = set('aeiouy')


def is_vowel(letter):
    return letter.lower() in VOWELS


def negated(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return not func(*args, **kwargs)
    return wrapper


class SwapVowels(object):

    @staticmethod
    def in_procedural_style(string):
        array = list(string)

        i = 0
        j = len(array) - 1

        while i < j:

            if not is_vowel(array[i]):
                i += 1
                continue

            if not is_vowel(array[j]):
                j -= 1
                continue

            array[i], array[j] = array[j], array[i]

            i += 1
            j -= 1

        return ''.join(array)

    @staticmethod
    def in_functional_style(string):
        return ''.join(
            chain.from_iterable(
                map(
                    itemgetter(1),
                    filter(
                        itemgetter(0),
                        chain.from_iterable(
                            zip(
                                groupby(string, negated(is_vowel)),
                                groupby(reversed(string), is_vowel)
                            )
                        )
                    )
                )
            )
        )

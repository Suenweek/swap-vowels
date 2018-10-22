import pytest
from swap_vowels import SwapVowels


@pytest.mark.parametrize(['str_in', 'str_out'], [
    ('', ''),                        # Empty
    ('phd', 'phd'),                  # No vowels
    ('aio', 'oia'),                  # No consonants
    ('y', 'y'),                      # One vowels
    ('x', 'x'),                      # One consonant
    ('linux', 'lunix'),              # Odd length
    ('manjaro', 'monjara'),          # Even length
    ('kilimanjaro', 'kolamanjiri'),  # Multi-syllable
    ('Achilles', 'echillAs')         # Upper case
])
@pytest.mark.parametrize('swap_vowels', [
    SwapVowels.in_procedural_style,
    SwapVowels.in_iterative_style,
    SwapVowels.in_purely_functional_style
])
def test_swap_vowels(swap_vowels, str_in, str_out):
    assert str_out == swap_vowels(str_in)

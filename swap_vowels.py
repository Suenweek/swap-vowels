VOWELS = set('aeiouy')


def vowel(letter):
    return letter.lower() in VOWELS


class SwapVowels(object):

    @staticmethod
    def in_procedural_style(string):
        array = list(string)

        i = 0
        j = len(array) - 1

        while i < j:

            if not vowel(array[i]):
                i += 1
                continue

            if not vowel(array[j]):
                j -= 1
                continue

            array[i], array[j] = array[j], array[i]

            i += 1
            j -= 1

        return ''.join(array)

    @staticmethod
    def in_iterative_style(string):
        reversed_vowels = filter(vowel, reversed(string))
        return ''.join(
            next(reversed_vowels) if vowel(letter) else letter
            for letter in string
        )

    @staticmethod
    def in_purely_functional_style(string):
        def join(cs, vs):
            if not cs:
                return vs

            if not vs:
                return cs

            if vowel(cs[0]):
                return vs[0] + join(cs[1:], vs[1:])

            return cs[0] + join(cs[1:], vs)

        return join(string, ''.join(filter(vowel, reversed(string))))

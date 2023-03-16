# Example of Using `itertools.permute()` and `filter()` to help at Scrabble
#
# In the game "Scrabble", you have a handful of letters available to you, and
# then you're allowed to use those letters to spell a word based-on an agreed
# dictionary of valid words.
#
import itertools


def word_is_valid(search_word: str, dictionary: list[str]) -> bool:
    word_found: bool = search_word in dictionary
    return word_found


def iterator_to_list_of_strings(iterator: list[tuple]) -> list[str]:
    return ["".join(map(str, tpl)) for tpl in iterator]


def get_all_substring_permutations(word: str, min_length: int = 2) -> list[str]:
    """Create a list of all Unique Permutations of the Substrings of the Word
    """
    all_permutations: list[str] = []
    num_letters = len(word)
    for substring_length in range(min_length, num_letters + 1, 1):
        permutation_substrings = iterator_to_list_of_strings(
            itertools.permutations(word, substring_length)
        )
        all_permutations.extend(permutation_substrings)
    return all_permutations


def propose_scrabble_suggestions(
    letters: list[str],
    dictionary: list[str],
    min_length: int = 2,
) -> list[str]:
    possible_words = get_all_substring_permutations("".join(letters), min_length)
    proposed_words = list(filter(lambda w: word_is_valid(w, dictionary), possible_words))
    return proposed_words


def propose_scrabble_suggestions_with_mixin(
    letters: list[str],
    mixin_letters: list[str],
    dictionary: list[str],
    min_length: int = 2,
) -> list[str]:
    possible_words = get_all_substring_permutations("".join(letters + mixin_letters), min_length)
    proposed_words = list(filter(lambda w: word_is_valid(w, dictionary), possible_words))
    return proposed_words


if __name__ == "__main__":
    dictionary = [
        "SISTRA",
        "SISTROID",
        "SISTRUM",
        "SISTRUMS",
        "SIT",
        "SITAR",
        "SITARIST",
        "SITARISTS",
        "SITARS",
        "SITCOM",
        "SITCOMS",
        "SITE",
        "SITED",
        "SITES",
        "SITH",
        "SITHENCE",
        "SITHENS",
        "SITING",
        "SITOLOGIES",
    ]

    scrabble_letters: list[str] = ["S", "T", "D", "H", "I", "E", "R", "C"]
    proposed_words: list[str] = propose_scrabble_suggestions(scrabble_letters, dictionary, min_length=2)
    print(f"> Letters: {scrabble_letters}")
    print(f"> Valid Words ({len(proposed_words)}): {proposed_words}")
    print()

    scrabble_letters: list[str] = ["S", "T", "D", "H", "I", "E", "R", "C"]
    mixin_letters: list[str] = ["A", "O"]
    proposed_words: list[str] = propose_scrabble_suggestions_with_mixin(
        scrabble_letters,
        mixin_letters,
        dictionary,
        min_length=2,
    )
    print(f"> Letters: {scrabble_letters} | Mixin Letters: {mixin_letters}")
    print(f"> Valid Words ({len(proposed_words)}): {proposed_words}")
    print()

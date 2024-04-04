import difflib
from splatink import matcher

map_list = list(matcher.abbreviations.keys())


def find_close_matches(input_word, word_list, n=1, cutoff=0.6):
    return difflib.get_close_matches(input_word, word_list, n=n, cutoff=cutoff)


def check_close_maps(input_word):
    return find_close_matches(input_word, map_list)



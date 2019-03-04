#!/usr/bin/env python3

from itertools import permutations


def solve(solvable, available_chars, word_list_file):
    for letter in solvable:
        if letter != "_": available_chars.remove(letter)
    possible_word_candidates = make_all_possible_word_candidates(available_chars, solvable)
    return check_possible_word_candidates_against_dictionary(possible_word_candidates, word_list_file)


def get_input():
    return input("Enter word to solve, using '_' or '-' for blanks (e.g. __Y_L): ").lower().replace("-","_"),\
           sorted(input("Enter all the available letters, including ones already placed in the solvable (order does not matter) (e.g. LYSOLID): ").lower())


def make_all_combos_from_available_chars(available_chars, blanks):
    return set(permutations(available_chars, len(blanks)))


def make_all_possible_word_candidates(available_chars, solvable):
    possible_word_candidates = []
    blanks = [char for char in range(len(solvable)) if solvable[char] == "_"]
    for combo in make_all_combos_from_available_chars(available_chars, blanks):
        possible_word_candidate = list(solvable)
        for index in range(len(combo)):
            possible_word_candidate[blanks[index]] = combo[index]
        possible_word_candidates.append("".join(possible_word_candidate))
    return possible_word_candidates


def check_possible_word_candidates_against_dictionary(possible_word_candidates, word_list_file):
    # Word lists: https://github.com/dwyl/english-words
    with open(word_list_file) as dict_file:
        word_list = [word.strip().lower() for word in dict_file.readlines()]
    possible_words = []
    for possible_word in possible_word_candidates:
        if possible_word in word_list:
            possible_words.append(possible_word.upper())
    return possible_words


if __name__ == "__main__":
    input_solvable, input_available_chars = get_input()
    for possible_word in solve(input_solvable, input_available_chars, word_list_file="words.txt"):
        print(possible_word)

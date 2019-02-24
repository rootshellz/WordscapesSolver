#!/usr/bin/env python3

from itertools import permutations


def get_input():
    return input("Enter word to solve, using '_' or '-' for blanks (e.g. __Y_L): ").lower().replace("-","_"), sorted(input("Enter all the available letters, including ones already placed in the solvable (order does not matter) (e.g. LYSOLID): ").lower())


def make_all_combos_from_availables():
    return set(permutations(availables, len(blanks)))


def make_all_possible_word_candidates():
    possible_word_candidates = []
    for combo in make_all_combos_from_availables():
        possible_word_candidate = list(solvable)
        for index in range(len(combo)):
            possible_word_candidate[blanks[index]] = combo[index]
        possible_word_candidates.append("".join(possible_word_candidate))
    return possible_word_candidates


def check_possible_word_candidates_against_dictionary():
    # Word lists: https://github.com/dwyl/english-words 
    with open("words_alpha.txt") as dict_file:
        word_list = [word.strip().lower() for word in dict_file.readlines()]
    possible_words = []
    for possible_word in possible_word_candidates:
        if possible_word in word_list:
            possible_words.append(possible_word.upper())
    return possible_words


solvable, availables = get_input()

for letter in solvable:
    if letter != "_": availables.remove(letter)

blanks = [char for char in range(len(solvable)) if solvable[char] == "_"]

all_available_combos = make_all_combos_from_availables()
possible_word_candidates = make_all_possible_word_candidates()
for possible_word in check_possible_word_candidates_against_dictionary():
    print(possible_word)

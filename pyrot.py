#!/usr/bin/env python3

import argparse
import itertools
from colorama import Fore, Back, Style

script_name = "Pyrot"
script_vers = "0.0.1a"

chars = "abcdefghijklmnopqrstuvwxyz"

def perform_rot(input: str, shift: int) -> str:
    newchars = chars[shift:] + chars[:shift]
    trans = str.maketrans(chars + chars.upper(), newchars + newchars.upper())
    return input.translate(trans)

def is_in_dictionary(input: str, dict_filename: str) -> bool:
    with open(dict_filename, "r") as dict:
        input_tokens = input.split()
        dict_entries = [line.strip() for line in dict]

        for entry, token in itertools.product(dict_entries, input_tokens):
            if(token.lower().find(entry.lower()) != -1):
                return True

    return False

def main():
    dictionary_filename = "top100_eng.dict"

    # Arguments processing
    argparser = argparse.ArgumentParser(
        prog=f"{script_name}",
        description="A simple script to bruteforce ROT-encoded messages"
    )

    input_group = argparser.add_mutually_exclusive_group()
    input_group.add_argument('-f', '--file', help='File to read encoded message from')
    input_group.add_argument('-s', '--string', help='An encoded string to bruteforce')
    argparser.add_argument('-v', '--verbose', help='Display more information', action='store_true')
    argparser.add_argument('-d', '--dictionary', help="Use custom dictionary")
    argparser.add_argument('--version', action='version', version=f'{script_name} {script_vers}')
    args = vars(argparser.parse_args())

    # Obtain the input string based on arguments
    encoded_string = ""

    if(args['file'] is None and args['string'] is None):
        # Read from standard input
        encoded_string = input("Encoded string: ")
    elif(args['string'] is not None):
        # Read string from argument -s
        encoded_string = args['string']
        print(f"Encoded string: {encoded_string}")
    else:
        # Open the input file and read the string from there
        with open(args['file'], 'r') as input_file:
            encoded_string = input_file.read().strip('\n')
            print(f"Encoded string: {encoded_string}")

    if(args['dictionary'] is not None):
        dictionary_filename = args['dictionary']

    solutions = []

    for rotations in range(2, 26):
        decoded_string = perform_rot(encoded_string, rotations)

        if (is_in_dictionary(decoded_string, dictionary_filename)):
            # The string is in the dictionary, highlight it
            if(args['verbose']):
                print(f"ROT{rotations:02d}: {Fore.RED}{decoded_string}{Style.RESET_ALL}")
            solutions.append(rotations)
        elif args['verbose']:
            print(f"ROT{rotations:02d}: {Style.DIM}{decoded_string}{Style.RESET_ALL}")

    if(solutions):
        print("\nFound the following solutions: ")
        for solution in solutions:
            print(f"[+] {Style.BRIGHT}ROT{solution}{Style.RESET_ALL} = {Fore.RED}{perform_rot(encoded_string, solution)}{Style.RESET_ALL}")
    else:
        if(args['verbose'] is True):
            print("\n[-] No solutions found (perhaps try another dictionary?)")
        else:
            print("\n[-] No solutions found (perhaps try with -v?)")

if __name__ == '__main__':
    main()
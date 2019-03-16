#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Wordlist generator made easy for cracking"""

import sys


def get_parser():
    """Get parser object for script wordgen.py."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, FileType
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("wordlist",
                        type=FileType('r'),
                        default=sys.stdin,
                        metavar="wordlist",
                        help="wordlist to scramble")
    parser.add_argument("-o", "--output",
                        action="store",
                        type=FileType('w'),
                        default=sys.stdout,
                        dest="outputfile",
                        metavar="file",
                        help="write output to file")
    parser.add_argument("-s", "--seperator",
                        metavar="",
                        help="the seperator of words on each line")
    parser.add_argument("-l", "--leet",
                        metavar="",
                        default=False,
                        help="create l33tsp34k words")

    return parser


def add_characters(words):
    special_characters = ["!", "?", "."]
    wordlist = list()
    for word in words:
        for char in special_characters:
            wordlist.append(word + char)
    return wordlist


def add_numbers(words):
    common_numbers = ["123", "12345", "666", "789", "890", "69", "2019"]
    wordlist = list()
    for word in words:
        for number in common_numbers:
            wordlist.append(word + number)
    return wordlist


def initialize(args):
    wordlist = list()
    for line in args.wordlist:
        line = line.strip("\r").strip("\n")
        wordlist.append(line.lower())
        wordlist.append(line.capitalize())
    set(wordlist)
    return wordlist


if __name__ == "__main__":
    args = get_parser().parse_args()
    wordlist = initialize(args)
    wordlist = add_characters(wordlist)
    wordlist = add_numbers(wordlist)
    print(wordlist)

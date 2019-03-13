#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Wordlist generator made easy for cracking"""

import sys
import os

def is_valid_file(parser, arg):
    """
    Check if arg is a valid file that already exists on the file system.

    Parameters
    ----------
    parser : argparse object
    arg : str

    Returns
    -------
    arg
    """
    arg = os.path.abspath(arg)
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg

def get_parser():
    """Get parser object for script xy.py."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", "--file",
                        dest="filename",
                        type=lambda x: is_valid_file(parser, x),
                        help="write report to FILE",
                        metavar="FILE")
    parser.add_argument("-n",
                        dest="n",
                        default=10,
                        type=int,
                        help="how many lines get printed")
    parser.add_argument("-q", "--quiet",
                        action="store_false",
                        dest="verbose",
                        default=True,
                        help="don't print status messages to stdout")
    return parser

    """
    parser = argparse.ArgumentParser(description="Custom wordlist generator for cracking attempts")
    parser.add_argument('wordlist', type=argparse.FileType('r'), default=sys.stdin, dest='inputfile', metavar="FILE", help="wordlist to use")
    parser.add_argument("-v", '--verbosity', help="increase output verbosity")
    parser.add_argument("-o", '--output', action='store', type=argparse.FileType('w'), default=sys.stdout, dest='outputfile', metavar="FILE", help="write to file")
    parser.add_argument("-u", '--users', help="create usernames")
    parser.add_argument("-p", '--passwords', help="create passwords")
    parser.add_argument("-l", '--leet', help="create l33tsp34k words")
    """


if __name__ == '__main__':
    args = get_parser().parse_args()

import random
import sys

SAFE_WORDS = ['BLEEP', 'REDACTED', 'XXXXXXX']


def bleep_line(line, replacement):
    First, implement the function bleep_line(line, replacement),
    which takes in a string line and a string replacement and
    returns the line with any bad words replaced with whatever
    the replacement string is. We identify bad words using square
    brackets - [[bad word]] - and the string line will contain
    one or zero instances of bad words.
    >>> bleep_line('What the [[heck]] Richard??', 'BLEEP')
    'What the BLEEP Richard??'
    >>> bleep_line('They call him [[Lord Voldemort]]', 'He Who Must Not Be Named')
    'They call him He Who Must Not Be Named'
    >>> bleep_line('I do not need to swear to express my emotions', 'BLEEP')
    'I do not need to swear to express my emotions'
    left = line.find('[[')
    if left != -1:
        right = line.find(']]')
        line = line[:left] + replacement + line[right + 2:]
    return line


def file_bleeping(filename):
    Now, we're going to write a function called file_bleeping(filename)
    that takes in the name of a text file filename, and prints the
    contents of the file with each line bleeped out. Just like in the
    previous part of this project, you can assume that each line only
    contains a single item to be bleeped out, or none at all.

    Hint, hint: use your helper function from the previous part to
    implement this function!
    with open(filename) as f:
        for line in f:
            line = line.strip() # without this, the space between printed lines would be extra large
            replacement = random.choice(SAFE_WORDS)
            line_bleeped = bleep_line(line, replacement)
            print(line_bleeped)



if __name__ == "__main__":
    args = sys.argv[1:]
    file_bleeping(args[0])

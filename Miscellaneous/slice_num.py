import sys


def slice_num(s):
    """
    In this problem, you'll write a function slice_num(s)
    that takes in a string s and returns the integer contained
    in that string. If the string contains an integer, it will
    be between two hashtags. If there are no hashtags, you can
    return 0.
    >>> slice_num('My favorite number is #2#!')
    2
    >>> slice_num('Blahblah#12345#blah')
    12345

    Write your own Doctests here!
    """
    left = s.find('#')
    if left == -1:
        return 0
    right = s.find('#', left + 1)
    result = int(s[left + 1:right])
    return result




def sum_nums(s1, s2):
    """
    Implement the function sum_nums(s1, s2) that takes in two strings
    and returns the sum of the integers in those strings. As in
    slice_num(s), any integers in these strings will be between two
    hashtags, and each string will have at most one integer, or none.
    Calculate the sum, then return it. Hint: this would be a great place
    to use the helper function you just wrote!

    >>> sum_nums('#1#', 'plus #2# equals')
    3
    >>> sum_nums('abc#123#xyz', 'no nums here!')
    123
    >>> sum_nums('', '')
    0
    """
    return slice_num(s1) + slice_num(s2)


if __name__ == "__main__":
    sum_nums('My favorite number is #2#', 'Well, I prefer #5# instead.')
    print('Should have printed: 7')

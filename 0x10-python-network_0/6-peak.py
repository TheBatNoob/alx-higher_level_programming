#!/usr/bin/python3
""" Finds a peak inside a list """


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None

    return max(list_of_integers)


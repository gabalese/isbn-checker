# coding=utf-8
import re


def is_valid(isbn):
    digits_sum = 0
    isbn = re.sub(r"[-–—\s]", "", isbn)
    # in case of isbn13
    if len(isbn) == 13 and isbn[0:3] == "978" or "979":  # is it a ISBN? Thanks @librarythingtim
        for d, i in enumerate(isbn):
            try:
                if (int(d) + 1) % 2 != 0:
                    digits_sum += int(i)
                else:
                    digits_sum += int(i) * 3
            except ValueError:
                return False
        if digits_sum % 10 == 0:
            return True
        else:
            return False
    # in case of isbn10
    elif len(isbn) == 10:
        isbn = list(isbn)
        if isbn[-1] == "X" or isbn[-1] == "x":  # a final x stands for 10
            isbn[-1] = 10
        for d, i in enumerate(isbn[:-1]):
            digits_sum += (int(d) + 1) * int(i)
        if (digits_sum % 11) == int(isbn[-1]):
            return True
        else:
            return False
    else:
        return False

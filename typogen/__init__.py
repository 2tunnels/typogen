import re


def skip_letter(text):
    """Skip letter in text.

    Examples:
    >>> skip_letter('cat')
    {'ca', 'ct', 'at'}
    >>> skip_letter('frog')
    {'rog', 'fro', 'fog', 'frg'}

    :type text: str
    :rtype: set
    """

    text = _clean_text(text)

    typos = []

    for i in range(len(text)):
        if text[i].isspace():
            continue

        typo = '{head}{tail}'.format(
            head=text[0:i],
            tail=text[i + 1:]
        )

        typos.append(typo)

    return set(typos)


def double_letter(text):
    """Double letter in text.

    Examples:
    >>> double_letter('cat')
    {'ccat', 'caat', 'catt'}
    >>> double_letter('frog')
    {'frogg', 'ffrog', 'frrog', 'froog'}

    :type text: str
    :rtype: set
    """

    text = _clean_text(text)

    typos = []

    for i in range(len(text)):
        if text[i].isspace():
            continue

        typo = '{head}{letter}{tail}'.format(
            head=text[0:i + 1],
            letter=text[i],
            tail=text[i + 1:]
        )

        typos.append(typo)

    return set(typos)


def reverse_letters(text):
    """Reverse letters in text.

    Examples:
    >>> reverse_letters('cat')
    {'cta', 'act'}
    >>> reverse_letters('frog')
    {'rfog', 'forg', 'frgo'}

    :type text: str
    :rtype: set
    """

    text = _clean_text(text)

    typos = []

    for i in range(len(text) - 1):
        first_letter = text[i]
        second_letter = text[i + 1]

        # do not reverse if the same letter
        if first_letter == second_letter:
            continue

        typo = '{head}{second}{first}{tail}'.format(
            head=text[0:i],
            second=second_letter,
            first=first_letter,
            tail=text[i + 2:]
        )

        typos.append(typo)

    return set(typos)


def skip_spaces(text):
    """Skip spaces in text.

    Examples:
    >>> skip_spaces('blue invisible unicorn')
    {'blueinvisible unicorn', 'blue invisibleunicorn'}

    :type text: str
    :rtype: set
    """

    text = _clean_text(text)

    typos = []

    start = 0

    while True:
        try:
            index = text.index(' ', start)
        except ValueError:
            break

        typo = '{head}{tail}'.format(
            head=text[0:index],
            tail=text[index + 1:]
        )

        typos.append(typo)

        start = index + 1

    return set(typos)


def nearest_keys(key):
    """Returns nearest keys to provided one.

    :type key: str
    :rtype: list
    """

    key = str(key)
    normalized_key = key.lower()

    try:
        keys = _nearest_keys[normalized_key]
    except KeyError:
        return key

    if key.isupper():
        return [k.upper() for k in keys]

    return keys


def missed_key(text):
    """Misses needed key as if was pushed nearest ones.

    :type text: str
    :rtype: set
    """

    text = _clean_text(text)

    typos = []

    for i in range(len(text)):
        if text[i].isspace():
            continue

        for key in nearest_keys(text[i]):
            typos.append(text[0:i] + key + text[i + 1:])

    return set(typos)


def inserted_key(text):
    """Inserts nearest keys before and after needed one.

    :type text: str
    :rtype: set
    """

    text = _clean_text(text)

    typos = []

    for i in range(len(text)):
        if text[i].isspace():
            continue

        for key in nearest_keys(text[i]):
            typos.append(text[0:i] + key + text[i] + text[i + 1:])
            typos.append(text[0:i] + text[i] + key + text[i + 1:])

    return set(typos)


# http://tools.seobook.com/spelling/keywords-typos.cgi
_nearest_keys = {
    '1': ['2', 'q'],
    '2': ['3', 'w', 'q', '1'],
    '3': ['4', 'e', 'w', '2'],
    '4': ['5', 'r', 'e', '3'],
    '5': ['6', 't', 'r', '4'],
    '6': ['7', 'y', 't', '5'],
    '7': ['8', 'u', 'y', '6'],
    '8': ['9', 'i', 'u', '7'],
    '9': ['0', 'o', 'i', '8'],
    '0': ['p', 'o', '9'],
    'q': ['1', '2', 'w', 's', 'a'],
    'w': ['q', '2', '3', 'e', 'd', 's', 'a'],
    'e': ['w', '3', '4', 'r', 'f', 'd', 's'],
    'r': ['e', '4', '5', 't', 'g', 'f', 'd'],
    't': ['r', '5', '6', 'y', 'h', 'g', 'f'],
    'y': ['t', '6', '7', 'u', 'j', 'h', 'g'],
    'u': ['y', '7', '8', 'i', 'k', 'j', 'h'],
    'i': ['u', '8', '9', 'o', 'l', 'k', 'j'],
    'o': ['i', '9', '0', 'p', 'l', 'k'],
    'p': ['o', '0', 'l'],
    'a': ['q', 'w', 's', 'x', 'z'],
    's': ['a', 'w', 'e', 'd', 'x', 'z'],
    'd': ['s', 'e', 'r', 'f', 'c', 'x'],
    'f': ['d', 'r', 't', 'g', 'v', 'c'],
    'g': ['f', 't', 'y', 'h', 'b', 'v'],
    'h': ['g', 'y', 'u', 'j', 'n', 'b'],
    'j': ['h', 'u', 'i', 'k', 'm', 'n'],
    'k': ['j', 'i', 'o', 'l', 'm'],
    'l': ['k', 'o', 'p'],
    'z': ['a', 's', 'x'],
    'x': ['z', 's', 'd', 'c'],
    'c': ['x', 'd', 'f', 'v'],
    'v': ['c', 'f', 'g', 'b'],
    'b': ['v', 'g', 'h', 'n'],
    'n': ['b', 'h', 'j', 'm'],
    'm': ['n', 'j', 'k'],
}


def _clean_text(text):
    """Strips text and removes duplicate spaces from it.

    :type text: str
    :rtype: str
    """

    text = text.strip()
    text = re.sub(r'\s+', ' ', text)

    return text

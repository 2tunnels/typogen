import re


def skip_letter(keyword):
    keyword = keyword.strip()
    keyword = re.sub(r'\s+', ' ', keyword)

    typos = []

    for i in range(len(keyword)):
        if keyword[i].isspace():
            continue

        typos.append(keyword[0:i] + keyword[i + 1:])

    return set(typos)


def double_letters(keyword):
    keyword = keyword.strip()
    keyword = re.sub(r'\s+', ' ', keyword)

    typos = []

    for i in range(len(keyword)):
        if keyword[i].isspace():
            continue

        typos.append(keyword[0:i + 1] + keyword[i] + keyword[i + 1:])

    return set(typos)


def reverse_letters(keyword):
    keyword = keyword.strip()
    keyword = re.sub(r'\s+', ' ', keyword)

    typos = []

    for i in range(len(keyword) - 1):
        # do not reverse if the same letter
        if keyword[i] == keyword[i + 1]:
            continue

        typos.append(keyword[0:i] + keyword[i + 1] + keyword[i] + keyword[i + 2:])

    return set(typos)


def skip_spaces(keyword):
    keyword = keyword.strip()
    keyword = re.sub(r'\s+', ' ', keyword)

    typos = []

    start = 0

    while True:
        try:
            index = keyword.index(' ', start)
        except ValueError:
            break

        typos.append(keyword[0:index] + keyword[index + 1:])

        start = index + 1

    return set(typos)


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


def nearest_keys(key):
    key = str(key)
    normalized_key = key.lower()

    try:
        keys = _nearest_keys[normalized_key]
    except KeyError:
        return key

    if key.isupper():
        return [k.upper() for k in keys]

    return keys

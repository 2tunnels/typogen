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
    seen = [keyword]

    for i in range(len(keyword) - 1):
        typo = keyword[0:i] + keyword[i + 1] + keyword[i] + keyword[i + 2:]

        if typo not in seen:
            seen.append(typo)
            yield typo


def skip_spaces(keyword: str):
    keyword = keyword.strip()
    keyword = re.sub(r'\s+', ' ', keyword)

    start = 0

    while True:
        try:
            index = keyword.index(' ', start)
        except ValueError:
            break

        yield keyword[0:index] + keyword[index + 1:]

        start = index + 1

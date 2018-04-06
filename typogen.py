def skip_letter(keyword):
    seen = []

    for i in range(len(keyword)):
        typo = keyword[0:i] + keyword[i + 1:]

        if typo not in seen:
            seen.append(typo)
            yield typo


def double_letters(keyword):
    seen = []

    for i in range(len(keyword)):
        typo = keyword[0:i + 1] + keyword[i] + keyword[i + 1:]

        if typo not in seen:
            seen.append(typo)
            yield typo

import typogen


def test_skip_letter():
    assert list(typogen.skip_letter('cat')) == ['at', 'ct', 'ca']
    assert list(typogen.skip_letter('frog')) == ['rog', 'fog', 'frg', 'fro']


def test_skip_letter_double():
    assert list(typogen.skip_letter('bull')) == ['ull', 'bll', 'bul']


def test_skip_letter_not_stripped():
    assert list(typogen.skip_letter(' cat ')) == ['at', 'ct', 'ca']
    assert list(typogen.skip_letter(' frog ')) == ['rog', 'fog', 'frg', 'fro']
    assert list(typogen.skip_letter(' bull ')) == ['ull', 'bll', 'bul']


def test_double_letters():
    assert list(typogen.double_letters('cat')) == ['ccat', 'caat', 'catt']
    assert list(typogen.double_letters('frog')) == ['ffrog', 'frrog', 'froog', 'frogg']


def test_double_letters_double():
    assert list(typogen.double_letters('bull')) == ['bbull', 'buull', 'bulll']


def test_reverse_letters():
    assert list(typogen.reverse_letters('cat')) == ['act', 'cta']
    assert list(typogen.reverse_letters('frog')) == ['rfog', 'forg', 'frgo']


def test_reverse_letters_double():
    assert list(typogen.reverse_letters('bull')) == ['ubll', 'blul']


def test_skip_spaces():
    assert list(typogen.skip_spaces('blue invisible unicorn')) == [
        'blueinvisible unicorn',
        'blue invisibleunicorn',
    ]


def test_skip_spaces_not_stripped():
    assert list(typogen.skip_spaces(' blue invisible unicorn ')) == [
        'blueinvisible unicorn',
        'blue invisibleunicorn',
    ]


def test_skip_spaces_multiple_spaces():
    assert list(typogen.skip_spaces('blue   invisible   unicorn')) == [
        'blueinvisible unicorn',
        'blue invisibleunicorn',
    ]


def test_skip_spaces_no_spaces():
    assert list(typogen.skip_spaces('cat')) == []

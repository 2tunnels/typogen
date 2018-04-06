import typogen


def test_skip_letter():
    assert list(typogen.skip_letter('cat')) == ['at', 'ct', 'ca']
    assert list(typogen.skip_letter('frog')) == ['rog', 'fog', 'frg', 'fro']


def test_skip_letter_double():
    assert list(typogen.skip_letter('bull')) == ['ull', 'bll', 'bul']


def test_double_letters():
    assert list(typogen.double_letters('cat')) == ['ccat', 'caat', 'catt']
    assert list(typogen.double_letters('frog')) == ['ffrog', 'frrog', 'froog', 'frogg']


def test_double_letters_double():
    assert list(typogen.double_letters('bull')) == ['bbull', 'buull', 'bulll']

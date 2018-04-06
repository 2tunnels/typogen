import typogen


class TestSkipLetter:
    def test_simple(self):
        assert typogen.skip_letter('cat') == {'at', 'ct', 'ca'}
        assert typogen.skip_letter('frog') == {'rog', 'fog', 'frg', 'fro'}

    def test_double(self):
        assert typogen.skip_letter('bull') == {'ull', 'bll', 'bul'}

    def test_with_space(self):
        assert typogen.skip_letter('cat frog') == {
            'at frog',
            'ct frog',
            'ca frog',
            'cat rog',
            'cat fog',
            'cat frg',
            'cat fro',
        }

    def test_empty(self):
        assert typogen.skip_letter('') == set()

    def test_multiple_spaces(self):
        assert typogen.skip_letter('   cat   ') == {'at', 'ct', 'ca'}
        assert typogen.skip_letter('   frog   ') == {'rog', 'fog', 'frg', 'fro'}
        assert typogen.skip_letter('   bull   ') == {'ull', 'bll', 'bul'}
        assert typogen.skip_letter('   cat   frog   ') == {
            'at frog',
            'ct frog',
            'ca frog',
            'cat rog',
            'cat fog',
            'cat frg',
            'cat fro',
        }
        assert typogen.skip_letter('   ') == set()


class TestDoubleLetters:
    def test_simple(self):
        assert typogen.double_letters('cat') == {'ccat', 'caat', 'catt'}
        assert typogen.double_letters('frog') == {'ffrog', 'frrog', 'froog', 'frogg'}

    def test_double(self):
        assert typogen.double_letters('bull') == {'bbull', 'buull', 'bulll'}

    def test_with_space(self):
        assert typogen.double_letters('cat frog') == {
            'ccat frog',
            'caat frog',
            'catt frog',
            'cat ffrog',
            'cat frrog',
            'cat froog',
            'cat frogg',
        }

    def test_empty(self):
        assert typogen.double_letters('') == set()

    def test_multiple_spaces(self):
        assert typogen.double_letters('   cat   ') == {'ccat', 'caat', 'catt'}
        assert typogen.double_letters('   frog   ') == {'ffrog', 'frrog', 'froog', 'frogg'}
        assert typogen.double_letters('   bull   ') == {'bbull', 'buull', 'bulll'}
        assert typogen.double_letters('   cat   frog   ') == {
            'ccat frog',
            'caat frog',
            'catt frog',
            'cat ffrog',
            'cat frrog',
            'cat froog',
            'cat frogg',
        }
        assert typogen.double_letters('   ') == set()


class TestReverseLetters:
    def test_simple(self):
        assert typogen.reverse_letters('cat') == {'act', 'cta'}
        assert typogen.reverse_letters('frog') == {'rfog', 'forg', 'frgo'}

    def test_double(self):
        assert typogen.reverse_letters('bull') == {'ubll', 'blul'}

    def test_with_space(self):
        assert typogen.reverse_letters('cat frog') == {
            'act frog',
            'cta frog',
            'ca tfrog',
            'catf rog',
            'cat rfog',
            'cat forg',
            'cat frgo',
        }

    def test_empty(self):
        assert typogen.reverse_letters('') == set()

    def test_multiple_spaces(self):
        assert typogen.reverse_letters('   cat   ') == {'act', 'cta'}
        assert typogen.reverse_letters('   frog   ') == {'rfog', 'forg', 'frgo'}
        assert typogen.reverse_letters('   bull   ') == {'ubll', 'blul'}
        assert typogen.reverse_letters('   cat   frog   ') == {
            'act frog',
            'cta frog',
            'ca tfrog',
            'catf rog',
            'cat rfog',
            'cat forg',
            'cat frgo',
        }
        assert typogen.reverse_letters('   ') == set()


class TestSkipSpaces:
    def test_simple(self):
        assert typogen.skip_spaces('blue invisible unicorn') == {
            'blueinvisible unicorn',
            'blue invisibleunicorn',
        }

    def test_no_spaces(self):
        assert typogen.skip_spaces('cat') == set()

    def test_empty(self):
        assert typogen.skip_spaces('') == set()

    def test_multiple_spaces(self):
        assert typogen.skip_spaces('   blue   invisible   unicorn   ') == {
            'blueinvisible unicorn',
            'blue invisibleunicorn',
        }
        assert typogen.skip_spaces('   cat   ') == set()
        assert typogen.skip_spaces('   ') == set()

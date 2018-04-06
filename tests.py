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
        assert typogen.skip_letter('   frog   ') == {
            'rog',
            'fog',
            'frg',
            'fro',
        }
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
        assert typogen.double_letter('cat') == {'ccat', 'caat', 'catt'}
        assert typogen.double_letter('frog') == {
            'ffrog',
            'frrog',
            'froog',
            'frogg',
        }

    def test_double(self):
        assert typogen.double_letter('bull') == {'bbull', 'buull', 'bulll'}

    def test_with_space(self):
        assert typogen.double_letter('cat frog') == {
            'ccat frog',
            'caat frog',
            'catt frog',
            'cat ffrog',
            'cat frrog',
            'cat froog',
            'cat frogg',
        }

    def test_empty(self):
        assert typogen.double_letter('') == set()

    def test_multiple_spaces(self):
        assert typogen.double_letter('   cat   ') == {'ccat', 'caat', 'catt'}
        assert typogen.double_letter('   frog   ') == {
            'ffrog',
            'frrog',
            'froog',
            'frogg',
        }
        assert typogen.double_letter('   bull   ') == {
            'bbull',
            'buull',
            'bulll',
        }
        assert typogen.double_letter('   cat   frog   ') == {
            'ccat frog',
            'caat frog',
            'catt frog',
            'cat ffrog',
            'cat frrog',
            'cat froog',
            'cat frogg',
        }
        assert typogen.double_letter('   ') == set()


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
        assert typogen.reverse_letters('   frog   ') == {
            'rfog',
            'forg',
            'frgo',
        }
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
        assert typogen.skip_spaces('cat frog') == {'catfrog'}
        assert typogen.skip_spaces('blue invisible unicorn') == {
            'blueinvisible unicorn',
            'blue invisibleunicorn',
        }

    def test_no_spaces(self):
        assert typogen.skip_spaces('cat') == set()

    def test_empty(self):
        assert typogen.skip_spaces('') == set()

    def test_multiple_spaces(self):
        assert typogen.skip_spaces('   cat   frog   ') == {'catfrog'}
        assert typogen.skip_spaces('   blue   invisible   unicorn   ') == {
            'blueinvisible unicorn',
            'blue invisibleunicorn',
        }
        assert typogen.skip_spaces('   cat   ') == set()
        assert typogen.skip_spaces('   ') == set()


class TestNearestKeys:
    def test_1(self):
        assert typogen.nearest_keys('1') == ['2', 'q']
        assert typogen.nearest_keys(1) == ['2', 'q']

    def test_2(self):
        assert typogen.nearest_keys('2') == ['3', 'w', 'q', '1']
        assert typogen.nearest_keys(2) == ['3', 'w', 'q', '1']

    def test_3(self):
        assert typogen.nearest_keys('3') == ['4', 'e', 'w', '2']
        assert typogen.nearest_keys(3) == ['4', 'e', 'w', '2']

    def test_4(self):
        assert typogen.nearest_keys('4') == ['5', 'r', 'e', '3']
        assert typogen.nearest_keys(4) == ['5', 'r', 'e', '3']

    def test_5(self):
        assert typogen.nearest_keys('5') == ['6', 't', 'r', '4']
        assert typogen.nearest_keys(5) == ['6', 't', 'r', '4']

    def test_6(self):
        assert typogen.nearest_keys('6') == ['7', 'y', 't', '5']
        assert typogen.nearest_keys(6) == ['7', 'y', 't', '5']

    def test_7(self):
        assert typogen.nearest_keys('7') == ['8', 'u', 'y', '6']
        assert typogen.nearest_keys(7) == ['8', 'u', 'y', '6']

    def test_8(self):
        assert typogen.nearest_keys('8') == ['9', 'i', 'u', '7']
        assert typogen.nearest_keys(8) == ['9', 'i', 'u', '7']

    def test_9(self):
        assert typogen.nearest_keys('9') == ['0', 'o', 'i', '8']
        assert typogen.nearest_keys(9) == ['0', 'o', 'i', '8']

    def test_0(self):
        assert typogen.nearest_keys('0') == ['p', 'o', '9']
        assert typogen.nearest_keys(0) == ['p', 'o', '9']

    def test_q(self):
        assert typogen.nearest_keys('q') == ['1', '2', 'w', 's', 'a']
        assert typogen.nearest_keys('Q') == ['1', '2', 'W', 'S', 'A']

    def test_w(self):
        assert typogen.nearest_keys('w') == ['q', '2', '3', 'e', 'd', 's', 'a']
        assert typogen.nearest_keys('W') == ['Q', '2', '3', 'E', 'D', 'S', 'A']

    def test_e(self):
        assert typogen.nearest_keys('e') == ['w', '3', '4', 'r', 'f', 'd', 's']
        assert typogen.nearest_keys('E') == ['W', '3', '4', 'R', 'F', 'D', 'S']

    def test_r(self):
        assert typogen.nearest_keys('r') == ['e', '4', '5', 't', 'g', 'f', 'd']
        assert typogen.nearest_keys('R') == ['E', '4', '5', 'T', 'G', 'F', 'D']

    def test_t(self):
        assert typogen.nearest_keys('t') == ['r', '5', '6', 'y', 'h', 'g', 'f']
        assert typogen.nearest_keys('T') == ['R', '5', '6', 'Y', 'H', 'G', 'F']

    def test_y(self):
        assert typogen.nearest_keys('y') == ['t', '6', '7', 'u', 'j', 'h', 'g']
        assert typogen.nearest_keys('Y') == ['T', '6', '7', 'U', 'J', 'H', 'G']

    def test_u(self):
        assert typogen.nearest_keys('u') == ['y', '7', '8', 'i', 'k', 'j', 'h']
        assert typogen.nearest_keys('U') == ['Y', '7', '8', 'I', 'K', 'J', 'H']

    def test_i(self):
        assert typogen.nearest_keys('i') == ['u', '8', '9', 'o', 'l', 'k', 'j']
        assert typogen.nearest_keys('I') == ['U', '8', '9', 'O', 'L', 'K', 'J']

    def test_o(self):
        assert typogen.nearest_keys('o') == ['i', '9', '0', 'p', 'l', 'k']
        assert typogen.nearest_keys('O') == ['I', '9', '0', 'P', 'L', 'K']

    def test_p(self):
        assert typogen.nearest_keys('p') == ['o', '0', 'l']
        assert typogen.nearest_keys('P') == ['O', '0', 'L']

    def test_a(self):
        assert typogen.nearest_keys('a') == ['q', 'w', 's', 'x', 'z']
        assert typogen.nearest_keys('A') == ['Q', 'W', 'S', 'X', 'Z']

    def test_s(self):
        assert typogen.nearest_keys('s') == ['a', 'w', 'e', 'd', 'x', 'z']
        assert typogen.nearest_keys('S') == ['A', 'W', 'E', 'D', 'X', 'Z']

    def test_d(self):
        assert typogen.nearest_keys('d') == ['s', 'e', 'r', 'f', 'c', 'x']
        assert typogen.nearest_keys('D') == ['S', 'E', 'R', 'F', 'C', 'X']

    def test_f(self):
        assert typogen.nearest_keys('f') == ['d', 'r', 't', 'g', 'v', 'c']
        assert typogen.nearest_keys('F') == ['D', 'R', 'T', 'G', 'V', 'C']

    def test_g(self):
        assert typogen.nearest_keys('g') == ['f', 't', 'y', 'h', 'b', 'v']
        assert typogen.nearest_keys('G') == ['F', 'T', 'Y', 'H', 'B', 'V']

    def test_h(self):
        assert typogen.nearest_keys('h') == ['g', 'y', 'u', 'j', 'n', 'b']
        assert typogen.nearest_keys('H') == ['G', 'Y', 'U', 'J', 'N', 'B']

    def test_j(self):
        assert typogen.nearest_keys('j') == ['h', 'u', 'i', 'k', 'm', 'n']
        assert typogen.nearest_keys('J') == ['H', 'U', 'I', 'K', 'M', 'N']

    def test_k(self):
        assert typogen.nearest_keys('k') == ['j', 'i', 'o', 'l', 'm']
        assert typogen.nearest_keys('K') == ['J', 'I', 'O', 'L', 'M']

    def test_l(self):
        assert typogen.nearest_keys('l') == ['k', 'o', 'p']
        assert typogen.nearest_keys('L') == ['K', 'O', 'P']

    def test_z(self):
        assert typogen.nearest_keys('z') == ['a', 's', 'x']
        assert typogen.nearest_keys('Z') == ['A', 'S', 'X']

    def test_x(self):
        assert typogen.nearest_keys('x') == ['z', 's', 'd', 'c']
        assert typogen.nearest_keys('X') == ['Z', 'S', 'D', 'C']

    def test_c(self):
        assert typogen.nearest_keys('c') == ['x', 'd', 'f', 'v']
        assert typogen.nearest_keys('C') == ['X', 'D', 'F', 'V']

    def test_v(self):
        assert typogen.nearest_keys('v') == ['c', 'f', 'g', 'b']
        assert typogen.nearest_keys('V') == ['C', 'F', 'G', 'B']

    def test_b(self):
        assert typogen.nearest_keys('b') == ['v', 'g', 'h', 'n']
        assert typogen.nearest_keys('B') == ['V', 'G', 'H', 'N']

    def test_n(self):
        assert typogen.nearest_keys('n') == ['b', 'h', 'j', 'm']
        assert typogen.nearest_keys('N') == ['B', 'H', 'J', 'M']

    def test_m(self):
        assert typogen.nearest_keys('m') == ['n', 'j', 'k']
        assert typogen.nearest_keys('M') == ['N', 'J', 'K']


class TestMissedKey:
    def test_simple(self):
        assert typogen.missed_key('cat') == {
            'xat', 'dat', 'fat', 'vat',
            'cqt', 'cwt', 'cst', 'cxt',
            'czt', 'car', 'ca5', 'ca6',
            'cay', 'cah', 'cag', 'caf',
        }
        assert typogen.missed_key('frog') == {
            'drog', 'rrog', 'trog', 'grog', 'vrog',
            'crog', 'feog', 'f4og', 'f5og', 'ftog',
            'fgog', 'ffog', 'fdog', 'frig', 'fr9g',
            'fr0g', 'frpg', 'frlg', 'frkg', 'frof',
            'frot', 'froy', 'froh', 'frob', 'frov',
        }

    def test_double(self):
        assert typogen.missed_key('bull') == {
            'vull', 'gull', 'hull', 'null',
            'byll', 'b7ll', 'b8ll', 'bill',
            'bkll', 'bjll', 'bhll', 'bukl',
            'buol', 'bupl', 'bulk', 'bulo',
            'bulp',
        }

    def test_with_space(self):
        assert typogen.missed_key('cat frog') == {
            'xat frog', 'dat frog', 'fat frog', 'vat frog',
            'cqt frog', 'cwt frog', 'cst frog', 'cxt frog',
            'czt frog', 'car frog', 'ca5 frog', 'ca6 frog',
            'cay frog', 'cah frog', 'cag frog', 'caf frog',
            'cat drog', 'cat rrog', 'cat trog', 'cat grog',
            'cat vrog', 'cat crog', 'cat feog', 'cat f4og',
            'cat f5og', 'cat ftog', 'cat fgog', 'cat ffog',
            'cat fdog', 'cat frig', 'cat fr9g', 'cat fr0g',
            'cat frpg', 'cat frlg', 'cat frkg', 'cat frof',
            'cat frot', 'cat froy', 'cat froh', 'cat frob',
            'cat frov',
        }

    def test_empty(self):
        assert typogen.missed_key('') == set()

    def test_multiple_spaces(self):
        assert typogen.missed_key('   cat   ') == {
            'xat', 'dat', 'fat', 'vat',
            'cqt', 'cwt', 'cst', 'cxt',
            'czt', 'car', 'ca5', 'ca6',
            'cay', 'cah', 'cag', 'caf',
        }
        assert typogen.missed_key('   frog   ') == {
            'drog', 'rrog', 'trog', 'grog', 'vrog',
            'crog', 'feog', 'f4og', 'f5og', 'ftog',
            'fgog', 'ffog', 'fdog', 'frig', 'fr9g',
            'fr0g', 'frpg', 'frlg', 'frkg', 'frof',
            'frot', 'froy', 'froh', 'frob', 'frov',
        }
        assert typogen.missed_key('   bull   ') == {
            'vull', 'gull', 'hull', 'null',
            'byll', 'b7ll', 'b8ll', 'bill',
            'bkll', 'bjll', 'bhll', 'bukl',
            'buol', 'bupl', 'bulk', 'bulo',
            'bulp',
        }
        assert typogen.missed_key('   cat   frog   ') == {
            'xat frog', 'dat frog', 'fat frog', 'vat frog',
            'cqt frog', 'cwt frog', 'cst frog', 'cxt frog',
            'czt frog', 'car frog', 'ca5 frog', 'ca6 frog',
            'cay frog', 'cah frog', 'cag frog', 'caf frog',
            'cat drog', 'cat rrog', 'cat trog', 'cat grog',
            'cat vrog', 'cat crog', 'cat feog', 'cat f4og',
            'cat f5og', 'cat ftog', 'cat fgog', 'cat ffog',
            'cat fdog', 'cat frig', 'cat fr9g', 'cat fr0g',
            'cat frpg', 'cat frlg', 'cat frkg', 'cat frof',
            'cat frot', 'cat froy', 'cat froh', 'cat frob',
            'cat frov',
        }
        assert typogen.missed_key('   ') == set()


class TestInsertedKey:
    def test_simple(self):
        assert typogen.inserted_key('cat') == {
            'xcat', 'cxat', 'dcat', 'cdat', 'fcat',
            'cfat', 'vcat', 'cvat', 'cqat', 'caqt',
            'cwat', 'cawt', 'csat', 'cast', 'caxt',
            'czat', 'cazt', 'cart', 'catr', 'ca5t',
            'cat5', 'ca6t', 'cat6', 'cayt', 'caty',
            'caht', 'cath', 'cagt', 'catg', 'caft',
            'catf',
        }
        assert typogen.inserted_key('frog') == {
            'dfrog', 'fdrog', 'rfrog', 'frrog', 'tfrog',
            'ftrog', 'gfrog', 'fgrog', 'vfrog', 'fvrog',
            'cfrog', 'fcrog', 'ferog', 'freog', 'f4rog',
            'fr4og', 'f5rog', 'fr5og', 'frtog', 'frgog',
            'ffrog', 'frfog', 'frdog', 'friog', 'froig',
            'fr9og', 'fro9g', 'fr0og', 'fro0g', 'frpog',
            'fropg', 'frlog', 'frolg', 'frkog', 'frokg',
            'frofg', 'frogf', 'frotg', 'frogt', 'froyg',
            'frogy', 'frohg', 'frogh', 'frobg', 'frogb',
            'frovg', 'frogv',
        }

    def test_double(self):
        assert typogen.inserted_key('bull') == {
            'vbull', 'bvull', 'gbull', 'bgull', 'hbull',
            'bhull', 'nbull', 'bnull', 'byull', 'buyll',
            'b7ull', 'bu7ll', 'b8ull', 'bu8ll', 'biull',
            'buill', 'bkull', 'bukll', 'bjull', 'bujll',
            'buhll', 'bulkl', 'buoll', 'bulol', 'bupll',
            'bulpl', 'bullk', 'bullo', 'bullp',
        }

    def test_with_space(self):
        assert typogen.inserted_key('cat frog') == {
            'xcat frog', 'cxat frog', 'dcat frog', 'cdat frog', 'fcat frog',
            'cfat frog', 'vcat frog', 'cvat frog', 'cqat frog', 'caqt frog',
            'cwat frog', 'cawt frog', 'csat frog', 'cast frog', 'caxt frog',
            'czat frog', 'cazt frog', 'cart frog', 'catr frog', 'ca5t frog',
            'cat5 frog', 'ca6t frog', 'cat6 frog', 'cayt frog', 'caty frog',
            'caht frog', 'cath frog', 'cagt frog', 'catg frog', 'caft frog',
            'catf frog', 'cat dfrog', 'cat fdrog', 'cat rfrog', 'cat frrog',
            'cat tfrog', 'cat ftrog', 'cat gfrog', 'cat fgrog', 'cat vfrog',
            'cat fvrog', 'cat cfrog', 'cat fcrog', 'cat ferog', 'cat freog',
            'cat f4rog', 'cat fr4og', 'cat f5rog', 'cat fr5og', 'cat frtog',
            'cat frgog', 'cat ffrog', 'cat frfog', 'cat frdog', 'cat friog',
            'cat froig', 'cat fr9og', 'cat fro9g', 'cat fr0og', 'cat fro0g',
            'cat frpog', 'cat fropg', 'cat frlog', 'cat frolg', 'cat frkog',
            'cat frokg', 'cat frofg', 'cat frogf', 'cat frotg', 'cat frogt',
            'cat froyg', 'cat frogy', 'cat frohg', 'cat frogh', 'cat frobg',
            'cat frogb', 'cat frovg', 'cat frogv',
        }

    def test_empty(self):
        assert typogen.inserted_key('') == set()

    def test_multiple_spaces(self):
        assert typogen.inserted_key('   cat   ') == {
            'xcat', 'cxat', 'dcat', 'cdat', 'fcat',
            'cfat', 'vcat', 'cvat', 'cqat', 'caqt',
            'cwat', 'cawt', 'csat', 'cast', 'caxt',
            'czat', 'cazt', 'cart', 'catr', 'ca5t',
            'cat5', 'ca6t', 'cat6', 'cayt', 'caty',
            'caht', 'cath', 'cagt', 'catg', 'caft',
            'catf',
        }
        assert typogen.inserted_key('   frog   ') == {
            'dfrog', 'fdrog', 'rfrog', 'frrog', 'tfrog',
            'ftrog', 'gfrog', 'fgrog', 'vfrog', 'fvrog',
            'cfrog', 'fcrog', 'ferog', 'freog', 'f4rog',
            'fr4og', 'f5rog', 'fr5og', 'frtog', 'frgog',
            'ffrog', 'frfog', 'frdog', 'friog', 'froig',
            'fr9og', 'fro9g', 'fr0og', 'fro0g', 'frpog',
            'fropg', 'frlog', 'frolg', 'frkog', 'frokg',
            'frofg', 'frogf', 'frotg', 'frogt', 'froyg',
            'frogy', 'frohg', 'frogh', 'frobg', 'frogb',
            'frovg', 'frogv',
        }
        assert typogen.inserted_key('   bull   ') == {
            'vbull', 'bvull', 'gbull', 'bgull', 'hbull',
            'bhull', 'nbull', 'bnull', 'byull', 'buyll',
            'b7ull', 'bu7ll', 'b8ull', 'bu8ll', 'biull',
            'buill', 'bkull', 'bukll', 'bjull', 'bujll',
            'buhll', 'bulkl', 'buoll', 'bulol', 'bupll',
            'bulpl', 'bullk', 'bullo', 'bullp',
        }
        assert typogen.inserted_key('   cat   frog   ') == {
            'xcat frog', 'cxat frog', 'dcat frog', 'cdat frog', 'fcat frog',
            'cfat frog', 'vcat frog', 'cvat frog', 'cqat frog', 'caqt frog',
            'cwat frog', 'cawt frog', 'csat frog', 'cast frog', 'caxt frog',
            'czat frog', 'cazt frog', 'cart frog', 'catr frog', 'ca5t frog',
            'cat5 frog', 'ca6t frog', 'cat6 frog', 'cayt frog', 'caty frog',
            'caht frog', 'cath frog', 'cagt frog', 'catg frog', 'caft frog',
            'catf frog', 'cat dfrog', 'cat fdrog', 'cat rfrog', 'cat frrog',
            'cat tfrog', 'cat ftrog', 'cat gfrog', 'cat fgrog', 'cat vfrog',
            'cat fvrog', 'cat cfrog', 'cat fcrog', 'cat ferog', 'cat freog',
            'cat f4rog', 'cat fr4og', 'cat f5rog', 'cat fr5og', 'cat frtog',
            'cat frgog', 'cat ffrog', 'cat frfog', 'cat frdog', 'cat friog',
            'cat froig', 'cat fr9og', 'cat fro9g', 'cat fr0og', 'cat fro0g',
            'cat frpog', 'cat fropg', 'cat frlog', 'cat frolg', 'cat frkog',
            'cat frokg', 'cat frofg', 'cat frogf', 'cat frotg', 'cat frogt',
            'cat froyg', 'cat frogy', 'cat frohg', 'cat frogh', 'cat frobg',
            'cat frogb', 'cat frovg', 'cat frogv',
        }
        assert typogen.inserted_key('   ') == set()

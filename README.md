# Typogen

[![Travis](https://img.shields.io/travis/2tunnels/typogen.svg)](https://travis-ci.org/2tunnels/typogen)
[![PyPI](https://img.shields.io/pypi/v/typogen.svg)](https://pypi.python.org/pypi/typogen)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/typogen.svg)](https://pypi.python.org/pypi/typogen)
[![PyPI - License](https://img.shields.io/pypi/l/typogen.svg)](https://pypi.python.org/pypi/typogen)

Generate keyboard typos based on keyword.

## Install

Using [pip](https://pip.pypa.io/en/stable/)

```
pip install typogen
```

Using [pipenv](https://docs.pipenv.org/) (it's amazing)

```
pipenv install typogen
```

## Examples

### Python

```python
>>> import typogen
>>> typogen.skip_letter('cat')
{'ct', 'ca', 'at'}
>>> typogen.double_letter('dog')
{'dogg', 'doog', 'ddog'}
>>> typogen.reverse_letters('frog')
{'forg', 'rfog', 'frgo'}
>>> typogen.skip_spaces('blue invisible unicorn')
{'blueinvisible unicorn', 'blue invisibleunicorn'}
>>> typogen.missed_key('cat')
{'ca5', 'cxt', 'cqt', 'vat', 'cay', 'fat', 'dat', 'xat', 'ca6', 'cah', 'cag', 'caf', 'cwt', 'cst', 'car', 'czt'}
>>> typogen.inserted_key('cat')
{'caft', 'caty', 'caxt', 'catf', 'cast', 'cagt', 'cvat', 'cawt', 'catg', 'cwat', 'ca5t', 'cxat', 'catr', 'cayt', 'cat5', 'cath', 'xcat', 'cat6', 'vcat', 'ca6t', 'cart', 'cfat', 'cazt', 'caqt', 'dcat', 'fcat', 'csat', 'cdat', 'czat', 'cqat', 'caht'}
```

### CLI

All available typos

```
$ typogen cat
```

Only skip letter

```
$ typogen cat --skip-letter
```

Both double letter and reverse letters

```
$ typogen cat --double-letter --reverse-letters
```

Check out other options

```
$ typogen --help
```

## Test

Install development requirements

```
pipenv install --dev
```

Test!

```
pytest
```

Lint!

```
flake8
```

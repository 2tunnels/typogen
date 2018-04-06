# Typogen

Generate typos based on keyword.

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

```python
>>> import typogen
>>> typogen.skip_letter('cat')
{'ct', 'ca', 'at'}
>>> typogen.double_letters('dog')
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

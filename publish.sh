#!/usr/bin/env bash

echo '🤘 Building...'
python setup.py sdist bdist_wheel

echo '🤘 Signing...'
gpg --detach-sign -a dist/typogen-*.tar.gz
gpg --detach-sign -a dist/typogen-*.whl

echo '🤘 Uploading...'
twine upload dist/*

echo '🤘 Cleaning...'
rm -rf build dist typogen.egg-info

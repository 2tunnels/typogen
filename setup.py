from setuptools import setup

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='typogen',
    version='0.0.1',
    description='Generate keyboard typos based on keyword.',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Vlad Dm',
    author_email='2tunnels@gmail.com',
    url='https://github.com/2tunnels/typogen',
    packages=['typogen'],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    license='MIT',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities',
    ),
)

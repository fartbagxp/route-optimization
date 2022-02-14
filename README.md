# Route Optimization

This is intended to be a simple program used for collapsing _full_ IP ranges for optimizing routing rules.

## Simple setup

This environment follows a standard python setup.

```
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Have more dependencies? Install and freeze them.

```
python -m pip freeze > requirements.txt
```

## Running

There are example files created under the folder **test_files/**.

```
python main.py --path test_files/test0.txt
```

The output will _try_ to collapse the ranges in the test files into IP ranges.

```
summarizing test_files/test1.txt to route [IPNetwork('10.0.0.0/16')]
10.0.0.0/16: 10.0.0.0 - 10.0.255.255
```

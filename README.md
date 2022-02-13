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
python main.py test_files/test0.txt
```

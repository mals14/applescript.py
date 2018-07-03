[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/applescript.svg?longCache=True)](https://pypi.org/pypi/applescript/)
[![](https://img.shields.io/pypi/v/applescript.svg?maxAge=3600)](https://pypi.org/pypi/applescript/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/applescript.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/applescript.py/)

### Install
```bash
$ [sudo] pip install applescript
```

### Examples
```python
>>> import applescript
>>> r = applescript.run('path/to/file.applescript')
>>> r = applescript.run('return 1')

>>> r.code
0
>>> r.out
'hello world'
>>> r.err
''
```

### Sources
+   [`applescript.run(applescript, flags=None, background=False)`](https://github.com/looking-for-a-job/applescript.py/blob/master/applescript/__init__.py)
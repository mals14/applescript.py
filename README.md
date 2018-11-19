[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/applescript.svg?longCache=True)](https://pypi.org/pypi/applescript/)
[![](https://img.shields.io/pypi/v/applescript.svg?maxAge=3600)](https://pypi.org/pypi/applescript/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/applescript.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/applescript.py/)

#### Install
```bash
$ [sudo] pip install applescript
```

#### Functions
function|description
-|-
`applescript.run(applescript, background=False)`|run applescript file/string
`applescript.tell.app(appname, applescript, background=False)`|execute applescript `tell application "VLC" ...`

#### Examples
```python
>>> import applescript
>>> r = applescript.run('return 1')
>>> r = applescript.run('path/to/file.applescript')

>>> r.code
0
>>> r.out
'hello world'
>>> r.err
''
```

`tell application "appname"`
```python
>>> applescript.tell.app("Terminal",'do script "ls"')
>>> applescript.tell.app("Terminal",'do script "ls"',background=True)
```

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>
<br>

#### Start
Prerequisites: 
 - taskfile https://taskfile.dev/installation/
 - poetry https://python-poetry.org/docs/#installation

Create virtual environment
```commandline
task init
```
Activate virtual environment
```commandline
poetry shell
```
or 
```commandline
source .venv/bin/activate
```
Default task
```commandline
task
```
to execute automatic code formatting, tests and linters.
<br>

#### Linters

##### Flake8

See which plugins are installed
```commandline
flake8 --version
> 4.0.1 (flake8-bugbear: 22.7.1, flake8-darglint: 1.8.1, flake8_builtins: 1.5.2, 
> mccabe: 0.6.1, naming: 0.13.0, pycodestyle: 2.8.0, pyflakes: 2.4.0) 
> CPython 3.10.5 on Linux
```

To set docstring style for darglint add in tox.ini
```
docstring_style = numpy
```

Line length has to be set in **two** places: 
```commandline
tox.ini

[flake8]
max-line-length = 88
```
and in
```commandline
pyproject.toml

[tool.black]
line-length = 88
```

To debug workflows in github actions use 
```commandline
#    - name: Setup tmate session
#      uses: mxschmitt/action-tmate@v3
```

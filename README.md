[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai)  
[![CircleCI](https://circleci.com/gh/Stegallo/adventofcode.svg?style=shield)](https://circleci.com/gh/Stegallo/adventofcode)
[![codecov](https://codecov.io/gh/stegallo/adventofcode/branch/master/graph/badge.svg)](https://codecov.io/gh/stegallo/adventofcode)
<a href="https://codeclimate.com/github/Stegallo/adventofcode/test_coverage"><img src="https://api.codeclimate.com/v1/badges/d3a26d2fed4f5d3b04c7/test_coverage" /></a>
<a href="https://codeclimate.com/github/Stegallo/adventofcode/maintainability"><img src="https://api.codeclimate.com/v1/badges/d3a26d2fed4f5d3b04c7/maintainability" /></a>
# adventofcode

activate the adventofcode virtual environment:
```
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements/base.txt
```

copy the input of the day inside the file
```
y_20xy/input_day<day>.txt
```
you can create a test input file with name
```
y_20xy/input_day<day>_test.txt
```

run the command
```
python -m src --year <year> --day <day>
```
if you want to run against the test file
```
python -m src --year <year> --day <day> --test 1
```

note: to avoid tracking in git your credentials:
```
git update-index --assume-unchanged y_2022/secret.py
```

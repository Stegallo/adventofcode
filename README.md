[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai)  
[![CircleCI](https://circleci.com/gh/Stegallo/adventofcode.svg?style=shield)](https://circleci.com/gh/Stegallo/adventofcode)
[![codecov](https://codecov.io/gh/stegallo/adventofcode/branch/master/graph/badge.svg)](https://codecov.io/gh/stegallo/adventofcode)
<a href="https://codeclimate.com/github/Stegallo/adventofcode/test_coverage"><img src="https://api.codeclimate.com/v1/badges/d3a26d2fed4f5d3b04c7/test_coverage" /></a>
<a href="https://codeclimate.com/github/Stegallo/adventofcode/maintainability"><img src="https://api.codeclimate.com/v1/badges/d3a26d2fed4f5d3b04c7/maintainability" /></a>
# adventofcode

to run the adventofcode environment:
```
sh docker/run.sh
```

copy the input of the day inside the file
```
y_20xy/input_day<day>.txt
```
you can create a test file with name
```
y_20xy/input_day<day>_test.txt
```

inside the container, run the command (for years after 2019)
```
python -m y_20xy --day <day>
```
if you want to run against the test file
```
python -m y_20xy --day <day> --test 1
```

inside the container, run the command (for years before 2019)
```
python y_20xy/common.py <day>
```

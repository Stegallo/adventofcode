[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai)  
[![CircleCI](https://circleci.com/gh/Stegallo/adventofcode.svg?style=shield)](https://circleci.com/gh/Stegallo/adventofcode)
[![codecov](https://codecov.io/gh/stegallo/adventofcode/branch/master/graph/badge.svg)](https://codecov.io/gh/stegallo/adventofcode)
<a href="https://codeclimate.com/github/Stegallo/adventofcode/test_coverage"><img src="https://api.codeclimate.com/v1/badges/d3a26d2fed4f5d3b04c7/test_coverage" /></a>
<a href="https://codeclimate.com/github/Stegallo/adventofcode/maintainability"><img src="https://api.codeclimate.com/v1/badges/d3a26d2fed4f5d3b04c7/maintainability" /></a>
# adventofcode

for solutions in rust, refer to [rust repo][rustrepo]

|    | 2015        | 2016        | 2017        | 2018        | 2019        | 2020        | 2021        | 2022        | 2023        |
| -  | -           | -           | -           | -           | -           | -           | -           | -           |
| 01 | [puzzle][201501p]</br>[✓][201501] |  |  |  |  |  |  | [puzzle][202201p]</br>[✓][202201] | [puzzle][202301p]</br>[✓][202301] |
| 02 | [puzzle][201502p]</br>[✓][201502] |  |  |  |  |  |  |  |  |
| 03 | [puzzle][201503p]</br>[✓][201503] |  |  |  |  |  |  |  |  |
| 04 | [puzzle][201504p]</br>[✓][201504] |  |  |  |  |  |  |  |  |
| 05 | [puzzle][201505p]</br>[✓][201505] |  |  |  |  |  |  |  |  |
| 06 | [puzzle][201506p]</br>[✓][201506] |  |  |  |  |  |  |  |  |
| 07 | [puzzle][201507p]</br>[✓][201507] |  |  |  |  |  |  |  |  |
| 08 | [puzzle][201508p]</br>[✓][201508] |  |  |  |  |  |  |  |  |
| 09 | [puzzle][201509p]</br>[✓][201509] |  |  |  |  |  |  |  |  |
| 10 | [puzzle][201510p]</br>[✓][201510] |  |  |  |  |  |  |  |  |
| 11 | [puzzle][201511p]</br>[✓][201511] |  |  |  |  |  |  |  |  |

[201501]: https://github.com/Stegallo/adventofcode/blob/master/y_2015/day1.py
[201501p]: https://adventofcode.com/2015/day/1
[201502]: https://github.com/Stegallo/adventofcode/blob/master/y_2015/day2.py
[201502p]: https://adventofcode.com/2015/day/2
[201503]: https://github.com/Stegallo/adventofcode/blob/master/y_2015/day3.py
[201503p]: https://adventofcode.com/2015/day/3
[201504]: https://github.com/Stegallo/adventofcode/blob/master/y_2015/day4.py
[201504p]: https://adventofcode.com/2015/day/4
[201505]: https://github.com/Stegallo/adventofcode/blob/master/y_2015/day5.py
[201505p]: https://adventofcode.com/2015/day/5
[201506]: https://github.com/Stegallo/adventofcode/blob/master/y_2015/day6.py
[201506p]: https://adventofcode.com/2015/day/6
[201507]: https://github.com/Stegallo/adventofcode/blob/master/y_2015/day7.py
[201507p]: https://adventofcode.com/2015/day/7
[201508]: https://github.com/Stegallo/adventofcode/blob/master/y_2015/day8.py
[201508p]: https://adventofcode.com/2015/day/8
[201509]: https://github.com/Stegallo/adventofcode/blob/master/y_2015/day9.py
[201509p]: https://adventofcode.com/2015/day/9
[201510]: https://github.com/Stegallo/adventofcode/blob/master/y_2015/day10.py
[201510p]: https://adventofcode.com/2015/day/10
[201511]: https://github.com/Stegallo/adventofcode/blob/master/y_2015/day11.py
[201511p]: https://adventofcode.com/2015/day/11

[202201]: https://github.com/Stegallo/adventofcode/blob/master/y_2022/day1.py
[202201p]: https://adventofcode.com/2022/day/1

[202301]: https://github.com/Stegallo/adventofcode/blob/master/y_2023/day1.py
[202301p]: https://adventofcode.com/2023/day/1

[rustrepo]: https://github.com/Stegallo/adventofcodeinrust

## to run the code

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
git update-index --assume-unchanged secret.py
```

## contributing

install [pre-commit](https://pre-commit.com/)

```
python -m pip install -r requirements/test.txt
```
```
pre-commit install
```

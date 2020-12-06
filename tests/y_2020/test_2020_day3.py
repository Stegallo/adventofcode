from y_2020.day3 import Day
from unittest.mock import patch, mock_open

with patch("builtins.open", mock_open(read_data="")):
    day = Day()


def test_calculate_1():
    day._input_data = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    ]
    assert day._calculate_1() == 7


def test_calculate_2():
    day._input_data = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    ]
    assert day._calculate_2() == 336

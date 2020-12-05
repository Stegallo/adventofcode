from y_2020.day5 import calculate_1, calculate_2, decode_seat
from unittest.mock import patch


def test_calculate_1():
    assert calculate_1(["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR"]) == 567


def test_calculate_2():
    with patch("y_2020.day5.decode_seat") as mock_decode_seat:
        mock_decode_seat.side_effect = [18, 19, 21, 22]
        assert (
            calculate_2(
                [
                    "",
                    "",
                    "",
                    "",
                ]
            )
            == 20
        )


def test_decode_seat():
    assert decode_seat("FBFBBFFRLR") == 357
    assert decode_seat("BFFFBBFRRR") == 567
    assert decode_seat("FFFBBBFRRR") == 119
    assert decode_seat("BBFFBBFRLL") == 820

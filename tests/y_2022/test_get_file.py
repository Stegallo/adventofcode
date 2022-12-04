from __future__ import annotations

from unittest.mock import mock_open, patch

from y_2022.get_file import pull_file


def test_pull_file():

    with patch("requests.Session") as mock_session:
        mock_session().get().text = ""
        with patch("builtins.open", mock_open()) as mock_open_file:
            pull_file(0)
    mock_open_file.assert_called_with("y_2022/input_day0.txt", "w")

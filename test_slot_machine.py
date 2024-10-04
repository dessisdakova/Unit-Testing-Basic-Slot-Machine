import pytest
from unittest.mock import patch
from main import deposit, get_number_of_lines, generate_random_spin, check_winning_combinations, \
    SYMBOLS_AND_COUNT, ROWS, REELS, MAX_LINES


def test_deposit_with_negative_and_zero_input(capsys):
    # Simulate user inputs: first a negative number, then a valid positive number
    with patch('builtins.input', side_effect=["-10", "0", "50"]):
        result = deposit()

        # Capture the printed output
        captured = capsys.readouterr()

        # Check that the error message for a negative deposit is printed
        assert "You must deposit more than $0." in captured.out
        assert "You must deposit more than $0." in captured.out
        assert result == 50


def test_deposit_with_invalid_input(capsys):
    with patch("builtins.input", side_effect=["ten", "$$$", "100"]):
        result = deposit()
        captured = capsys.readouterr()
        assert "Please enter a number." in captured.out
        assert "Please enter a number." in captured.out
        assert result == 100


def test_get_number_of_lines_with_negative_zero_and_out_of_boundaries_input(capsys):
    with patch("builtins.input", side_effect=["-10", "0", "7", "3"]):
        result = get_number_of_lines()
        captured = capsys.readouterr()
        assert f"Please enter a number of lines from 1 to {MAX_LINES}" in captured.out
        assert f"Please enter a number of lines from 1 to {MAX_LINES}" in captured.out
        assert f"Please enter a number of lines from 1 to {MAX_LINES}" in captured.out
        assert result == 3


def test_get_number_of_lines_with_invalid_input(capsys):
    with patch("builtins.input", side_effect=["one", "-----", "5"]):
        result = get_number_of_lines()
        captured = capsys.readouterr()
        assert "Please enter a valid number of lines." in captured.out
        assert "Please enter a valid number of lines." in captured.out
        assert result == 5


def test_generate_random_spin_generates_valid_structure():
    spin = generate_random_spin(ROWS, REELS)
    assert len(spin) == REELS
    for reel in spin:
        assert len(reel) == ROWS


def test_generate_random_spin_generates_only_valid_symbols_from_list():
    spin = generate_random_spin(ROWS, REELS)
    all_symbols = [symbol for symbol in SYMBOLS_AND_COUNT]
    for reel in spin:
        for symbol in reel:
            assert symbol in all_symbols


# Mock spin simulating three reels and three rows for vertical winning checks.
# The check_winning_combinations func is designed to evaluate winning lines vertically,
# because the generate_random_spin func first generates reels and then rows
# so we adjust the mock spin accordingly to reflect that orientation.
mock_spin = [
    ["♠", "♠", "♠"],  # reel 1
    ["♠", "♠", "♠"],  # reel 2
    ["♠", "♦", "♦"]   # reel 3
]


def test_check_winning_combinations_returns_correct_winnings_and_lines():
    bet = 10
    lines = 5
    winnings, winning_lines = check_winning_combinations(mock_spin, lines, bet)
    assert winnings == 400
    assert winning_lines == [1, 5]

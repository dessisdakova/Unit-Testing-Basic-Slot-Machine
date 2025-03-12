from slot_machine.constants import SYMBOLS_AND_COUNT, ROWS, REELS
from slot_machine.core import _get_all_available_symbols, generate_random_reels_in_spin, convert_reels_to_rows, \
    check_winning_combinations


def test__get_all_available_symbols_returns_correct_symbols():
    expected_symbol_count = sum(SYMBOLS_AND_COUNT.values())

    actual_symbols = _get_all_available_symbols()

    assert len(actual_symbols) == expected_symbol_count
    for symbol, count in SYMBOLS_AND_COUNT.items():
        assert actual_symbols.count(symbol) == count


def test_generate_random_spin_generates_correct_structure():
    spin = generate_random_reels_in_spin(ROWS, REELS)

    assert len(spin) == REELS
    for reel in spin:
        assert len(reel) == ROWS


def test_convert_reels_to_rows_correctly_transforms_spin():
    mock_reels = [
        ["♦", "♦", "♦"],
        ["♥", "♥", "♥"],
        ["♣", "♣", "♣"]
    ]
    expected = [
        ["♦", "♥", "♣"],
        ["♦", "♥", "♣"],
        ["♦", "♥", "♣"]
    ]

    result = convert_reels_to_rows(mock_reels)

    assert result == expected


def test_check_winning_combinations_1st_to_3rd_lines():
    mock_spin = [
        ["♦", "♦", "♦"],
        ["♥", "♥", "♥"],
        ["♠", "♠", "♠"]
    ]
    bet = 10
    lines = 5

    winnings, winning_lines = check_winning_combinations(mock_spin, lines, bet)

    assert winnings == 450
    assert winning_lines == [1, 2, 3]


def test_check_winning_combinations_4rd_5th_lines():
    mock_spin = [
        ["♣", "♥", "♣"],
        ["♥", "♣", "♥"],
        ["♣", "♠", "♣"]
    ]
    bet = 10
    lines = 5

    winnings, winning_lines = check_winning_combinations(mock_spin, lines, bet)

    assert winnings == 100
    assert winning_lines == [4, 5]

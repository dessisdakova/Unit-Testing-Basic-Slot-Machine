import pytest
from unittest.mock import patch
from main import deposit, get_number_of_lines, get_bet, generate_symbols_in_reel, generate_random_spin, \
    convert_reels_to_rows, print_spin, check_winning_combinations, spin, compare_total_bet_and_balance, \
    print_winnings, main, SYMBOLS_AND_COUNT, ROWS, REELS, MAX_LINES, MAX_BET, MIN_BET


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


def test_get_bet_with_negative_zero_and_out_of_boundaries_input(capsys):
    with patch("builtins.input", side_effect=(["-5", "0", "150", "20"])):
        result = get_bet()
        captured = capsys.readouterr()
        assert f"Bet must be between ${MIN_BET} - ${MAX_BET}" in captured.out
        assert f"Bet must be between ${MIN_BET} - ${MAX_BET}" in captured.out
        assert f"Bet must be between ${MIN_BET} - ${MAX_BET}" in captured.out
        assert result == 20


def test_get_bet_with_invalid_input(capsys):
    with patch("builtins.input", side_effect=(["one", "$", "1.5", "10"])):
        result = get_bet()
        captured = capsys.readouterr()
        assert "Please enter a number." in captured.out
        assert "Please enter a number." in captured.out
        assert "Please enter a number." in captured.out
        assert result == 10


def test_generate_symbols_in_reel_returns_correct_values_and_counts():
    actual_symbols = generate_symbols_in_reel()
    expected_symbol_count = sum(SYMBOLS_AND_COUNT.values())
    # Check the total count of symbols is correct
    assert len(actual_symbols) == expected_symbol_count
    # Check that the symbols and their counts match the expected counts
    for symbol, count in SYMBOLS_AND_COUNT.items():
        assert actual_symbols.count(symbol) == count


def test_generate_random_spin_generates_correct_structure():
    spin = generate_random_spin(ROWS, REELS)
    assert len(spin) == REELS
    for reel in spin:
        assert len(reel) == ROWS


def test_convert_reels_to_rows_correctly_transforms_spin():
    mock_reels = [
        ["♦", "♦", "♦"],
        ["♥", "♥", "♥"],
        ["♣", "♣", "♣"]
    ]
    result = convert_reels_to_rows(mock_reels)
    expected = [
        ["♦", "♥", "♣"],
        ["♦", "♥", "♣"],
        ["♦", "♥", "♣"]
    ]
    assert result == expected


def test_print_spin_correctly_prints(capsys):
    rows = [
        ["♠", "♠", "♠"],
        ["♠", "♠", "♠"],
        ["♠", "♦", "♦"]
    ]
    print_spin(rows)
    captured = capsys.readouterr()
    expected = "♠ | ♠ | ♠\n♠ | ♠ | ♠\n♠ | ♦ | ♦\n"
    assert captured.out == expected


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


def test_compare_total_bet_and_balance(capsys):
    with patch("main.get_number_of_lines", side_effect=[5]), \
            patch("main.get_bet", side_effect=[5, 4]):
        balance = 20
        bet, lines, total_bet = compare_total_bet_and_balance(balance)
        captured = capsys.readouterr()
        expected_output = f"You don't have enough to bet that amount. Your current credit is ${balance}."
        assert expected_output in captured.out
        assert bet == 4
        assert lines == 5
        assert total_bet == 20


def test_print_winnings(capsys):
    winnings = 150
    winning_lines = [1, 2, 3]
    print_winnings(winnings, winning_lines)
    captured = capsys.readouterr()
    expected = f"You won ${winnings}.\nYou won on lines : {', '.join(map(str, winning_lines))}"


def test_spin_returns_correct_value():
    balance = 100
    with patch("main.compare_total_bet_and_balance") as mock_compare_total_bet_and_balance, \
         patch("main.generate_random_spin") as mock_generate_random_spin, \
         patch("main.convert_reels_to_rows") as mock_convert_reels_to_rows, \
         patch("main.check_winning_combinations") as mock_check_winning_combinations, \
         patch("main.print_spin") as mock_print_spin, \
         patch("main.print_winnings") as mock_print_winnings:

        mock_compare_total_bet_and_balance.return_value = (10, 3, 30)
        mock_generate_random_spin.return_value = [['♠', '♥', '♦'], ['♣', '♠', '♦'], ['♥', '♣', '♠']]
        mock_convert_reels_to_rows.return_value = [['♠', '♣', '♥'], ['♥', '♠', '♣'], ['♦', '♦', '♦']]
        mock_check_winning_combinations.return_value = (100, [3])

        result = spin(balance)
        expected_win = 100
        expected_total_bet = 30
        expected_result = expected_win - expected_total_bet

        assert result == expected_result
        mock_compare_total_bet_and_balance.assert_called_once()
        mock_generate_random_spin.assert_called_once()
        mock_convert_reels_to_rows.assert_called_once()
        mock_check_winning_combinations.assert_called_once()


def test_main_quits_when_user_cashes_out(capsys):
    with patch("main.deposit") as mock_deposit, \
         patch("builtins.input", side_effect=["x"]):

        mock_deposit.return_value = 70
        main()
        captured = capsys.readouterr()
        expected = f"Current balance is $70.\nYou have cashed out $70.\n"

        assert captured.out == expected
        mock_deposit.assert_called_once_with()


def test_main_quits_when_balance_is_zero(capsys):
    with patch("main.deposit") as mock_deposit,\
         patch("builtins.input", side_effect=[""]), \
         patch("main.spin") as mocked_spin:

        mock_deposit.return_value = 50
        mocked_spin.return_value = -50
        main()
        captured = capsys.readouterr()
        expected = f"Current balance is $50.\nYour current credit is $0. You can not play anymore!\n"
        assert captured.out == expected
        mock_deposit.assert_called_once()
        mocked_spin.assert_called_once()

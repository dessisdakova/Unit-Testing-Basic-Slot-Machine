# Slot Machine Game Unit Testing in Python

## Project Overview
This project implements a simple Slot Machine game in Python. The game allows users to deposit money,select lines and bet, spin the reels, and check for winning combinations. The winning lines and corresponding payouts are determined based on predefined symbols and their multipliers. The game ends when the balance gets to zero or the play chooses to cash out.

## Features
- User-friendly interface for deposits and spins<br />
- Randomly generated spins<br />
- Different winning lines with associated payouts<br />
- Input validation for deposit, lines and bet<br />
- Updates the current balance by considering total bets and winnings.<br />
- Unit tests for core functionalities

## Functions
```python
deposit()
```
Prompts the user to enter an amount to deposit into their slot machine balance. It validates the input to ensure it is a positive integer. If the input is invalid (non-numeric or less than or equal to zero), the function provides appropriate feedback and continues to prompt the user until a valid amount is entered. The function returns the deposited amount as an integer.<br />
```python
get_number_of_lines()
```
Prompts the user to specify the number of lines they wish to bet on in the slot machine game. It validates the input to ensure it is an integer within the range of 1 to MAX_LINES. If the input is invalid, the function provides feedback and continues to prompt the user until a valid number is entered. The function returns the selected number of lines as an integer.<br />
```python
get_bet()
```
Prompts the user to enter a betting amount for each line in the slot machine game. It validates the input to ensure it is a number within the defined minimum (MIN_BET) and maximum (MAX_BET) limits. If the input is invalid, it provides appropriate feedback and prompts the user to try again until a valid bet is entered. The function returns the valid bet amount as an integer.<br />
```python
generate_random_spin(rows, reels)
```
Generates a random spin for the slot machine by creating a specified number of reels, each containing a specified number of rows. It populates the reels with symbols based on their defined counts in the SYMBOLS_AND_COUNT dictionary, ensuring that each symbol appears the correct number of times. The resulting structure is a nested list representing the random outcome of the spin.<br />
```python
print_spin(reels)
```
Displays the current spin of the slot machine in a user-friendly format. It transposes the reel data to print each row of symbols horizontally, separating symbols with a vertical bar (|). This visual representation helps players easily see the outcome of their spin.<br />
```python
check_winning_combinations(current_spin, lines, bet)
```
Evaluates the current spin of the slot machine to determine potential winnings. It checks predefined winning lines against the symbols displayed in the current spin. If all symbols in a winning line match, it calculates the total winnings based on the corresponding symbol's multiplier and the player's bet. The function returns the total winnings and a list of winning lines for the current spin.<br />
```python
spin(balance)
```
This function manages a single spin of the slot machine. It prompts the user to select the number of lines to bet on and the amount to wager per line, ensuring the total bet does not exceed the available balance. After generating a random spin and displaying the results, it calculates the current winnings and updates the balance based on the total bet and winnings.<br />
```python
main()
```
Orchestrates the flow of the slot machine game. It first prompts the user to deposit an initial balance. Then, it enters a loop where the user can either spin the slot machine or cash out. If the user opts to spin, the function updates the balance based on the results of the spin. The loop continues until the user chooses to cash out or their balance reaches zero, at which point a message is displayed indicating that they can no longer play.<br />

## Tech Stack
*Language:* Python 3.11.3<br />
*IDE:* PyCharm Community Edition 2021<br />
*Testing Framework:*  Pytest<br />

## Test Cases

### Deposit Function Tests
1. **`test_deposit_with_negative_and_zero_input(capsys)`**
   - Tests the `deposit` function for negative and zero inputs. It simulates user inputs of `-10`, `0`, and then a valid input `50`. The test verifies that appropriate error messages are printed for invalid inputs and that the final returned value is `50`.

2. **`test_deposit_with_invalid_input(capsys)`**
   - Tests the `deposit` function for invalid inputs such as strings and symbols. It simulates inputs of `"ten"`, `"$$$"`, and then a valid input of `100`. The test checks that the error message for invalid entries is printed and that the returned value is `100`.

### Get Number of Lines Function Tests
3. **`test_get_number_of_lines_with_negative_zero_and_out_of_boundaries_input(capsys)`**
   - Tests the `get_number_of_lines` function for negative, zero, and out-of-bound inputs. It simulates inputs of `-10`, `0`, `7`, and finally `3`. The test asserts that the appropriate error messages are printed for invalid inputs and that the returned value is `3`.

4. **`test_get_number_of_lines_with_invalid_input(capsys)`**
   - Tests the `get_number_of_lines` function for invalid string inputs. It simulates inputs of `"one"`, `"-----"`, and a valid input of `5`. The test ensures that the correct error message is printed for invalid entries and that the returned value is `5`.

### Generate Random Spin Function Tests
5. **`test_generate_random_spin_generates_valid_structure()`**
   - Tests that the `generate_random_spin` function produces a valid structure for the spin. It checks that the generated spin has the correct number of reels (`ROWS`) and rows (`REELS`).

6. **`test_generate_random_spin_generates_only_valid_symbols_from_list()`**
   - Tests that the `generate_random_spin` function only generates valid symbols as defined in the `SYMBOLS_AND_COUNT` dictionary. The test ensures that every symbol in the generated spin is contained in the valid symbols list.

### Check Winning Combinations Function Test
7. **`test_check_winning_combinations_returns_correct_winnings_and_lines()`**
   - Tests the `check_winning_combinations` function using a predefined `mock_spin`. It simulates a scenario where the winning lines are vertical, reflecting how the function checks for winning combinations. The test verifies that the function returns the correct winnings and winning lines when provided with the mock spin, a bet of `10`, and `5` lines.

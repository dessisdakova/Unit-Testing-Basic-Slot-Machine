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
generate_symbols_in_reel()
```
Generates a list of symbols for a each reel in the slot machine based on predefined symbol counts. It iterates over a dictionary of symbols and their respective counts, appending each symbol to the reel the number of times specified in the dictionary. The resulting list is used to simulate the content of the slot machine reel with the appropriate symbol distribution.<br />
```python
generate_random_spin(rows, reels)
```
Generates a random spin for the slot machine by creating a specified number of reels, each containing a specified number of rows. It first retrieves all possible symbols from the generate_symbols_in_reel() function and then creates each reel by randomly choosing a symbol for each row without repetition (per reel). The resulting list of reels represents the visual outcome of a slot machine spin. <br />
```python
convert_reels_to_rows(reels)
```
Converts the list of reels (which represent columns in a slot machine) into rows for easier processing and display. It transposes the reels by iterating through each row index and gathering the corresponding symbols from each reel, creating a new list of rows. This format is more intuitive for checking winning combinations and printing.<br />
```python
print_spin(reels)
```
Prints the slot machine spin results in a user-friendly format. It takes the transposed rows of symbols and displays them, separating symbols in each row with a " | " delimiter, simulating the visual layout of a slot machine.<br />
```python
check_winning_combinations(current_spin, lines, bet)
```
Evaluates the current spin of the slot machine to determine potential winnings. It checks predefined winning lines against the symbols displayed in the current spin. If all symbols in a winning line match, it calculates the total winnings based on the corresponding symbol's multiplier and the player's bet. The function returns the total winnings and a list of winning lines for the current spin.<br />
```python
compare_total_bet_and_balance(balance)
```
Prompts the player to input their bet amount and the number of lines they wish to play, ensuring that the total bet does not exceed their available balance. It continually requests a valid bet until the player provides one that fits within their balance. Once a valid bet is received, the function prints the betting details, including the bet amount, the number of lines, and the total bet amount. It returns the bet amount, the number of lines, and the total bet.<br />
```python
spin(balance)
```
Simulates a spin in the slot machine game. It first verifies the player's bet amount and the number of lines through the compare_total_bet_and_balance() function, ensuring the total bet does not exceed the player's balance. It then generates a random arrangement of symbols for the reels using generate_random_spin(), converts this arrangement into rows with convert_reels_to_rows(), and prints the resulting spin layout with print_spin(). After displaying the spin, it checks for winning combinations using check_winning_combinations(), printing any winnings and the corresponding winning lines with print_winnings(). Finally, the function returns the net result of the spin by subtracting the total bet from the total winnings.<br />
```python
print_winnings(winnings, winning_lines)
```
Displays the player's winnings from the slot machine spin. It prints the total amount won and, if there are any winnings, it also outputs the specific lines on which the player won. The unpack operator (\*) is used to format the winning lines as a space-separated list in the output, providing a clear and concise display of the winning information.<br />
```python
main()
```
Orchestrates the flow of the slot machine game. It first prompts the user to deposit an initial balance. Then, it enters a loop where the user can either spin the slot machine or cash out. If the user opts to spin, the function updates the balance based on the results of the spin. The loop continues until the user chooses to cash out or their balance reaches zero, at which point a message is displayed indicating that they can no longer play.<br />

## Tech Stack
*Language:* Python 3.11.3<br />
*IDE:* PyCharm Community Edition 2021<br />
*Testing Framework:*  pytest<br />

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

### Get Bet Function Tests
5. **`test_get_bet_with_negative_zero_and_out_of_boundaries_input(capsys)`**
   - Verifies that the `get_bet()` function correctly handles invalid input values, including negative numbers, zero, and values exceeding the maximum limit. The test simulates user input of `-5`, `0`, and `150`, ensuring that the function prompts the user with the appropriate error message indicating that the bet must be within the defined limits (`MIN_BET` to `MAX_BET`). It also checks that the function returns a valid bet value of `20` when the input is finally acceptable.
   
6. **`test_get_bet_with_invalid_input(capsys)`**
   - Ensures that the `get_bet()` function handles invalid input gracefully by prompting the user when non-numeric values are entered. The test simulates user input of `"one"`, `"$"`, and `"1.5"`, which are all invalid for a betting amount. It verifies that the function outputs the appropriate message, "Please enter a number," for each invalid input and that it ultimately returns a valid bet amount of `10` when a correct value is finally provided.
   
### Generate Symbols in Reel Function Test
7. **`test_generate_symbols_in_reel_returns_correct_values_and_counts()`**
   - Verifies the functionality of the `generate_symbols_in_reel()` function. It checks that the total number of symbols generated matches the expected count based on the predefined `SYMBOLS_AND_COUNT` dictionary. Additionally, the test ensures that each symbol is generated the correct number of times according to its specified count. This ensures the integrity and accuracy of the symbol generation process within the slot machine logic.

### Generate Random Spin Function Test
8. **`test_generate_random_spin_generates_correct_structure()`**
   - Validates the structure of the output generated by the `generate_random_spin()` function. It checks that the number of reels produced matches the expected count defined by `REELS`. Additionally, it ensures that each reel contains the correct number of rows specified by `ROWS`. This ensures that the random spin generation adheres to the defined slot machine configuration.
).

### Convert Reels to Rows Function Test
9. **`test_convert_reels_to_rows_correctly_transforms_spin()`**
   - Verifies the functionality of the `convert_reels_to_rows()` function by checking its ability to correctly transpose the input structure of reels into rows. A mock input representing a set of reels is provided, and the test ensures that the output matches the expected row configuration. This is crucial for confirming that the slot machine's reel data is correctly formatted for processing winning combinations.

### Print Spin Function Test
10. **`test_print_spin_correctly_prints(capsys)`**
	- Checks the `print_spin()` function to ensure it correctly formats and prints the spin results of the slot machine. A predefined set of rows is passed to the function, and the output is captured using `capsys`. The test asserts that the printed output matches the expected string format, validating that the symbols are correctly displayed with the appropriate separators and line breaks.

### Check Winning Combinations Function Tests
11. **`test_check_winning_combinations_1st_to_3rd_lines()`**
   - Evaluates the `check_winning_combinations()` function by simulating a mock spin result where all symbols in the first three lines match. It sets a bet of 10 and checks for a total of 5 lines. The test asserts that the calculated winnings equal 450 and that the winning lines returned are [1, 2, 3], ensuring the function correctly identifies and calculates winnings based on winning combinations.
   
12. **`test_check_winning_combinations_4rd_5th_lines()`**
	- Assesses the `check_winning_combinations()` function by simulating a mock spin result where the symbols in the fourth and fifth lines match. It sets a bet of 10 and checks for a total of 5 lines. The test asserts that the winnings calculated are 100 and that the winning lines returned are [4, 5], verifying that the function accurately identifies and computes winnings for these winning combinations.
	
### Compare Total Bet and Balance Function Test
13. **`test_compare_total_bet_and_balance(capsys)`**
	- Checks the `compare_total_bet_and_balance()` function by simulating a bet that exceeds the user's balance. It verifies that the appropriate error message is shown, the bet is adjusted to a valid amount, the number of lines is correct, and the total bet reflects the adjusted inputs.

	
### Print Winnings Function Test
14. **`test_print_winnings(capsys)`**
	- Verifies the `print_winnings()` function by capturing the output when winnings and winning lines are printed. It checks that the output correctly reflects the amount won and the lines on which the player won.


### Spin Function Test
15. **`test_spin_returns_correct_value()`**
	- Checks that the `spin()` function returns the correct net winnings by mocking the dependencies. It ensures the function accurately calculates the result based on the balance, total bet, and winnings, and verifies that each mocked function is called exactly once.

	
### Main Function Tests
16. **`test_main_quits_when_user_cashes_out(capsys)`**
	- Verifies that the `main()` function correctly handles a user cashing out. It mocks the `deposit()` function to return a balance of $70, simulates user input to cash out, and checks that the output message reflects the current balance and confirms the cash-out.

17. **`test_main_quits_when_balance_is_zero(capsys)`**
	- Checks that the `main()` function correctly handles the scenario when the user's balance reaches zero after a spin. It mocks the `deposit()` function to return a balance of $50 and simulates a spin that results in a total loss of $50. The test verifies that the appropriate message is displayed, indicating the balance and that the user can no longer play.

	


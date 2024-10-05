import random

MAX_LINES = 5
MIN_BET = 1
MAX_BET = 100

ROWS = 3
REELS = 3

# pass this dictionary to get_slot_machine_spin() func
SYMBOLS_AND_COUNT = {
    "♠": 5,
    "♥": 5,
    "♦": 10,
    "♣": 10
}

WINNING_LINES = {
    1: [(0, 0), (0, 1), (0, 2)],  # Top row
    2: [(1, 0), (1, 1), (1, 2)],  # Middle row
    3: [(2, 0), (2, 1), (2, 2)],  # Bottom row
    4: [(0, 0), (1, 1), (2, 2)],  # Diagonal from top-left to bottom-right
    5: [(2, 0), (1, 1), (0, 2)],  # Diagonal from bottom-left to top-right
}

# pass this dictionary to check_all_winnings func
SYMBOLS_AND_MULTIPLIERS = {
    "♠": 20,
    "♥": 15,
    "♦": 10,
    "♣": 5
}


# returns deposit money
def deposit():
    while True:
        amount = input("How much would you like to deposit? : ")
        try:
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("You must deposit more than $0.")
        except ValueError:
            print("Please enter a number.")
    return amount


# returns number of selected lines
def get_number_of_lines():
    while True:
        lines = input("How many lines would you like to bet on? (1 - " + str(MAX_LINES) + ") : ")
        try:
            lines = int(lines)
            if 1 <= lines <= 5:
                break
            else:
                print(f"Please enter a number of lines from 1 to {MAX_LINES}")
        except ValueError:
            print("Please enter a valid number of lines.")
    return lines


# returns selected bet per line
def get_bet():
    while True:
        bet = input(f"How much would you like to bet on each line? (${MIN_BET} - ${MAX_BET}) : ")
        try:
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break;
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}")
        except ValueError:
            print("Please enter a number.")
    return bet


def generate_symbols_in_reel():
    symbols_per_reel = []
    # .items gives the key and the value associated with the dictionary
    for symbol, symbol_count in SYMBOLS_AND_COUNT.items():
        # adding the symbol to all_symbols list as many times as its count
        for _ in range(symbol_count):
            symbols_per_reel.append(symbol)
    return symbols_per_reel


# generates a spin using rows, reels and symbol dict and returns a dictionary
def generate_random_spin(rows, reels):
    all_symbols = generate_symbols_in_reel()
    # selecting what values are going to go in every single reel
    reels_dict = []
    # generating the reel
    for _ in range(reels):
        reel = []
        current_symbols = all_symbols[:]  # [:] copies the list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            reel.append(value)

        reels_dict.append(reel)
    return reels_dict


def convert_reels_to_rows(reels):
    rows = []
    # Loop through the rows of each reel (columns) and transpose them to rows
    for row_idx in range(len(reels[0])):  # Assuming all reels have the same number of rows
        row = [reels[reel_idx][row_idx] for reel_idx in range(len(reels))]
        rows.append(row)
    return rows


def print_spin(rows):
    for row in rows:
        print(" | ".join(row))


def check_winning_combinations(transposed_spin, lines, bet):
    total_winnings = 0
    winning_lines = []

    for line in range(1, lines + 1):
        # Get the positions for the current line from the WINNING_LINES dictionary
        positions = WINNING_LINES[line]
        # Check if all symbols in those positions are the same
        first_symbol = transposed_spin[positions[0][0]][positions[0][1]]  # Get the first symbol
        for (row, reel) in positions:
            if transposed_spin[row][reel] != first_symbol:
                break
        else:
            # All symbols in this line match, it's a win
            total_winnings += SYMBOLS_AND_MULTIPLIERS[first_symbol] * bet
            winning_lines.append(line)

    return total_winnings, winning_lines


def compare_total_bet_and_balance(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(f"You don't have enough to bet that amount. Your current credit is ${balance}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")
    return bet, lines, total_bet


# performs a spin using balance and returns winnings value
def spin(balance):
    bet, lines, total_bet = compare_total_bet_and_balance(balance)
    spin_be_reels = generate_random_spin(ROWS, REELS)
    transposed_spin = convert_reels_to_rows(spin_be_reels)
    print_spin(transposed_spin)
    winnings, winning_lines = check_winning_combinations(transposed_spin, lines, bet)
    print_winnings(winnings, winning_lines)
    return winnings - total_bet


def print_winnings(winnings, winning_lines):
    print(f"You won ${winnings}.")
    if winnings:
        print(f"You won on lines :", *winning_lines)  # * - unpack operator


# runs the game
def main():
    balance = deposit()
    while balance > 0:
        print(f"Current balance is ${balance}.")
        answer = input("Press \"enter\" to spin or \"x\" to cash out : ")
        if answer == "x":
            print(f"You have cashed out ${balance}.")
            break
        balance += spin(balance)
    if balance == 0:
        print("Your current credit is $0. You can not play anymore!")


# calling the main function to start the game
if __name__ == "__main__":
    main()  # This will only run if the script is executed directly, not imported

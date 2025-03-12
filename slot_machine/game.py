from slot_machine.constants import ROWS, REELS
from slot_machine.core import generate_random_reels_in_spin, convert_reels_to_rows, check_winning_combinations
from slot_machine.utils import compare_total_bet_and_balance, print_spin, print_winnings, get_deposit


def spin(balance) -> int:
    """Performs a single spin of the slot machine.

    This function manages the process of a single spin, including:
        1.  Getting the bet and number of lines from the player.
        2.  Generating the random spin.
        3.  Converting the reels to rows.
        4.  Printing the spin result.
        5.  Checking for winning combinations and calculating winnings.
        6.  Printing the winnings.
        7.  Returning the net change in the player's balance.

    :param balance: The current balance of the player.
    :return: The net change in the player's balance (winnings - total bet).
    """
    bet, lines, total_bet = compare_total_bet_and_balance(balance)
    spin_be_reels = generate_random_reels_in_spin(ROWS, REELS)
    transposed_spin = convert_reels_to_rows(spin_be_reels)
    print_spin(transposed_spin)
    winnings, winning_lines = check_winning_combinations(transposed_spin, lines, bet)
    print_winnings(winnings, winning_lines)
    return winnings - total_bet

def main():
    """Runs the main game loop of the slot machine.

    This function manages the overall game flow, including:
        1.  Getting the initial deposit from the player.
        2.  Looping until the player's balance is zero, or they choose to cash out.
        3.  Displaying the current balance.
        4.  Prompting the player to spin or cash out.
        5.  Performing a spin and updating the balance.
        6.  Displaying a cash-out message when the player cashes out.
        7.  Displaying a game over message when the balance reaches zero.
    """
    balance = get_deposit()
    while balance > 0:
        print(f"Current balance is ${balance}.")
        answer = input("Press \"enter\" to spin or \"x\" to cash out: ")
        if answer == "x":
            print(f"You have cashed out ${balance}.")
            break
        balance += spin(balance)
    if balance == 0:
        print("Your current credit is $0. You can not play anymore!")


if __name__ == '__main__':
    main()
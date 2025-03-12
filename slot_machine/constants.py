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
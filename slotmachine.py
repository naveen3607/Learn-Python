import random

MAX_LINES = random[1:6]
MAX_BET = 100
MIN_BET = 1

ROWS = MAX_LINES
COLS = MAX_LINES


def deposit():
    while True:
        amount = input("What would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter the valid number of lines.")
        else:
            print("Please enter a number.")
    return lines


def get_bet():
    while True:
        bet_amount = input("What would you like to bet? $ ")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return bet_amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet_amount = get_bet()
        total_bet_amount = bet_amount * lines
        if total_bet_amount > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance} ")
        else:
            break

    print(f"You are betting ${bet_amount} on {lines} lines. Total bet is equal to ${total_bet_amount}")


main()

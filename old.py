import random


possible_nums = [["0"],  # 0
                 ["1", "3", "5", "7", "9", "12", "14", "16", "18", "19", "21", "23", "25", "27", "30", "32", "34", "36"],  # reds
                 ["2", "4", "6", "8", "10", "11", "13", "15", "17", "20", "22", "24", "26", "28", "29", "31", "33", "35"]]  # blacks


green = set(possible_nums[0])
reds = set(possible_nums[1])
blacks = set(possible_nums[2])


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


def start_game():
    while True:
        print("Welcome to 'The Rarlette Wheel'.")
        start = input("Press the enter key to start (q to quit). ")
        if start == "":
            main()
        elif start.lower() == "q":
            print("Thanks for playing!")
            break
        else:
            print("Please enter a valid option.")


def get_spin():
    winning_num = []

    for _ in range(1):
        value = random.randrange(0, 36)

        winning_num.append(value)
    return set(winning_num)


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end=" ")

        print()


def deposit():
    while True:
        amount = input("How much would you like to deposit? £")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_red_or_black():
    while True:
        choice = input(
            "Would you like to bet on red, black or green? (Enter 'r' for red, 'b' for black and 'g' for green (0))? ")
        betting_on = []
        if choice.lower() == "r":
            choice = "red"
            betting_on = reds
            break
        elif choice.lower() == "b":
            choice = "black"
            betting_on = blacks
            break
        elif choice.lower() == "g":
            choice = "green"
            betting_on = green
            break
        else:
            print("Enter a valid option.")

    get_num_bet()

    return choice, betting_on


def get_num_bet():
    num_bet = []
    seperator = ", "

    while True:
        choice = input(
            "What numbers will you bet on? (Type as the example shows: '1, 24, 12, 27, 8' or 'n' for none. ")
        if str(choice.split(seperator)):
            num_choice = choice.split(seperator)
            num_bet = num_choice
            break
            
        elif choice == "n":
            break

        else:
            print("Enter a valid option.")
            pass
    print(num_bet)

    return num_bet

def add_red_bet_and_num():
    player_bet = set(get_red_or_black()) + set(get_num_bet())
    print(type(player_bet))

def get_bet():
    while True:
        amount = input("How much would you like to bet? £")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between £{MIN_BET} - £{MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount



def spin(balance):
    ranNum = str(random.randint(0,36))
    _, player_bet = get_red_or_black().__add__(tuple(get_num_bet())) # player is betting_on

    while True:
        bet = get_bet()
        total_bet = bet * 2

        if bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: £{balance}")
        else:
            break

    print()
    print(f"You are betting £{bet} on {player_bet}. Total bet is equal to: £{total_bet}")

    # slots = get_slotmachine_spin(ROWS, COLS, symbol_count)
    # print_slot_machine(slots)

    winnings = total_bet
    winning_number = ranNum
    if winning_number in player_bet:
        has_won = True
    else:
        has_won = False

    print(winning_number)
    print(player_bet)
    print(has_won)

    if has_won == True:
        print(f"You won £{winnings}.")
        print(f"You won on: {winning_number}")
    else:
        print()
        print("You didn't win anything this time.")
        print(f"The winning number was: {winning_number}")

        return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is: £{balance}")
        answer = input("Press enter to spin! ('q' to go to the main menu).")
        if answer.lower() == "q":
            start_game()
        balance += spin(balance)
    print(f"You left with £{balance}")


start_game()

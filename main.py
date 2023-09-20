import random
import re
import time

green = [0]
reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
blacks = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

bal = 0

MAX_BET = 101
MIN_BET = 1


def start_game():
    while True:
        print("Welcome to 'The Rarlette Wheel'.")
        start = input("Press the enter key to start (q to quit). ")
        if start == "":
            deposit()
        elif start.lower() == "q":
            print("Thanks for playing!")
            break
        else:
            print("Please enter a valid option.")


def deposit():
    while True:
        print()
        amount = input("How much would you like to deposit? £")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    global bal
    bal += amount
    main()
    return amount


def main():
    global bal
    plr_bal = bal
    print()
    inp = input("Would you like to spin, or deposit money? (Press enter to spin, or type 'd' to deposit. "
                "\n")
    if inp == "":
        pass
    elif inp.lower() == "d":
        print()
        deposit()
    else:
        print("Please enter a valid option.")

    while True:
        print(f"Your current balance is: £{plr_bal}")
        num_bet = input("What numbers' would you like to bet on (separated with just one space ' ')? "
                        "\n")
        print()
        b = list(num_bet.split(' '))
        for i in range(len(b)):
            if re.match('\d+', b[i]):
                if b[i].isdecimal() and int(b[i]) < 0 or int(b[i]) > 36:
                    invalid_num = b[i]
                    print(f"{invalid_num} is not a valid number. Please choose between 0, and 36.")
                    main()
                else:
                    continue
            else:
                print()
                invalid_num = b[i]
                print(f"//// '{invalid_num}' is not a valid number. Please choose between 0, and 36.")
                print()
                main()

        print(b)

        bet_amount = input("How much would you like to bet? £")

        if bet_amount.isdigit():
            print()
            bet_amount = int(bet_amount)
            if len(b) > 1:
                t_bet_amount = bet_amount * len(b)
                # print("t_bet_amount", t_bet_amount)

            elif bet_amount * len(b) > plr_bal:
                print("////", bet_amount)
                print("You do not have enough money.")
                continue
            elif bet_amount < MIN_BET:
                print()
                print(f"//// Minimum bet is £{MIN_BET}.")
                print()
                continue
            elif bet_amount > MAX_BET:
                print()
                print(f"//// Maximum bet is £{MAX_BET}.")
                print()
                continue
        else:
            print()
            print("//// Invalid input. Please type only numbers.")
            print()
            continue

        spin_num = random.randint(0, 36)
        b_joined = "'" + "', '".join(b) + "'"
        print(f"You are betting on: {b_joined}.")
        time.sleep(.8)
        print()
        print(".")
        time.sleep(0.5)
        print("..")
        time.sleep(0.5)
        print("...")
        time.sleep(.8)
        plr_win = False
        for i in range(len(b)):
            time.sleep(0.5)
            if int(b[i]) != spin_num:
                num_lost = b[i]
                print()
                print(f"You lost on {num_lost}! ")
                plr_bal -= bet_amount
                continue
            elif int(b[i]) == spin_num:
                print()
                print(f"You won on: {spin_num}! ")
                plr_bal += bet_amount * 36
                plr_win = True
                continue
        time.sleep(0.5)
        print()
        amount_won = bet_amount * 36
        if plr_win:
            print(f"Nice! You won £{amount_won} on number {spin_num}.")
        else:
            print(f"Sorry! You didn't win anything this time, the winning number was: {spin_num}. ")
        print()
        inp = input("Would you like to spin again or go to the Main Menu (Press enter to spin or type 'm' to go to the Main Menu)? "
                    "\n")

        if inp == "":
            print()
            start_game()
        elif inp.lower() == "m":
            print()
            break
        else:
            print("Please enter a valid option.")


start_game()

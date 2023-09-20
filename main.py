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
    bal = amount
    main()
    return amount


def main():
    global bal
    plr_bal = bal
    while True:
        print()
        print(f"Your current balance is: £{plr_bal}")
        num_bet = input("What numbers' would you like to bet on (separated with just one space ' ')? "
                        "\n")
        print()
        b = list(num_bet.split(' '))
        for i in range(len(b)):
            if not b[i].isdecimal():
                print()
                print("//// Invalid input. Please type only numbers.")
                print()
                main()

            elif b[i].isdecimal():
                for index, val in enumerate(b):
                    if int(val) < 0 or int(val) > 36:
                        invalid_num = val
                        print(f"{invalid_num} is not a valid number. Please choose between 0, and 36.")
                        continue
                continue

        #print(b)

        bet_amount = input("How much would you like to bet? £")

        if bet_amount.isdigit():
            print()
            bet_amount = int(bet_amount)
            if len(b) > 1:
                t_bet_amount = bet_amount * len(b)
                #print("t_bet_amount", t_bet_amount)

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
        print()
        print(f"You are betting on, {b}")
        for i in range(len(b)):
            print(b[i])
            if int(b[i]) != spin_num:
                num_lost = b[i]
                print()
                print(f"You lost on {num_lost}! The winning number was: {spin_num}. ")
                plr_bal -= bet_amount
                print()
                continue
            elif int(b[i]) == spin_num:
                print()
                print(f"You won on: {spin_num}! ")
                plr_bal += bet_amount*36
                print()
                continue





start_game()

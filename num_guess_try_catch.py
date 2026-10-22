#!/usr/bin/env python3
# Created By: Victor Victor-Calixte
# Date: 09/16/26
# This program runs basic math.

import random


def main():

    generated_num = random.randint(0, 9)
    num_guess_as_string = input("Please guess a number between 0-9: ")

    try:
        num_guess_as_num = int(num_guess_as_string)

        if num_guess_as_num == generated_num:
            print("You guessed correctly!")
        else:
            print(
                "Your guess was incorrect! Correct number was: {}".format(generated_num)
            )

    except:
        print(
            "({}) Is not a valid value. (MUST BE A NUMBER)".format(num_guess_as_string)
        )

    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()

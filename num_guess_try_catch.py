#!/usr/bin/env python3
# Created By: Victor Victor-Calixte
# Date: 09/16/26
# This program asks the user to guess a number between 0-9. It also supports input failures.

import random

def main():

    # Getting a random generated number and asking the user to guess the number
    generated_num = random.randint(0, 9)
    num_guess_as_string = input("Please guess a number between 0-9: ")

    # the try statement will make sure the code safely with invald user inputs
    try:
        # Converting the guessed number ( string ) -> ( number )
        num_guess_as_num = int(num_guess_as_string)

        # Checking whether or not the user guess correcty.
        if num_guess_as_num == generated_num:
            # If they guessed correctly, then let the user know they guessed correctly
            print("You guessed correctly!")
        else:
            # Otherwise, let them know the correct number
            print(
                "Your guess was incorrect! Correct number was: {}".format(generated_num)
            )
    # If the try statement fails, it was likely due to the input from the user being invalid
    except:
        # Tell the user about the mistake
        print(
            "({}) Is not a valid value. (MUST BE A NUMBER)".format(num_guess_as_string)
        )

    # Dismiss the user
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()

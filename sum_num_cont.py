# !/user/bin/env.python3
# Created By: Daniel Momoh
# Date: Nov. 19, 2022
# This program asks the user how many numbers they want to add together.
# The user will then be input the numbers and the program
# will display the sum of the numbers


def main():
    # Declaring of variables, loop counter and sum
    loop_counter = 0
    sum = 0
    answer = ""
    while True:
        # get user input
        user_input = input("How many numbers would you like to add?: ")
        print("")
        try:
            # converts the first user input to integer
            user_number = int(user_input)
            if user_number == 0:
                print("This is a zero.")
                print("")
            if user_number > 0:
                # calculate the sum of the entered numbers
                while loop_counter < user_number:
                    # gets input from user
                    user_input_b = input("Enter a whole number: ")
                    try:
                        # converts entered number from string to integer
                        user_number_b = int(user_input_b)
                        # joins the inputted numbers together
                        if user_number_b < 0:
                            print("This is < 0 and cannot be added")
                            print("")
                            continue
                        print("{} added to the sum.".format(user_number_b))
                        print("")
                        # calculates the sum of the two numbers
                        sum = sum + user_number_b
                        loop_counter = loop_counter + 1
                        answer += str(user_number_b) + " + "
                    # if user input b is not an integer loop back
                    # to get an integer
                    except Exception:
                        print("{} is not a number.".format(user_input_b))
                        print("")
                        continue
                if loop_counter == user_number:
                    print("{} = {} ".format(answer, sum))
                    print("The sum is {}.".format(sum))
                    break
            # if user input is equal to zero
            # loop back to get user input
            else:
                print("Please enter a whole number!")
                print("")
        # if user input is not an integer loop back
        # to get an integer
        except Exception:
            print("{} is not a number.".format(user_input))
            print("")
    print("Thanks for playing")


if __name__ == "__main__":
    main()

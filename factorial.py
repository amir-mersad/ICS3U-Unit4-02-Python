#!/usr/bin/env python3

# Created by Amir Mersad
# Created on September 2019
# This program asks the user for a positive integer,
#  then multiplies the whole numbers up to that number


def main():
    # This function asks the user for a positive integer,
    #  then multiplies the whole numbers up to that number
    number = input("enter a number: ")
    result = 1
    x = 0
    try:
        number = int(number)
        if number >= 0:
            while x <= number:
                result = x * result
                x += 1
            print(result)
        else:
            print("number should be positive!")
    except(Exception):
        print("Wrong input!!!")


if __name__ == "__main__":
    main()

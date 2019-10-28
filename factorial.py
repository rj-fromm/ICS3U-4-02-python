#!/usr/bin/env python3

# Created by: RJ Fromm
# Created on: Oct 2019
# This program multiplies numbers together


def main():

    number = int(input("Please enter a number : "))

    number1 = number

    counter = 1

    total = 0

    while counter != number1:

        number = number * counter

        counter = counter + 1

        total = number

        print("{0}".format(total))


if __name__ == "__main__":
    main()

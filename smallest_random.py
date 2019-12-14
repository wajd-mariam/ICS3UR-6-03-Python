#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: December 2019
# This program calculates the smallest number in a list.

import random


def smallest_number(random_list):
    # this function returns the largest number
    smallest_random = random_list[0]

    for loop_counter in range(0, len(random_list)):
        if random_list[loop_counter] < smallest_random:
            smallest_random = random_list[loop_counter]

    return smallest_random


def main():
    # this function calculates the average of randomized numbers

    list_random = []

    # input
    print("The randomized numbers are:")
    for loop_counter in range(0, 10):
        random_number = random.randint(1, 100)
        list_random.append(random_number)
        print("{0}, ".format(random_number), end="")
    print("")

    small = smallest_number(list_random)

    print("The smallest number of all numbers is {0}".format(small))


if __name__ == "__main__":
    main()

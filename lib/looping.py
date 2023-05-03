#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while (i >= 1):
        print(f"{i}")
        i -= 1
        if i == 0:
            print("Happy New Year!")
        

square_nums = list()

def square_integers(int_list):
    square_list = [num * num for num in int_list]
    square_nums.append(square_list)
    return square_list 


def fizzbuzz():
    for num in range(101):
        if num % 3 == 0 and num % 5 == 0 and num != 0:
            print("FizzBuzz")
        elif num % 5 == 0 and num != 0:
            print("Buzz")
        elif num % 3 == 0 and num != 0:
            print("Fizz")
        else:
            if num != 0:
                print(num)



# 61
# convert distance ( in feet ) to inches, yards and miles

def convert_feets():
    d = float(input("enter the distance in feets: "))
    d_inches = d * 12
    d_yards = d / 3
    d_miles = d / 5280
    print(f"in inches = {d_inches}, in yards = {d_yards}, in miles = {d_miles}")


convert_feets()

# ========================================================================== #
# 62
# convert all units of time into seconds.
def convert_to_seconds(hours, minutes):
    t_seconds = hours * 60 * 60 + minutes * 60
    print(f"time in seconds = {t_seconds}")


convert_to_seconds(3, 10)
# ====================================================================== #
# 63
# get an absolute file path
import os

print(os.path.abspath('./main.py'))

# ====================================================================== #
# 64
import os
import time

print(time.ctime(os.path.getmtime('./main.py')))  # modification time.
print(time.ctime(os.path.getctime('./main.py')))  # creation time.

# ========================================================== #
# 65
# calculate BMI

def calc_bmi():
    height = float(input("enter height in meters: "))
    weight = float(input("enter weight in kg: "))
    bmi = weight / (height ** 2)
    print(format(bmi, '.2f'))
    # or
    # print(round(bmi, 2))


calc_bmi()
# ===================================================== #
# 68
# calculate the sum of digits of a number.


def sum_digits(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    return total


print(sum_digits(1234))

# ========================================================= #
# 69
# sort three integers without need to conditional statements or loops.

def sort_integers(my_list):
    min_int = min(my_list)
    max_int = max(my_list)
    middle = sum(my_list) - max_int - min_int
    return max_int, middle, min_int


print(sort_integers([10, 5, 3]))
# ================================================== #
# 70
# sort files by date
import os
import glob

# glob == global enables searching for file patterns
files = glob.glob('*.txt')
files.sort(key=os.path.getmtime())
print("\n".join(files))

# ========================================================== #
# 71
# get a directory listing, sorted by date
import glob
import os

os.chdir('./test')
files = os.listdir()
print(files)
files.sort(key=os.path.getctime)
print("\n".join(files))

# ======================================================= #
# 72
# get details of a module
import math

print('\n'.join(dir(math)))

# ================================================================== #
# 73
# get the midpoint of a line

def get_midpoint(x1, x2, y1, y2):
    result = ((x1 + x2) / 2, (y1 + y2) / 2)
    return result


print(get_midpoint(2,3,5, 8))

# ==================================================================== #
# 74
# hash a word
from hashlib import sha256


def hashy():
    _ = input("enter a word to hash in sha256:  ")
    return sha256(_.encode('utf-8')).hexdigest()
    # encode to represent characters as ascii
    # hexdigest is a string object of double length, containing only hexadecimal digits.
    # This may be used to exchange the value safely in email or other non-binary environments.


print(hashy())

# ================================================================== #
# 75
# read and write your copyrights
# to see python copyrights use print(sys.copyright)

__author__ = "Alaa Atwa"
__copyright__ = "copyright (c) 2023 Alaa Atwa"
__licence__ = "Google Domain"
__version__ = "1.9"

print(__copyright__)
print(__version__)

# =================================================================== #
# 76
# get command line arguments, name of the script
import sys

# no. arguments passed
n = len(sys.argv)  # argument variables.

# name of script == sys.argv[0]
script_name = sys.argv[0]

# arguments passed, every argument is an item in argv[] list starting from one
for i in range(1, n):  # starting from one because zero is the script name
    print(sys.argv[i], end=" ")

# or simply print the str(sys.argv)
# ============================================================== #
# 78
# show available builtin functions
help('modules')

# =================================================================== #
# 79
# get size of object
import sys

text = "hello_there"
print(sys.getsizeof(text))

# ============================================================ #
# 80
# get current value of recursion limit.
# recursion is how many times a function can call itself
import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

# ============================================================== #
# 81
# concatenate N strings

def concat_text(text_list):
    final_text = "-".join(text_list)
    print(final_text)


concat_text(['hello', 'there', 'welcome', 'home'])

# ========================================================= #
# 82
# sum of items of a container (tuple, list, ...)

def sum_items(container):
    total = 0
    for item in container:
        total += item
    return total


print(sum_items([1, 2, 3, 4]))
print(sum_items((1, 2, 3, 4)))

# for dictionaries just use keys to iterate for the values of it

# ========================================================================= #
# 83
# test if all numbers in a list are greater than certain number.

def check_list(your_list):
    check = int(input("enter a number to check: "))
    for num in your_list:
        if num <= check:
            return False
    return True


print(check_list([2, 3, 4, 6, 8]))

# or using all method

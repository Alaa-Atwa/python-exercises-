# 34
# sum of two integers, however if the sum is between 15 and 20, the sum will be zero.
# =============================================================================== #
def calc_total(num1, num2):
    total = 0
    if 15 < num1 + num2 < 20:
        return total
    return num1 + num2


print(calc_total(7, 11))
print(calc_total(20, 30))

# =========================================================================== #
# 35
def check(num1, num2):
    if num1 == num2 or abs(num1 - num2) == 5 or num1+num2 == 5:
        return True
    return False


print(check(3, 3))
print(check(15, 10))
print(check(3, 2))
# ================================================================ #
# 36
def add_integers(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        print(num1+num2)
    else:
        print("false type to add to it.")


add_integers(2, 3)
# ==================================================================== #
# 40
# calculate the distance between two points.
import math


def calc_distance(x1, x2, y1, y2):
    h_distance = x2 - x1
    v_distance = y2 - y1
    return math.sqrt(h_distance ** 2 + v_distance ** 2)


print(calc_distance(20, 30, 40, 60))
# ====================================================================== #
# 41

from os import path

print(path.isfile('./main.py'))

# ======================================================================= #
# 49
import os

content = os.system("ls /home/user/Documents")
print(content)

# ========================================================================== #
# 50 
# print without new lines 
for i in range(10):
    print('*', end="")

# ======================================================================== #
# 53
# access environment variables
import os

# get the value of the path env variable
path = os.environ['PATH']
print(path)

# set a new environment variable
os.environ['MY_VAR'] = 'helloworld123'
print(os.environ['MY_VAR'])

# to avoid key errors if the var is not found use os.environ.get('MY_VAR')
# the output wille be none.

# ============================================================================ #
# 54
# get current username
import os

print(os.environ.get('USER'))

# ============================================================================ #
# 55
# show local ip address
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()

# ====================================================================== #
# 57
# get execution time by a program

import time

start = time.time()

for i in range(20**30):
    print("*")

end = time.time()
full_time = end - start
print(full_time)

# or with formatted time:
print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(full_time)))

# U can also use timeit module

# ======================================================================= #
# 58
# sum of the first n positive numbers

limit = int(input("enter a positive number: "))
total = 0
i = 0
while i <= limit:
    total += i
    i += 1

print(total)
# or using the formula of n * ( n + 1 ) / 2
# print(limit * (limit + 1) / 2)

# =================================================================== #
# 59
# convert feet to meters and centimeters
def convert_to_meter():
    d = float(input("enter the distance in feet: "))
    d_meters = round(d * 0.3048)
    d_centi = round(d_meters * 100)
    print(f"distance in meters {d_meters} , and in centimeters is {d_centi}")


convert_to_meter()

# ========================================================================= #
# 60
# find the hypotenuse of a right-angled triangle.
import math


def find_hypo(arm, feet):
    hypo_squared = arm ** 2 + feet ** 2
    hypo = math.sqrt(hypo_squared)
    print(hypo)


find_hypo(6, 8)

# ============================================================================= #

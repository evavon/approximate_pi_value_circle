#the goal of the project is to estimate pi value without using the function math.pi.
#Theory: Assuming that you throw 18,000 balls into a square of 2 feet by 2 feet. The maximum circle inside the square has radius 
#equal to 1. Assuming that 18,000 balls has the same probability to fall into inside the circle or outside the circle within
#the square. At the end, we are going to calculate number of balls inside the circle divided by 18,000 to get the approximate 
#value of pi

import random as rd
import math


inside_circle = 0
outside_circle = 0
n = 18000

for i in range(0,n):
    x = rd.random ()
    y = rd.random ()
    if math.sqrt(x*x + y*y) <= 1:
        inside_circle = inside_circle + 1
    else:
        outside_circle = outside_circle + 1
pi_value = 4*inside_circle/n
print (pi_value*1.00000)
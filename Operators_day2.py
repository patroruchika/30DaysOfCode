import math
import os
import random
import re
import sys

# Complete the solve function below.
mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())

def solve(a, b, c):
    a = mealCost
    b = tipPercent 
    c = taxPercent

    tip_cost = (b/100.)* a
    tax_cost = (c/100.)* a
    totalCost = int(round(a + tip_cost + tax_cost))
    print(totalCost)

solve(mealCost, tipPercent, taxPercent)

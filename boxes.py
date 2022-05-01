"""
A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping.
Write a Python program named boxes.py that asks the user for two integers:

the number of manufactured items
the number of items that the user will pack per box

Your program must compute and print the number of boxes necessary to hold the items.
This must be a whole number. Note that the last box may be packed with fewer items than the other boxes.
"""

from decimal import ROUND_UP
from importlib.machinery import BYTECODE_SUFFIXES
import math

items = int(input("\nEnter the number of items: "))
perBox = int(input("Enter the number of items per box: "))

boxes = math.ceil(items/perBox)

print(f"\nFor {items} items, packing {perBox} items in each box, you will need {boxes} boxes.\n")
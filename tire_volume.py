from datetime import datetime
import math

width = int(input("Enter the width of the tire in mm (ex 205): "))
ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi*width**2*ratio*(width*ratio+2540*diameter))/10000000000

date = datetime.now()

with open('volumes.txt', mode="at") as log:
    print(f"{date:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f}", file=log)


print(f"\nThe aproximate volume is {volume:.2f} liters\n")
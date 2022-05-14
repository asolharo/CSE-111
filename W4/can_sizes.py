# Import the standard math module so that
# math.pi can be used in this program.
import math
import csv

def main():
    with open('cans.csv', newline='') as csvfile:
        cans = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in cans:
            if row[0] == '#1 Picnic':
                print (row[1])

def compute_volume(radius,height):
    #Compute and return the volumen
    #Parameters:
        #radius: the radius of the cylinder
        #height: the height of the cylinder
    volume = math.pi *radius**2 * height
    return volume

def compute_surface_area(radius,height):
    #Compute and return the surface area
    #Parameters:
        #radius: the radius of the cylinder
        #height: the height of the cylinder
   surface_area =  2*math.pi *radius*(radius+height)
   return surface_area

#start this program
#calling the main functionsx
main()
# Shin Yamagami
# Oct 15th, 2015
#
# This program calculate the kinetic energy of a moving object from
# a distance and mass inputted by a user.

# explain what this program will do
def print_description():
    print('This program calculate the kinetic energy of a moving object from\n'
          'a distance and mass inputted by a user.')
    
# get feet as a float from a user
def get_feet():
    return float(input('Please input how high the moving object is in feet?: '))

# get pound as a float from a user
def get_pound():
    return float(input('Please input how heavy the moving object is in pound?: '))

# convert feet to meter
def meter_from_feet(feet):
    meter = feet * 0.3048
    return meter

# print the meter
def print_meter(meter):
    print('It is', format(meter,'.2f'),'meters.')
    
# convert pound to kg
def kg_from_pound(pound):
    kg = pound * 0.453592
    return kg

# print the kg
def print_kg(kg):
    print('It is', format(kg,'.2f'),'kg.')
    
# calculate a time from the meter and gravity and print it
def time_from_meter(meter):
    g = 9.8
    time = (meter * 2 / g)**(1/2)
    return time

# print the time
def print_time(time):
    print('It takes', format(time,'.4f'),'seconds to the ground.')
    
# calculate an energy from the kg, the meter and the time and print it
def kinetic_energy(kg, meter, time):
    energy = (1/2) * kg * (meter / time)**2
    return energy

def print_energy(energy):
    print('The energy is', format(energy,'.2f'),'.')
    
def main():
    # first, print the description of this program
    print_description()
    
    # get the feet as a float and assign it to 'feet'
    feet = get_feet()
    
    # get the pound as a float and assign it to 'pound'
    pound = get_pound()
    
    # convert feet to meter and assign it to 'meter'
    meter = meter_from_feet(feet)
    
    # print the meter
    print_meter(meter)
    
    # convert pound to kg and assign it to 'kg'
    kg = kg_from_pound(pound)
    
    # print the kg
    print_kg(kg)
    # calculate a time from the meter and gravity and assign it to 'time'
    time = time_from_meter(meter)
    
    # print the time
    print_time(time)
    
    # calculate an energy from the kg, the meter and the time and assign it to 'energy'
    energy = kinetic_energy(kg, meter, time)
    
    # print the energy
    print_energy(energy)
    
main()




"""

# Oct 14th, 2015
# This program calculate the kinetic energy from a distance in feet and
# a mass in pound inputted by a user.

# print the description what this program will do.
print('This program calculate the kinetic energy from a distance in feet and\n'
      'a mass in pound inputted by a user.')

# get a distance in feet from a user
feet = float(input('Please input how high it is in feet?: '))
# get a mass in pound from a user
pound = float(input('Please input how heavy it is in pound?: '))
# set variables after changing units or calculating variables
meter = feet * 0.3048

kg = pound * 0.453592

g = 9.8

time = (meter * 2 / g)**(1/2)

energy = (1/2) * kg * (meter / time)**2

# Create the main function to aggregate 
def main():

    meter_from_feet(meter)

    kg_from_pound(kg)

    time_from_meter(time)
    
    kinetic_energy(energy)

def meter_from_feet(meter):
    print('It is', format(meter,'.2f'),'meters high.')

def kg_from_pound(kg):
    print('It is', format(kg,'.2f'),'kg.')

def time_from_meter(time):
    print('It takes', format(time,'.4f'),'seconds.')
    
def kinetic_energy(energy):
    print('The energy is', format(energy,'.2f'),'.')

main()
"""

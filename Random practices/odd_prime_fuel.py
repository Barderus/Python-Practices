'''
LOCATION:  0    FUEL:  7.000000
2.125 FUEL BURNED
LOCATION:  1    FUEL:  4.875000
2.125 FUEL BURNED
LOCATION:  2    FUEL:  2.750000
2.125 FUEL BURNED
3 FUEL ADDED AT ODD PRIME MILE MARKER
LOCATION:  3    FUEL:  3.625000
2.125 FUEL BURNED
LOCATION:  4    FUEL:  1.500000
FINAL STRANDED LOCATION:  4.7058824

Requirements:
Starts at mile 0
2.125 units of fuel per mile
Odd numbers: add n amount of fuel being n the odd number

'''
# Constants
mile = 0
fuel = 8.375
FUEL_PER_MILE = 2.125

# Function to check if a number is an odd prime number
def isPrime(n):
    if n <= 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# While the fuel is greater than the fuel per mile
# add 1 to the mile and subtract the fuel per mile
# print the mile and fuel
# if the mile is an odd prime number add the mile to the fuel
while fuel >= FUEL_PER_MILE:
    mile += 1
    fuel -= FUEL_PER_MILE
    print(f"Mile: {mile}\tFuel: {fuel}")
    if isPrime(mile):
        fuel += mile
        print(f"FUEL ADDED AT MILE{mile} (ODD PRIME MILE MARKER)")

# Display the final results if the golf cart got stranded
print(f"You drove {mile} miles and have left {fuel} units of fuel")
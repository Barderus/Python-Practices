import random

def recursive_add(num, n):
    """
    Recursively multiplies the given value by 2 for 'n' times.

    Returns the result of the recursive multiplication.
    """
    if n == 0:
        return num
    else:
        return recursive_add(num + num, n - 1)

def main():
    """
    Generates a list of random numbers, multiplies each number, and prints the results.

    The program prints the input numbers and their corresponding multiplied results.
    """
    num_list = [random.randrange(1, 10) for n in range(5)]
    print(f"> {'In':<10}\t{'< Out'}")

    for i in range(len(num_list)):
        number = num_list[i]
        result = recursive_add(number, 4)
        result1 = recursive_add(number, 3)
        print(f"  {num_list[i]:<10}\t  {result + result1}")

if __name__ == "__main__":
    main()

# 1. Import the numpy package under the name `np` (★☆☆)
import numpy as np

# 2. Print the numpy version and the configuration (★☆☆)
print(f"Numpy version: {np.__version__}\nNumpy configuration: {np.show_config()}")

# 3. Create a null vector of size 10 (★☆☆)
arr = np.zeros(10)
print(arr)
# 4. How to find the memory size of any array (★☆☆)
print(f"Memory size of the arr array: {arr.itemsize} bytes")

# 5. How to get the documentation of the numpy add function from the command line? (★☆☆)
print(f"\nNumpy add function information: {np.info(np.add)}")

# 6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
arr[4] = 1
print(f"\nNull array with the 5th element a 1: {arr}")

# 7. Create a vector with values ranging from 10 to 49 (★☆☆)
arr_range = np.arange(10, 50)
print(f"Array ranging from 10 to 49: {arr_range}")

# 8. Reverse a vector (first element becomes last) (★☆☆)
reversed_arr = np.flip(arr_range)
print(print(f"\nReversed array: {reversed_arr}"))

# 9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
arr_matrix = np.arange(0, 9).reshape(3, 3)
print(f"\nArray matrix: {arr_matrix}")

# 10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
array_el = np.array([1, 2, 0, 0, 4, 0])
non_zero_indices = np.nonzero(array_el)[0]
print("\nNon-zero elements indices:", non_zero_indices)

# 11. Create a 3x3 identity matrix (★☆☆)
identity_matrix = np.identity(3)
print(f"\nIdentity matrix: {identity_matrix}")

# 12. Create a 3x3x3 array with random values (★☆☆)
random_arr = np.random.randint(1, 101, size=(3, 3, 3))
print(f"\nRandom array: {random_arr}")

# 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)

# 14. Create a random vector of size 30 and find the mean value (★☆☆)

# 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)

# 16. How to add a border (filled with 0's) around an existing array? (★☆☆)

# 17. What is the result of the following expression? (★☆☆)
"""
    0 * np.nan
    np.nan == np.nan
    np.inf > np.nan
    np.nan - np.nan
    np.nan in set([np.nan])
    0.3 == 3 * 0.1
"""

# 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)

# 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)

# 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element? (★☆☆)

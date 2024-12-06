from typing import List
import re
import numpy as np

# Read the file
with open("in.txt") as infile:
    content = infile.read()
    content_list = content.split("\n")

# Create the matrix
matrix = [list(line) for line in content_list]
numpy_matrix = np.array(matrix)

# Rotate NumPy matrix 90 degrees
rotated_matrix = np.rot90(numpy_matrix)


def get_all_diagonals(arr):
    rows, cols = arr.shape

    all_diagonals = []

    # Main diagonals
    for k in range(-(rows - 1), rows):
        diag = np.diag(arr, k)
        all_diagonals.append(diag)

    # Opposite diagonals
    flipped_matrix = np.fliplr(arr)
    for k in range(-(rows - 1), rows):
        diag = np.diag(flipped_matrix, k)
        all_diagonals.append(diag)
    return all_diagonals


# Function to accumulate diagonals to string
def diagonals_to_string(diagonals):
    acc = ""
    for diag in diagonals:
        acc += " " + "".join(diag)
    return acc


# Get diagonals for original and rotated matrices
original_diagonals = get_all_diagonals(numpy_matrix)

# Convert to strings
normal_str = " ".join(content_list)
original_diag_str = diagonals_to_string(original_diagonals)
rotated_diag_str = diagonals_to_string(rotated_matrix)


# Correct regex for finding XMAS and SAMX
def find_occurrences(s, word):
    return len(re.findall(word, s, re.IGNORECASE))


# Calculate total occurrences
xmas_total = (
        find_occurrences(normal_str, 'XMAS') +
        find_occurrences(original_diag_str, 'XMAS') +
        find_occurrences(rotated_diag_str, 'XMAS')
)

samx_total = (
        find_occurrences(normal_str, 'SAMX') +
        find_occurrences(original_diag_str, 'SAMX') +
        find_occurrences(rotated_diag_str, 'SAMX')
)

# Print total occurrences
print(f"Total XMAS: {xmas_total}")
print(f"Total SAMX: {samx_total}")
print(f"Ex 1: {samx_total+xmas_total}")


print("Part 2 -----------------")

big = matrix

def find_crossmans_occurances_in_bigger_matrix(big):
    xmas_counter = 0
    for i in range(len(big)):
        for j in range(len(big[0])):
            # dirty but i dont wanna anymore
            try:
                if big[i][j] == "M" and big[i][j+2] == "S" and big[i+2][j]== "M" and big[i+2][j+2] == "S" and big[i+1][j+1] == "A" or \
                    big[i][j] == "S" and big[i][j + 2] == "S" and big[i + 2][j] == "M" and big[i + 2][j + 2] == "M" and big[i + 1][j + 1] == "A" or \
                    big[i][j] == "S" and big[i][j + 2] == "M" and big[i + 2][j] == "S" and big[i + 2][j + 2] == "M" and big[i + 1][j + 1] == "A" or \
                    big[i][j] == "M" and big[i][j + 2] == "M" and big[i + 2][j] == "S" and big[i + 2][j + 2] == "S" and  big[i + 1][j + 1] == "A":
                    xmas_counter = xmas_counter +1
            except Exception as e:
                print(e)
    return  xmas_counter

print("Ex 2:" + find_crossmans_occurances_in_bigger_matrix(big))



# Assessment 3.7: Sorting Algorithms
# Name: RENZ RYAN LAREÑO
# Sorting Method: Bubble Sort

# Full Name
name = "RENZ RYAN LAREÑO"

# Remove spaces and duplicate letters
unsorted_array = []

for letter in name.upper():
    if letter != " " and letter not in unsorted_array:
        unsorted_array.append(letter)

# Display Unsorted Array
print("Full Name:", name)
print("\nUnsorted Array:")
print(unsorted_array)


# Bubble Sort
# Spanish alphabetical order (Ñ after N)
alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

sorted_array = unsorted_array.copy()

n = len(sorted_array)

for i in range(n):
    for j in range(0, n - i - 1):

        if alphabet.index(sorted_array[j]) > alphabet.index(sorted_array[j + 1]):
            # Swap letters
            sorted_array[j], sorted_array[j + 1] = (
                sorted_array[j + 1],
                sorted_array[j]
            )


# Display Sorted Array
print("\nSorted Array:")
print(sorted_array)

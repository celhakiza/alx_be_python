# pattern_drawing.py
# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# initialize the value for i
i = 0
while i < size:
    # Use a for loop to print asterisks in each row
    for j in range(size):
        print("*", end="")
    # Move to the next line after printing a row
    print()
    i += 1
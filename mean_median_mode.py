# An App to find mean , median , mode in python
# ===========================================================================
# Mean
numbers = [10,20,30,40,50]
mean    = sum(numbers) / len(numbers) 
print(f"mean \t= {mean}")
# ===========================================================================
# Median 
numbers2 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

# Sorting the list in ascending order
numbers2.sort()

# Checking if the length of the list is even
if len(numbers2) % 2 == 0:
    # If the length is even, finding the middle two elements
    n1 = numbers2[len(numbers2) // 2]
    n2 = numbers2[len(numbers2) // 2 - 1]
    # Calculating the median as the average of the two middle elements
    median = (n1 + n2) / 2
else:
    # If the length is odd, the median is the middle element
    median = numbers2[len(numbers2) // 2]

# Printing the calculated median
print(f"median  = {median}")
# ===========================================================================
# Mode
numbers3 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

# Creating a dictionary to store frequencies of each element
frequency = {}

# Counting the frequency of each element
for i in numbers3:
    frequency[i] = frequency.get(i, 0) + 1

# Finding the maximum frequency
max_frequency = max(frequency.values())

# Finding the mode (the element with the highest frequency)
for num, freq in frequency.items():
    if freq == max_frequency:
        mode = num

# Printing the mode
print(f"mode \t= {mode}")
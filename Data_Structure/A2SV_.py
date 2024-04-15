class ThreadletEqualizer:
    def make_threadlets_equal_length(self, a, b, c):
        # Check if all threadlets are already of equal length
        if a == b == c:
            return "YES"

        # Sort the lengths of the threadlets in ascending order
        lengths = sorted([a, b, c])

        # Check if it is possible to make all threadlets of equal length
        if lengths[0] + lengths[1] == lengths[2] or lengths[0] + lengths[2] == lengths[1]:
            return "YES"
        elif lengths[0] + lengths[1] + lengths[2] == lengths[0] * 3:
            return "YES"
        elif lengths[0] * 2 + lengths[1] == lengths[2]:
            return "YES"
        else:
            return "NO"

# Create an instance of the ThreadletEqualizer class
equalizer = ThreadletEqualizer()

# Provided input
input_data = [
    [1, 3, 2],
    [5, 5, 5],
    [6, 36, 12],
    [7, 8, 7],
    [6, 3, 3],
    [4, 4, 12],
    [12, 6, 8],
    [1000000000, 1000000000, 1000000000],
    [3, 7, 1],
    [9, 9, 1],
    [9, 3, 6],
    [2, 8, 2],
    [5, 3, 10],
    [8, 4, 8],
    [2, 8, 4]
]

# Iterate through each test case
for test_case in input_data:
    # Read the lengths of the threadlets
    a, b, c = test_case

    # Call the function to check if it is possible to make all threadlets of equal length
    result = equalizer.make_threadlets_equal_length(a, b, c)

    # Print the result
    print(result)
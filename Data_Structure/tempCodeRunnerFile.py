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

# Test case
a, b, c = 5, 5, 5
result = equalizer.make_threadlets_equal_length(a, b, c)
print(result)
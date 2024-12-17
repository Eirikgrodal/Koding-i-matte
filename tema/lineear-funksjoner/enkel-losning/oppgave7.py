length_1 = 100
length_2 = length_1 * 0.9
length_3 = length_2 * 0.9
length_4 = length_3 * 0.9

sum_of_lengths_4 = length_1 + length_2 + length_3 + length_4

length_10 = length_1 * (0.9 ** 9)

sum_of_lengths_10 = length_1 * ((1 - (0.9 ** 10)) / (1 - 0.9))

total_length = 0
num_segments = 0
while total_length < 900:
    num_segments += 1
    total_length += length_1 * (0.9 ** (num_segments - 1))

print("Length of line segment 3:", length_3)
print("Length of line segment 4:", length_4)
print("Sum of lengths of the first four line segments:", sum_of_lengths_4)
print("Length of line segment 10:", length_10)
print("Sum of lengths of the first ten line segments:", sum_of_lengths_10)
print("Number of line segments needed for a total length of at least 9m:", num_segments)
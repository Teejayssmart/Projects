# from collections import Counter
#
# # Provided data (as a list of lists)
# data = [
#     [19, 28, 24, 39, 32],
#     [29, 38, 31, 34, 18],
#     [3, 35, 12, 43, 13],
#     [10, 19, 2, 8, 24],
#     [1, 17, 39, 30, 3],
#     [24, 9, 31, 1, 36],
#     [26, 7, 23, 9, 10],
#     [44, 14, 22, 5, 33],
#     [24, 15, 37, 18, 9],
#     [43, 39, 47, 12, 15],
#     [45, 37, 11, 29, 2],
#     [38, 19, 8, 32, 15],
#     [17, 32, 12, 27, 43],
#     [3, 32, 34, 15, 28],
#     [18, 7, 13, 20, 31],
#     [23, 17, 22, 18, 29],
#     [35, 43, 33, 34, 22],
#     [14, 36, 21, 6, 24],
#     [41, 32, 33, 27, 47],
#     [30, 43, 18, 12, 35],
#     [46, 30, 6, 5, 47],
#     [17, 13, 12, 30, 15],
#     [4, 1, 39, 38, 23],
#     [32, 4, 6, 45, 35],
#     [23, 5, 32, 44, 3],
#     [9, 3, 31, 21, 22],
#     [8, 43, 4, 25, 21],
#     [37, 41, 33, 29, 2],
#     [33, 39, 15, 30, 32],
#     [33, 43, 35, 42, 23],
#     [11, 25, 34, 47, 26],
#     [42, 46, 43, 27, 20],
#     [40, 6, 17, 10, 24],
#     [31, 38, 23, 47, 8],
#     [2, 6, 34, 18, 24],
#     [8, 6, 24, 11, 45],
#     [33, 7, 25, 20, 30],
#     [32, 3, 26, 1, 9],
#     [27, 7, 5, 46, 38],
#     [10, 47, 2, 29, 6],
#     [21, 11, 15, 7, 32],
#     [45, 35, 44, 11, 34],
#     [19, 34, 5, 14, 10],
#     [4, 8, 34, 19, 6],
#     [33, 15, 32, 27, 8],
#     [32, 33, 45, 43, 20],
#     [27, 24, 38, 18, 10],
#     [22, 41, 23, 36, 6],
#     [10, 38, 19, 24, 16],
#     [32, 31, 42, 28, 30],
#     [31, 29, 24, 3, 41]
#
# ]

# Flatten the list of lists into a single list of numbers
flattened_data = [num for sublist in data for num in sublist]

# Count the frequency of each number using Counter
counter = Counter(flattened_data)

# Display the frequency of each number
for num, count in counter.items():
    print(f"Number {num} appears {count} times.")

    from collections import Counter

    # Provided data (as a list of numbers)
    data = [
        9, 1, 1, 9, 5, 8, 1, 5, 7, 5, 6, 9, 3, 5, 8, 7, 10, 1, 4, 6, 5, 10,
        3, 6, 8, 10, 9, 9, 4, 6, 8, 9, 8, 9, 2, 2, 3, 1, 8, 3, 6, 10, 8,
        9, 5, 10, 5, 6, 3, 10, 6
    ]

    # Count the frequency of each number using Counter
    counter = Counter(data)

    # Display the frequency of each number
    for num, count in counter.items():
        print(f"Number {num} appears {count} times.")
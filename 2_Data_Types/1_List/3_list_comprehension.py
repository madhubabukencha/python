# [expression for member in iterable (if conditional)]
even_num = [x for x in range(20) if x % 2 == 0]
print(even_num)

# [expression (if conditional) for member in iterable]
data = ["name_jame", "name_tagore", "tagore", "lovely", "name_king"]
names = [name if name.startswith("name") else 0 for name in data]
print(names)

# Nested if
filtered_list = [x for x in range(50) if x % 2 == 0 if x % 5 == 0]
print(filtered_list)

# Nested comprehension
matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
transpose_matrix = [[row[i] for row in matrix] for i in range(2)]
print(transpose_matrix)

# print number which are only divisible by either 5 and 7
answer = [num for num in range(1, 100)
          if all([True if (num%divisor)==0 else False for divisor in [7, 5]])]
print(answer)

# You can keep as many for loops as you can like this
colours = ["red", "green", "yellow", "blue"]
things = ["house", "car", "tree"]
coloured_things = [(x, y) for x in colours for y in things]
print(coloured_things)
# Which is equivalent to
# for x in colours:
#    for y in things:
#       print(x, y)

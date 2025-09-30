def create_empty_square(n):
    return [[0 for _ in range(n)] for _ in range(n)]

def place_number(square, num, i, j):
    square[i][j] = num

def next_position(i, j, n):
    # Move up and right
    i -= 1
    j += 1
    # Wrap around
    if i < 0:
        i = n - 1
    if j >= n:
        j = 0
    return i, j

def handle_divisible_case(i, j, n):
    # Move down 2 rows and left 1 column
    i += 2
    j -= 1
    # Wrap around
    if i >= n:
        i = i % n
    if j < 0:
        j = n - 1
    return i, j

def magic_square(n):
    if n % 2 == 0:
        print("Magic square works only for odd n!")
        return None

    square = create_empty_square(n)
    i, j = 0, n // 2  # Start top-middle

    for num in range(1, n * n + 1):
        place_number(square, num, i, j)
        if num % n == 0:
            i, j = handle_divisible_case(i, j, n)
        else:
            i, j = next_position(i, j, n)

    return square

def print_square(square):
    for row in square:
        print(row)

# PROGRAM
n = 3
result = magic_square(n)
if result:
    print("Magic Square of size", n, "is:")
    print_square(result)



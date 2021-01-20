

def count_binary_ones(n):
    binary_repr = bin(n)[2:]
    one_count = biggest_one_count = 0
    for digit in binary_repr:
        digit = int(digit)
        if digit == 1:
            one_count += 1
        if one_count > biggest_one_count:
            biggest_one_count = one_count
        if digit == 0:
            one_count = 0
    return biggest_one_count


if __name__ == '__main__':
    n = int(input())
    print(count_binary_ones(n))

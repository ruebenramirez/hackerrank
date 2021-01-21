def print_hour_glass(arr, row, cursor):
    tl = str(arr[row][cursor])
    tm = str(arr[row][cursor+1])
    tr = str(arr[row][cursor+2])
    m = str(arr[row+1][cursor+1])
    bl = str(arr[row+2][cursor])
    bm = str(arr[row+2][cursor+1])
    br = str(arr[row+2][cursor+2])

    print('{l} {m} {r}'.format(l=tl, m=tm, r=tr))
    print('{l} {m} {r}'.format(l=' ', m=m, r=' '))
    print('{l} {m} {r}'.format(l=bl, m=bm, r=br))


def sum_hour_glass(arr, row, cursor):
    top_sum = \
        arr[row][cursor] + arr[row][cursor+1] + arr[row][cursor+2]
    middle = arr[row+1][cursor+1]
    bottom_sum = \
        arr[row+2][cursor] + arr[row+2][cursor+1] + arr[row+2][cursor+2]
    total = top_sum + middle + bottom_sum
    return total


def biggest_hourglass(arr):
    hour_glass_len = len(arr) - 2
    max_hour_glass_sum = hour_glass_sum = max_row = max_cursor = None
    # process through rows:
    for row in range(hour_glass_len):
        hour_glass_width = len(arr[row]) - 2
        # process through columns:
        for cursor in range(hour_glass_width):
            hour_glass_sum = sum_hour_glass(arr, row, cursor)
            if max_hour_glass_sum is None or \
                    hour_glass_sum > max_hour_glass_sum:
                max_hour_glass_sum = hour_glass_sum
                max_row = row
                max_cursor = cursor
    print('Biggest Hour Glass: {c}'.format(c=max_hour_glass_sum))
    print_hour_glass(arr, max_row, max_cursor)


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    biggest_hourglass(arr)

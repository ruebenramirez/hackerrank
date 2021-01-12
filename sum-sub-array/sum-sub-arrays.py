

"""
input
-----
3
5
10
10
1
3
1 2 5

expected output
---------------
15


how to solve
------------

1) read in the array

2) iterate through queries

3) create sub-arrays

4) sum the sub arrays

5) substitute 0's with the zero replacement value

6) print out the sub array sum

"""


def sum_queries(numbers, queries):
    query_sums = []
    for query in queries:
        left = query[0] - 1
        right = query[1]
        zero_replacement = query[2]
        sub_numbers = numbers[left:right]
        query_sum = 0
        for num in sub_numbers:
            if num != 0:
                query_sum += num
            else:
                query_sum += zero_replacement
        query_sums.append(query_sum)
    return query_sums


numbers = [5, 10, 10]
queries = [[1, 2, 5]]
print(sum_queries(numbers, queries))

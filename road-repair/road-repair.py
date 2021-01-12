#!/bin/python3

import os

#
# Complete the 'getMinCost' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY crew_id
#  2. INTEGER_ARRAY job_id
#


def getMinCost(crew_id, job_id):
    """ cost of routing crews to job sites

    cost = difference between matching indexes in arrays"""
    cost = 0
    crew_id.sort()
    job_id.sort()
    job_count = len(job_id)
    for i in range(0, job_count):
        if crew_id[i] != job_id[i]:
            cost += abs(job_id[i] - crew_id[i])
    return cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crew_id_count = int(input().strip())
    crew_id = []
    for _ in range(crew_id_count):
        crew_id_item = int(input().strip())
        crew_id.append(crew_id_item)

    job_id_count = int(input().strip())
    job_id = []
    for _ in range(job_id_count):
        job_id_item = int(input().strip())
        job_id.append(job_id_item)

    result = getMinCost(crew_id, job_id)
    fptr.write(str(result) + '\n')
    fptr.close()


"""
input:
5
5
3
1
4
6
5
9
8
3
15
1

expected output:
17



how to work it

1) find workers already onsite

5
-3-
-1-
4
6

9
8
-3-
15
-1-


so we just have these left

5
4
6

9
8
15

2) we should sort these next

4, 5, 6
8, 9, 15

3) we just count into places next
4 = 8-4
4 = 9-5
9 = 15-6

total: 17 = 9 + 4 + 4


"""

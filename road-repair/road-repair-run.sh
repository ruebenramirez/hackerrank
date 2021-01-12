#!/bin/bash
export OUTPUT_PATH="stdout"
rm -f $OUTPUT_PATH
echo "5
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
" | python3 road-repair.py

cat $OUTPUT_PATH
rm -f $OUTPUT_PATH

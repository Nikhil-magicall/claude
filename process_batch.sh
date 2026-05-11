#!/bin/bash
# Usage: process_batch.sh START END
START=$1
END=$2
OUTFILE="/home/user/claude/rem_part_1.csv"
INFILE="/home/user/claude/rem_slice_1.txt"

domains=$(sed -n "${START},${END}p" "$INFILE")
echo "$domains"

#!/usr/bin/env bash

YEAR="$1"
DAY="$2"

CACHE_DIR="${XDG_CACHE_HOME:-$HOME/.cache}/aoc"
OUTPUT_FILE="$CACHE_DIR/$YEAR-day$DAY-input.txt"

aoc-request "$YEAR/day/$DAY/input" "$OUTPUT_FILE"

cat "$OUTPUT_FILE"

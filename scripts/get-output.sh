#!/usr/bin/env bash

YEAR="$1"
DAY="$2"

CACHE_DIR="${XDG_CACHE_HOME:-$HOME/.cache}/aoc"
OUTPUT_FILE="$CACHE_DIR/$YEAR-day$DAY-output.txt"
TMP_FILE="/tmp/aoc-$YEAR-day$DAY-output.html"

if [ ! -f "$OUTPUT_FILE" ]; then
    aoc-request "$YEAR/day/$DAY" "$TMP_FILE"

    rg --only-matching --pcre2 '(?<=Your puzzle answer was <code>).*?(?=</code>)' "$TMP_FILE" > "$OUTPUT_FILE"

    rm -f "$TMP_FILE"
fi

cat "$OUTPUT_FILE"

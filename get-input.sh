#!/usr/bin/env bash

YEAR="$1"
DAY="$2"

CACHE_DIR="${XDG_CACHE_HOME:-$HOME/.cache}/aoc"
mkdir -p "$CACHE_DIR"
SESSION_FILE="$CACHE_DIR/session"
OUTPUT_FILE="$CACHE_DIR/$YEAR/day$DAY"

while [ ! -f "$OUTPUT_FILE" ]; do
    if [ ! -f "$SESSION_FILE" ]; then
        echo -n "Please enter your session cookie: " >&2
        read -r SESSION
        echo "$SESSION" > "$SESSION_FILE"
    fi

    if ! curl "https://adventofcode.com/$YEAR/day/$DAY/input" -sf -H "Cookie: session=$(cat "$SESSION_FILE")" -o "$OUTPUT_FILE"; then
        echo "Invalid session cookie" >&2
        rm -f "$SESSION_FILE" "$OUTPUT_FILE"
    fi
done

cat "$OUTPUT_FILE"

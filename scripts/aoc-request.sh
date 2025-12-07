#!/usr/bin/env bash

REQUEST_PATH="$1"
OUTPUT_FILE="$2"

CACHE_DIR="${XDG_CACHE_HOME:-$HOME/.cache}/aoc"
mkdir -p "$CACHE_DIR"
SESSION_FILE="$CACHE_DIR/session"

while [ ! -f "$OUTPUT_FILE" ]; do
    if [ ! -f "$SESSION_FILE" ]; then
        echo -n "Please enter your session cookie: " >&2
        read -r SESSION
        echo "$SESSION" > "$SESSION_FILE"
    fi

    if ! curl "https://adventofcode.com/$REQUEST_PATH" -sf -H "Cookie: session=$(cat "$SESSION_FILE")" -o "$OUTPUT_FILE"; then
        echo "Invalid session cookie" >&2
        rm -f "$SESSION_FILE" "$OUTPUT_FILE"
    fi
done

#!/bin/bash

HISTORY_FILE_ZSH="$HOME/.zsh_history"
HISTORY_FILE_BASH="$HOME/.bash_history"
OUTPUT_DIR="history_dumps" 
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
OUTPUT_PATH="$OUTPUT_DIR/history_$TIMESTAMP.txt"

mkdir -p $OUTPUT_PATH

if [ -f "$HISTORY_FILE_ZSH" ]; then
    cp "$HISTORY_FILE_ZSH" "$OUTPUT_PATH"
    echo "🟢 History is preserved to $OUTPUT_PATH"
else
    echo "🔴 History file was not found"
fi 

if [ -f "$HISTORY_FILE_BASH" ]; then
    cp "$HISTORY_FILE_BASH" "$OUTPUT_PATH"
    echo "🟢 History is preserved to $OUTPUT_PATH"
else
    echo "🔴 History file was not found"
fi 
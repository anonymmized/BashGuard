#!/bin/bash

SHELL_NAME=$(basename "$SHELL")
if [ "$SHELL_NAME" = "zsh" ]; then
    RC_FILE="$HOME/.zshrc"
elif [ "SHELL_NAME" = "bash" ]; then
    RC_FILE="$HOME/.bashrc"
else
    echo "Unknown shell: $SHELL"
    exit 1
fi 

if ! grep -q 'export PATH="$HOME/.local/bin:$PATH"' "$RC_FILE"; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$RC_FILE"
    echo "Added to $RC_FILE"
else
    echo "File already in $RC_FILE"
fi

source "$RC_FILE"

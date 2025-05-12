#!/bin/bash

echo "🔍 Check which version of pip is available ..."

if command -v pip3 &> /dev/null; then
    echo "📦 Found pip3"
    PYTHON_CMD="pip3"
elif command -v pip &> /dev/null; then
    echo "📦 Found pip"
    PYTHON_CMD="pip"
else
    echo "🔴 pip is not installed. Install Python and PIP before continuing" 
    exit 1
fi

echo "🚀 We use: $PYTHON_CMD"

$PYTHON_CMD install colorama

echo "🟢 The installation is completed" 

#!/bin/bash
set -e

# Read input file, process word frequencies, and output top 10 words
python3 << 'EOF'
import re
from collections import Counter

# Read the input file
with open('/app/input.txt', 'r') as f:
    text = f.read()

# Convert to lowercase
text = text.lower()

# Extract words (only alphabetic characters)
words = re.findall(r'[a-z]+', text)

# Count word frequencies
word_counts = Counter(words)

# Get top 10 most common words
top_10 = word_counts.most_common(10)

# Write output (only the words, one per line)
with open('/app/output.txt', 'w') as f:
    for word, count in top_10:
        f.write(f"{word}\n")

print("Word frequency analysis complete!")
EOF

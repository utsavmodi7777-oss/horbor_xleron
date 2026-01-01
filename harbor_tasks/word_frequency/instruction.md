# Word Frequency Counter

## Task Description

You need to analyze a text file and count the frequency of each word, then output the top 10 most frequent words.

## Input

- **File location**: `/app/input.txt`
- **Format**: Plain text file containing multiple lines of text

## Processing Requirements

1. Read the text from `/app/input.txt`
2. Convert all text to lowercase
3. Extract all words (consider only alphabetic characters, split on whitespace and punctuation)
4. Count the frequency of each word
5. Sort words by frequency in descending order (most frequent first)
6. Select the top 10 most frequent words

## Output

- **File location**: `/app/output.txt`
- **Format**: One word per line, sorted by frequency (highest to lowest)
- **Example output**:
  ```
  the
  and
  to
  of
  a
  in
  is
  that
  it
  for
  ```

## Important Notes

- Words should be case-insensitive (convert to lowercase before counting)
- Only consider alphabetic characters (remove punctuation)
- If there are ties in frequency, maintain stable sorting (keep original order)
- Output exactly 10 words (one per line)
- No numbers, frequencies, or extra formatting in the output file

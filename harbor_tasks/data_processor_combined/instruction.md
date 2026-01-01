# Data Processor Combined Task

## Objective
Complete three independent data processing tasks involving text analysis, CSV processing, and JSON manipulation. All tasks must be completed successfully to pass.

---

## Task 1: Word Frequency Counter

### Input
- File: `/app/word_input.txt`
- Contains: Plain text with multiple words

### Requirements
1. Read the text file from `/app/word_input.txt`
2. Convert all text to lowercase
3. Extract only alphabetic words (a-z)
4. Count the frequency of each word
5. Find the top 10 most frequent words
6. Write results to `/app/word_output.txt`

### Output Format (`/app/word_output.txt`)
```
word: count
word: count
...
(exactly 10 lines, ordered by frequency descending)
```

**Example:**
```
the: 40
dog: 15
fox: 12
and: 10
```

---

## Task 2: CSV Filter and Summary

### Input
- File: `/app/employee_data.csv`
- Format: `id,name,department,salary`
- First row is header

### Requirements
1. Read the CSV file from `/app/employee_data.csv`
2. Filter all employees whose salary is **greater than 50000**
3. Write filtered data (with header) to `/app/csv_output.txt`
4. Append a summary section with:
   - Total number of filtered employees
   - Average salary (rounded to 2 decimal places)

### Output Format (`/app/csv_output.txt`)
```
id,name,department,salary
<filtered row 1>
<filtered row 2>
...

--- Summary ---
Total employees: <count>
Average salary: <average>
```

**Example:**
```
id,name,department,salary
1,Alice,Engineering,75000
3,Charlie,Sales,60000

--- Summary ---
Total employees: 2
Average salary: 67500.00
```

---

## Task 3: JSON Product Analysis

### Input
- File: `/app/products.json`
- Format: Array of product objects
- Each product has: `id`, `name`, `category`, `price`, `in_stock`

### Requirements
1. Read the JSON file from `/app/products.json`
2. Filter products that are in stock (`in_stock: true`)
3. Group products by category
4. For each category, calculate:
   - Number of products
   - Average price (rounded to 2 decimal places)
   - Cheapest product name
   - Most expensive product name
5. Write results to `/app/json_output.txt`

### Output Format (`/app/json_output.txt`)
```
Category: <category_name>
  Products: <count>
  Average Price: <price>
  Cheapest: <product_name> ($<price>)
  Most Expensive: <product_name> ($<price>)

Category: <category_name>
  ...
```

Categories should be sorted alphabetically.

**Example:**
```
Category: Electronics
  Products: 3
  Average Price: 599.99
  Cheapest: Mouse ($29.99)
  Most Expensive: Laptop ($1199.99)

Category: Office
  Products: 2
  Average Price: 45.50
  Cheapest: Pen ($5.99)
  Most Expensive: Notebook ($85.00)
```

---

## Success Criteria

All three output files must exist and contain valid data:
- `/app/word_output.txt` - Exactly 10 words with correct frequencies
- `/app/csv_output.txt` - Filtered CSV data with summary
- `/app/json_output.txt` - Categorized product analysis

The agent must complete all three tasks independently by reading the input files and producing the correct output format.

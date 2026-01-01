#!/usr/bin/env python3
"""
Validation tests for the Data Processor Combined task.
Tests all three functionalities: word frequency, CSV filtering, and JSON analysis.
"""

import re
import csv
import json
import sys
from collections import Counter


def test_word_frequency():
    """Test Task 1: Word Frequency Counter"""
    print("Testing Task 1: Word Frequency Counter...")
    
    # Read expected input (support both Docker and local paths)
    import os
    word_input = '/app/word_input.txt' if os.path.exists('/app/word_input.txt') else 'environment/word_input.txt'
    with open(word_input, 'r') as f:
        text = f.read().lower()
    
    words = re.findall(r'[a-z]+', text)
    expected_counts = Counter(words).most_common(10)
    
    # Read actual output (support both Docker and local paths)
    word_output = '/app/word_output.txt' if os.path.exists('/app/word_output.txt') else 'word_output.txt'
    try:
        with open(word_output, 'r') as f:
            lines = f.read().strip().split('\n')
    except FileNotFoundError:
        print("ERROR: word_output.txt not found")
        return False
    
    # Validate line count
    if len(lines) != 10:
        print(f"ERROR: Expected 10 lines, got {len(lines)}")
        return False
    
    # Parse output
    actual_counts = []
    for line in lines:
        if ':' not in line:
            print(f"ERROR: Invalid format in line: {line}")
            return False
        
        parts = line.split(':')
        if len(parts) != 2:
            print(f"ERROR: Invalid format in line: {line}")
            return False
        
        word = parts[0].strip()
        try:
            count = int(parts[1].strip())
        except ValueError:
            print(f"ERROR: Invalid count in line: {line}")
            return False
        
        actual_counts.append((word, count))
    
    # Compare results
    if actual_counts != expected_counts:
        print("ERROR: Word frequencies do not match expected output")
        print(f"Expected: {expected_counts}")
        print(f"Got: {actual_counts}")
        return False
    
    print("[PASS] Task 1")
    return True


def test_csv_filter():
    """Test Task 2: CSV Filter and Summary"""
    print("Testing Task 2: CSV Filter and Summary...")
    
    import os
    threshold = 50000
    
    # Read expected data (support both Docker and local paths)
    csv_input = '/app/employee_data.csv' if os.path.exists('/app/employee_data.csv') else 'environment/employee_data.csv'
    filtered_rows = []
    total_salary = 0
    
    with open(csv_input, 'r') as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        
        for row in reader:
            salary = int(row['salary'])
            if salary > threshold:
                filtered_rows.append(row)
                total_salary += salary
    
    expected_count = len(filtered_rows)
    expected_avg = total_salary / expected_count if expected_count > 0 else 0
    
    # Read actual output (support both Docker and local paths)
    csv_output = '/app/csv_output.txt' if os.path.exists('/app/csv_output.txt') else 'csv_output.txt'
    try:
        with open(csv_output, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("ERROR: csv_output.txt not found")
        return False
    
    lines = content.strip().split('\n')
    
    # Find summary section
    try:
        summary_index = lines.index('--- Summary ---')
    except ValueError:
        print("ERROR: Summary section not found")
        return False
    
    # Validate CSV section
    csv_lines = lines[:summary_index]
    if len(csv_lines) < 1:
        print("ERROR: No CSV data found")
        return False
    
    # Check header
    if csv_lines[0] != ','.join(header):
        print(f"ERROR: Header mismatch. Expected: {','.join(header)}, Got: {csv_lines[0]}")
        return False
    
    # Check number of data rows
    data_rows = [line for line in csv_lines[1:] if line.strip()]
    if len(data_rows) != expected_count:
        print(f"ERROR: Expected {expected_count} filtered rows, got {len(data_rows)}")
        return False
    
    # Validate summary
    summary_lines = [line for line in lines[summary_index+1:] if line.strip()]
    if len(summary_lines) < 2:
        print("ERROR: Summary incomplete")
        return False
    
    # Check total employees
    if not summary_lines[0].startswith('Total employees:'):
        print("ERROR: Total employees line not found")
        return False
    
    actual_count = int(summary_lines[0].split(':')[1].strip())
    if actual_count != expected_count:
        print(f"ERROR: Expected {expected_count} employees, got {actual_count}")
        return False
    
    # Check average salary
    if not summary_lines[1].startswith('Average salary:'):
        print("ERROR: Average salary line not found")
        return False
    
    actual_avg = float(summary_lines[1].split(':')[1].strip())
    if abs(actual_avg - expected_avg) > 0.01:
        print(f"ERROR: Expected average {expected_avg:.2f}, got {actual_avg:.2f}")
        return False
    
    print("[PASS] Task 2")
    return True


def test_json_analysis():
    """Test Task 3: JSON Product Analysis"""
    print("Testing Task 3: JSON Product Analysis...")
    
    import os
    # Read expected data (support both Docker and local paths)
    json_input = '/app/products.json' if os.path.exists('/app/products.json') else 'environment/products.json'
    with open(json_input, 'r') as f:
        products = json.load(f)
    
    # Filter in-stock products
    in_stock_products = [p for p in products if p.get('in_stock', False)]
    
    # Group by category
    categories = {}
    for product in in_stock_products:
        category = product['category']
        if category not in categories:
            categories[category] = []
        categories[category].append(product)
    
    # Read actual output (support both Docker and local paths)
    json_output = '/app/json_output.txt' if os.path.exists('/app/json_output.txt') else 'json_output.txt'
    try:
        with open(json_output, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("ERROR: json_output.txt not found")
        return False
    
    lines = [line.rstrip() for line in content.split('\n')]
    
    # Parse output by categories
    current_category = None
    parsed_categories = {}
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        if line.startswith('Category:'):
            current_category = line.split(':', 1)[1].strip()
            parsed_categories[current_category] = {}
            i += 1
            
            # Read category data
            while i < len(lines) and lines[i].startswith('  '):
                data_line = lines[i].strip()
                if ':' in data_line:
                    key, value = data_line.split(':', 1)
                    parsed_categories[current_category][key.strip()] = value.strip()
                i += 1
        else:
            i += 1
    
    # Validate categories
    expected_categories = sorted(categories.keys())
    actual_categories = sorted(parsed_categories.keys())
    
    if expected_categories != actual_categories:
        print(f"ERROR: Category mismatch. Expected: {expected_categories}, Got: {actual_categories}")
        return False
    
    # Validate each category
    for category in expected_categories:
        products_in_cat = categories[category]
        parsed_cat = parsed_categories[category]
        
        # Check product count
        expected_count = len(products_in_cat)
        actual_count = int(parsed_cat['Products'])
        if expected_count != actual_count:
            print(f"ERROR: {category} - Expected {expected_count} products, got {actual_count}")
            return False
        
        # Check average price
        expected_avg = sum(p['price'] for p in products_in_cat) / expected_count
        actual_avg = float(parsed_cat['Average Price'])
        if abs(expected_avg - actual_avg) > 0.01:
            print(f"ERROR: {category} - Expected avg {expected_avg:.2f}, got {actual_avg:.2f}")
            return False
        
        # Check cheapest product
        cheapest = min(products_in_cat, key=lambda p: p['price'])
        if cheapest['name'] not in parsed_cat['Cheapest']:
            print(f"ERROR: {category} - Cheapest product mismatch")
            return False
        
        # Check most expensive product
        most_expensive = max(products_in_cat, key=lambda p: p['price'])
        if most_expensive['name'] not in parsed_cat['Most Expensive']:
            print(f"ERROR: {category} - Most expensive product mismatch")
            return False
    
    print("[PASS] Task 3")
    return True


def main():
    """Run all tests"""
    print("=" * 50)
    print("Data Processor Combined - Validation Tests")
    print("=" * 50)
    print()
    
    all_passed = True
    
    # Test Task 1
    if not test_word_frequency():
        all_passed = False
    print()
    
    # Test Task 2
    if not test_csv_filter():
        all_passed = False
    print()
    
    # Test Task 3
    if not test_json_analysis():
        all_passed = False
    print()
    
    print("=" * 50)
    if all_passed:
        print("ALL TESTS PASSED")
        print("=" * 50)
        return 0
    else:
        print("SOME TESTS FAILED [X]")
        print("=" * 50)
        return 1


if __name__ == '__main__':
    sys.exit(main())

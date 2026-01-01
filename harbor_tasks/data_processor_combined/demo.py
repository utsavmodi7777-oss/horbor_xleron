import re, csv, json
from collections import Counter

# Feature 1: Word Frequency
text = open('environment/word_input.txt').read().lower()
words = re.findall(r'[a-z]+', text)
top_10 = Counter(words).most_common(10)
print('Feature 1: Word Frequency Analysis')
print('='*40)
for word, count in top_10:
    print(f'  {word:12} : {count}')
print()

# Feature 2: CSV Filter
reader = csv.DictReader(open('environment/employee_data.csv'))
rows = [r for r in reader if int(r['salary']) > 50000]
avg_sal = sum(int(r['salary']) for r in rows) / len(rows)
print('Feature 2: CSV Employee Filter (Salary > $50k)')
print('='*40)
print(f'  Filtered Employees: {len(rows)}')
print(f'  Average Salary    : ${avg_sal:,.2f}')
print()

# Feature 3: JSON Analysis
products = json.load(open('environment/products.json'))
in_stock = [p for p in products if p.get('in_stock', True)]
cats = {}
for p in in_stock:
    cats.setdefault(p['category'], []).append(p)
print('Feature 3: JSON Product Analysis')
print('='*40)
for cat, prods in sorted(cats.items()):
    avg_price = sum(p['price'] for p in prods) / len(prods)
    print(f'  {cat:18}: {len(prods)} products, Avg ${avg_price:.2f}')

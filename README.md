# Harbor Tasks - xelron Assignment Submission

**Submitted by:** Utsav Modi  
**Course:** SEM_7  
**Framework:** Harbor - AI Agent Evaluation Platform  
**Repository:** https://github.com/utsavmodi7777-oss/harbor_xelron

---

## 📋 Project Overview

This project implements **Harbor containerized tasks** for AI agent evaluation with three main functionalities:
1. **Word Frequency Counter** - Analyzes text and outputs top 10 most frequent words
2. **CSV Employee Filter** - Filters employees by salary threshold ($50,000+)
3. **JSON Product Analysis** - Categorizes products and calculates statistics

**Project Description (under 300 chars):**  
*Harbor containerized tasks for AI agent evaluation: word frequency counter, CSV filtering (salary>50k), JSON product analysis. Includes Docker setup, validation tests, Oracle (1.0) vs NOP (0.0) scoring.*

---

## 🗂️ Project Structure

```
harbor_xelron/
├── README.md                                # This file
├── SCREENSHOTS.md                           # Screenshot documentation
├── defiantion.pdf                           # Assignment requirements
├── test_oracle_nop.ps1                      # Oracle/NOP evaluation script
├── screenshots/                             # Execution results
│   ├── 01_task1_word_frequency.png
│   ├── 02_task2_combined_features.png
│   ├── 03_oracle_execution.png
│   ├── 04_validation_tests.png
│   ├── 05_oracle_result.png
│   ├── 06_nop_result.png
│   └── 07_final_summary.png
└── harbor_tasks/
    ├── word_frequency/                      # Task 1
    └── data_processor_combined/             # Task 2
```

---

## ✨ Features

### Task 1: Word Frequency Counter
- Counts word frequencies in text (case-insensitive)
- Outputs top 10 most frequent words
- Result: `the: 40`, `dog: 15`, `fox: 12`, etc.

### Task 2: Data Processor Combined (3 Features)

**Feature 1 - Word Frequency:**
- Top 10 words: `the: 38`, `dog: 15`, `fox: 13`

**Feature 2 - CSV Filter:**
- Filters 11 employees with salary > $50k
- Average salary: $66,181.82

**Feature 3 - JSON Analysis:**
- Electronics: 5 products, Avg $303.99
- Furniture: 3 products, Avg $278.66
- Office Supplies: 4 products, Avg $32.49

---

## 🚀 Running Tests

```powershell
# Oracle vs NOP validation
.\test_oracle_nop.ps1
```

**Expected Results:**
- Oracle Test: 1.0 (PASS) ✓
- NOP Test: 0.0 (FAIL) ✓

---

## 📊 Validation Results

| Agent | Score | Status | Meaning |
|-------|-------|--------|---------|
| Oracle | 1.0 | PASS | Task solvable with solution |
| NOP | 0.0 | FAIL | Task requires actual work |

---

## 🎯 Harbor Framework Compliance

✅ Containerized environments (Docker)  
✅ Modular task structure (task.toml, instruction.md)  
✅ Agent evaluation (Oracle/NOP scoring)  
✅ Automated validation  
✅ Multiple features (3 independent tasks)

---

## 📸 Screenshots

See [SCREENSHOTS.md](SCREENSHOTS.md) for detailed execution results with descriptions.

---

## 📝 Submission

```bash
git checkout -b new-hire/utsav-modi/data-processor-combined
git add harbor_tasks/ screenshots/ README.md SCREENSHOTS.md
git commit -m "Add data_processor_combined: Multi-feature task with word frequency, CSV filter, and JSON analysis"
git push -u origin new-hire/utsav-modi/data-processor-combined
```

---

## ✅ Success Criteria

- ✅ Oracle test: 1.0 (PERFECT SCORE)
- ✅ NOP test: 0.0 (NO OUTPUT)
- ✅ All tests PASS
- ✅ Screenshots included
- ✅ Complete documentation

**Status:** ✅ **READY FOR SUBMISSION**

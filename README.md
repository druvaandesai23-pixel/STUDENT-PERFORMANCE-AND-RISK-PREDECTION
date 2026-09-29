# STUDENT-PERFORMANCE-AND-RISK-PREDECTION
# Student Performance Analyzer

## Overview
A console application (CSE1021 - Introduction to Problem Solving and Programming)
that records CAT 1, CAT 2 and Term End marks, stores them in CSV, and reports
pass/fail status plus a CAT-based prediction of Term End performance.

## Features
- Validated marks entry (numeric, within 0 to max)
- CSV save and reload of student data
- Percentage, pass/fail and risk-prediction analysis
- Class summary with prediction accuracy
- Flags students who passed both CATs but failed Term End
- File-based logging (`app.log`)

## Technologies
Python 3.8+ (standard library only: `csv`, `os`, `logging`, `dataclasses`, `unittest`), Git.

## Project Structure
```
main.py             entry point / workflow
src/config.py       constants and thresholds
src/models.py       Student data class
src/validators.py   input validation
src/data_entry.py   Module 1: data entry
src/storage.py      Module 2: CSV storage
src/analyzer.py     Module 3: analysis and prediction
src/reports.py      Module 4: console reporting
src/logger_setup.py logging configuration
tests/              unit tests
```

## Install and Run
```
git clone <your-repo-url>
cd student-performance-analyzer
python main.py
```
No third-party packages are required.

## Testing
```
python -m unittest discover -s tests -t .
```

## Screenshots
_Add screenshots of a sample run here._

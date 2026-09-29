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
![First screenshot](https://github.com/druvaandesai23-pixel/STUDENT-PERFORMANCE-AND-RISK-PREDECTION/blob/03380f0e4ba3499a0b6b1bd63f22cafa500e1c05/Screenshot%202026-09-29%20235243.png)
![Second screenshot](https://github.com/druvaandesai23-pixel/STUDENT-PERFORMANCE-AND-RISK-PREDECTION/blob/3b9a0df017dd4b7922f29a56239f256439c5fa09/Screenshot%202026-09-29%20235313.png)


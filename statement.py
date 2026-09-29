# Problem Statement

## Problem
Instructors and students often track CAT 1, CAT 2 and Term End marks by hand.
This makes it slow to see who has passed, and hard to tell early whether a
student's continuous-assessment performance is a warning sign for the final exam.

## Scope
- Enter marks for any number of students (CAT 1 /50, CAT 2 /50, Term End /100)
- Validate all input and persist records in a CSV file
- Compute percentages, pass/fail status and a CAT-based risk prediction
- Report class-level results and prediction accuracy
- Out of scope: GUI, database server, multi-user access

## Target Users
- Course instructors and teaching assistants
- Students who want to check their own standing

## High-Level Features
1. Validated data entry (range and type checks)
2. CSV storage: save new data or reload previous data
3. Analysis: per-student percentages, pass/fail rule (>= 40% in every component),
   risk prediction (CAT average >= 50% predicts a Term End pass)
4. Summary report: totals, prediction accuracy, and students who passed both
   CATs but failed Term End
5. File logging of events and errors


# L6_L7_14_library_fines - Library Fines

## Lab 6: Code and Branch Coverage

### About

A small Python application that:
- Calculates late return fines based on library member type.
- Checks whether a member is eligible to borrow more books.
- Determines whether a book can be renewed.

### Files

| File | Description |
|---|---|
| `library_fines.py` | Original application module |
| `test_library_fines.py` | Teacher-provided starter tests |
| `CodeCoverageTest_PES2UG24AM170_library_fines.py` | Test cases for code coverage |
| `BranchCoverageTest_PES2UG24AM170_library_fines.py` | Test cases for branch coverage |
| `screenshots/` | Screenshots of final coverage reports |

### Tools Used

- Python 3.14.3
- pytest
- coverage.py

### How to Run Code Coverage

```bash
py -m coverage erase
py -m coverage run --source=library_fines -m pytest -p no:cacheprovider CodeCoverageTest_PES2UG24AM170_library_fines.py
py -m coverage report -m
```

### How to Run Branch Coverage

```bash
py -m coverage erase
py -m coverage run --branch --source=library_fines -m pytest -p no:cacheprovider BranchCoverageTest_PES2UG24AM170_library_fines.py
py -m coverage report -m
```

### Final Results

| Coverage Type | Tests Passed | Coverage |
|---|---:|---:|
| Code Coverage | 18 | 100% |
| Branch Coverage | 24 | 100% |

All 32 statements and all 22 branches were covered in the respective final test runs.

### Screenshots

- `screenshots/Code_Coverage.png`
- `screenshots/Branch_Coverage.png`


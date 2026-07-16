# Python Basics Practice Repository

Welcome to my Python Basics Practice Repository. This repository contains the programs, exercises, and experiments I completed while learning Python. Each script focuses on a specific concept, helping me build a strong foundation in Python programming through hands-on practice.

## Table of Contents

- [Introduction](#introduction)
- [Objectives](#objectives)
- [Topics Covered](#topics-covered)
- [Repository Structure](#repository-structure)
- [Programs Included](#programs-included)
- [Prerequisites](#prerequisites)
- [How to Run the Programs](#how-to-run-the-programs)
- [Learning Outcomes](#learning-outcomes)
- [Author](#author)

## Introduction

This repository is a hands-on collection of short Python scripts and small examples created while learning Python. Each file focuses on one or two concepts (I/O, control flow, data structures, file handling, small utilities, or tests).
The numbered files (01–22) follow the order in which I learned different Python concepts, making it easy to track my learning progression.


## Objectives

- Keep a record of exercises and short programs as I learn Python.
- Practice core Python topics through concise, self-contained scripts.
- Demonstrate the use of Python's standard library and selected third-party packages through practical examples.

## Topics Covered 

- Basic I/O: `print`, `input`
- Variables and data types: strings, integers, floats
- String manipulation: `strip()`, `title()`, `split()`
- Control flow: `if`/`elif`/`else`, `match`/`case`
- Functions and default arguments
- Loops: `for`, `while` and loop patterns
- Data structures: lists and dictionaries
- File I/O: reading/writing text and CSV files
- CSV handling with `csv.reader` and `csv.DictWriter`
- Error handling: `try` / `except`
- Debugging and `if __name__ == "__main__"` patterns
- Using modules: `random`, `statistics`, `json`, `re`, `requests`
- Command-line arguments via `sys.argv`
- Third-party packages examples: `cowsay`, `Pillow` (image processing)
- Regular expressions for validation
- Basic testing patterns and `pytest`

## Repository Structure

The repository contains the following main files:

| Path | Type |
| --- | --- |
| `01_Hello.py` … `22_Regular_Expressions.py` | Practice Python scripts (see list below) |
| `Calculator.py`, `Hello.py`, `Say.py`, `Sayings.py` | Utility scripts / small modules |
| `names.txt`, `students.csv`, `students_2.csv`, `students_3.csv` | Example input/output data files |

Note: auxiliary folders like caches and the `Test/` directory are intentionally excluded from this listing.

## Programs Included ✅

The table below lists every Python program in this repository with a short description (1–2 lines each).

| Filename | Description |
| --- | --- |
| `01_Hello.py` | Simple print examples: "Hello, World!" and quoted strings. |
| `02_Variables.py` | User input demos: name and age; shows `print` formatting and `end` parameter. |
| `03_String.py` | String cleanup and formatting (`strip`, `title`) and splitting a full name into first/last. |
| `04_Integer.py` | Integer input and addition example. |
| `05_Float.py` | Float input, division, rounding and numeric formatting. |
| `06_Function.py` | Function with default parameter (`add`) and simple usage. |
| `07.0_Conditionals.py` | Number comparisons with `if`/`elif` and logical operators. |
| `07.1_Parity.py` | `is_even` helper to determine even/odd numbers. |
| `07.2_Home.py` | `match`/`case` example mapping names to houses. |
| `08_Loops.py` | `for` and `while` loop examples and small helper functions. |
| `09_List.py` | Basic list operations: iteration, membership, append. |
| `10_Dictionary.py` | Dictionary lookups and list-of-dictionaries patterns. |
| `11_Mario.py` | Text-based shapes (rows, columns, squares) using nested loops. |
| `12_Exceptions.py` | Input validation with `try` / `except` to handle `ValueError`. |
| `13_Debugging.py` | Small program to print a pyramid; demonstrates `main` and debugging entry points. |
| `14.0_Libraries.py` | Examples using the `random` module (`choice`, `randint`, `shuffle`). |
| `14.1_Statistics.py` | Uses `statistics.mean` and a small `sys.argv` argument check example. |
| `14.2_Arguments.py` | Command-line arguments iteration via `sys.argv`. |
| `15_Packages.py` | Demonstrates using a third-party package (`cowsay`). |
| `16_APIs.py` | Example of calling an external API with `requests` and parsing JSON. |
| `17_Style.py` | Notes about code style (PEP 8) and a short dict example. |
| `18_Names.py` | Collecting names, writing to `names.txt`, and reading/sorting file contents. |
| `19_Students.py` | Parsing `students.csv` into lists/dicts and sorting by name. |
| `20_Students_2.py` | CSV module usage: `csv.reader` and `csv.DictReader` examples. |
| `21_Students_3.py` | Appending rows to `students_3.csv` using `csv.DictWriter`. |
| `22_Regular_Expressions.py` | Email validation examples using `re` (and simple string checks). |
| `Calculator.py` | Small module with `square()` and a `main()` wrapper for quick tests. |
| `Costumes.py` | Image processing example using `Pillow` to compose GIF animations. |
| `Hello.py` | `hello()` function returning greeting; demonstrates `if __name__ == "__main__"`. |
| `Say.py` | CLI wrapper that calls `Sayings.goodbye`; demonstrates module imports and `sys.argv`. |
| `Sayings.py` | Tiny package-like module with `hello()` and `goodbye()` helpers. |
| `Test_Calculator_1.py` | Simple manual tests for `Calculator.square()` (prints on failure). |
| `Test_Calculator_2.py` | Tests using `assert` inside try/except blocks for clearer messages. |
| `Test_Calculator_3.py` | `pytest`-style tests for `Calculator.square()` (example of pytest usage). |
| `Test_Hello.py` | `pytest` tests for `Hello.hello()` function. |

### Supporting data files

- `names.txt` — example file used by `18_Names.py` to persist names.
- `students.csv`, `students_2.csv`, `students_3.csv` — sample CSVs used by the students examples.

## Prerequisites

- Python 3.8+ recommended.
- Optional packages used in examples:
	- `requests` (for `16_APIs.py`) — `pip install requests`
	- `Pillow` (for `Costumes.py`) — `pip install pillow`
	- `cowsay` (for `15_Packages.py`) — `pip install cowsay`
	- `pytest` (for running tests) — `pip install pytest`

## How to Run the Programs

Most scripts are simple one-file examples and can be run with:

```bash
python 01_Hello.py
python 08_Loops.py
python 19_Students.py
```

Examples that require command-line arguments:

```bash
python 14.1_Statistics.py Alice
python 14.2_Arguments.py Alice Bob
python 16_APIs.py "Beatles"    # requires requests
python Costumes.py img1.png img2.png   # requires Pillow
```

To run tests with `pytest`:

```bash
pytest -q
```

## Learning Outcomes

- Familiarity with Python basics: I/O, variables, and data types.
- Practice structuring small scripts with functions and `main()` guards.
- Hands-on use of standard library modules (CSV, JSON, random, statistics, re).
- Confidence with file I/O patterns and simple CSV handling.
- Awareness of basic testing practices and how to run `pytest`.
- Exposure to calling external APIs and using third-party packages.


## Author

**Sumaira**

B.Tech Computer Science student passionate about Python, AI/ML, and software development.

This repository documents my journey of learning Python through practical coding exercises and examples.
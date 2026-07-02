# Markdown Note Search

A command-line Python application that searches Markdown files for a keyword and displays every matching line along with its line number.

## Features

- Validate folder paths
- Search only `.md` files
- Case-insensitive keyword search
- Display matching line numbers
- Show matching lines
- Display total matched files and total matches
- Handle cases where no matches are found

## Tech Stack

- Python
- os

## Run

```bash
python3 main.py
```

## Example

Folder:

```
notes/
├── Python.md
├── AI.md
├── README.txt
```

Search Keyword:

```
python
```

Output:

```
Python.md
  Line 2: Python is an interpreted language.
  Line 8: FastAPI is written in Python.

AI.md
  Line 4: Python powers modern AI systems.

----------------------------------

Files matched: 2
Total matches: 3
```

## Concepts Practiced

- File handling
- Reading text files
- Line-by-line processing
- Case-insensitive searching
- Dictionaries
- Tuples
- Enumerate
- Path manipulation
- CLI application design

## Project Status

✅ Complete
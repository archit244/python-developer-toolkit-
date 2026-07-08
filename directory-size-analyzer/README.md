# Directory Size Analyzer

A command-line Python utility that recursively scans a directory, calculates the size of every file and subfolder, and displays a hierarchical size breakdown along with the total directory size.

## Features

- Analyze the size of any directory
- Recursively traverses subfolders
- Displays files and folders in a tree-like structure
- Calculates total size for every directory
- Converts file sizes into human-readable units (B, KB, MB, GB, TB)
- Ignores hidden files and folders (e.g. `.git`, `.DS_Store`)

## Tech Stack

- Python
- os

## Run

```bash
python3 main.py
```

## Example Output

```
expense-tracker/

    README.md (1.94 KB)

    blba/

        new.py (0 B)

        Total: 0 B

    main.py (5.59 KB)

    Total: 7.53 KB
```

## Concepts Practiced

- Recursion
- Recursive accumulation
- Directory traversal
- File handling
- File metadata (`os.path.getsize`)
- Human-readable size formatting
- CLI application design
- Function decomposition

## Time Complexity

- **O(n)**

where **n** is the total number of files and directories visited.

## Space Complexity

- **O(d)**

where **d** is the maximum directory depth due to recursive function calls.

## Future Improvements

- Display directory tree using `├──` and `└──`
- Export analysis to a text or JSON report
- Show percentage contribution of each folder
- Sort by size instead of name
- Interactive directory explorer
- Display file count for each folder

## Project Status

✅ Complete
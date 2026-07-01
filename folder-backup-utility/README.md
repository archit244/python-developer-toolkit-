# Folder Backup Utility

A command-line application built in Python that creates a complete backup of a folder while preserving its directory structure.

## Features

- Validate folder paths
- Create a backup folder automatically
- Copy all files and subfolders recursively
- Preserve file metadata using `shutil.copy2()`
- Automatically create a unique backup folder if one already exists (e.g. `folder_backup(1)`)

## Tech Stack

- Python
- os
- shutil

## Run

```bash
python3 main.py
```

## Example

Before:

```
Documents/
├── notes.txt
├── image.png
└── Projects/
    └── app.py
```

After:

```
Documents/
Documents_backup/
├── notes.txt
├── image.png
└── Projects/
    └── app.py
```

## Concepts Practiced

- Recursion
- File and directory traversal
- Path manipulation
- Recursive folder creation
- File copying with metadata
- Working with the operating system using Python

## Project Status

✅ Complete
# Bulk File Renamer

A command-line Python application that renames all files in a folder using a custom prefix while preserving their original file extensions.

## Features

- Validate folder paths
- Rename files with a custom prefix
- Preserve original file extensions
- Automatically avoid filename collisions
- Skip directories
- Display every rename operation
- Show a summary after completion

## Tech Stack

- Python
- os

## Run

```bash
python3 main.py
```

## Example

Before:

```
Photos/
├── IMG_1023.jpg
├── Screenshot.png
├── notes.txt
```

After using the prefix `vacation`:

```
Photos/
├── vacation_1.jpg
├── vacation_2.png
├── vacation_3.txt
```

## Concepts Practiced

- File renaming
- Path manipulation
- String formatting
- File extension handling
- Input validation
- Collision detection

## Project Status

✅ Complete
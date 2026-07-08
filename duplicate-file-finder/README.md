# Duplicate File Finder

A command-line Python utility that scans a folder, detects duplicate files using SHA-256 hashing, and optionally removes duplicate copies while preserving the oldest file.

## Features

- Scan any folder for duplicate files
- Supports all file types (images, videos, PDFs, documents, etc.)
- Uses SHA-256 hashing for accurate duplicate detection
- Groups duplicate files together
- Displays duplicate groups in a clean format
- Optional duplicate cleanup
- Automatically keeps the oldest file and deletes newer copies
- Confirmation prompt before deleting files

## Tech Stack

- Python
- os
- hashlib

## Run

```bash
python3 main.py
```

## Example

```
Enter folder path:
/Users/archit/Desktop/Photos

Scanning files...

===== Duplicate Files =====

Group 1:
  - cat.jpg
  - cat_copy.jpg

Group 2:
  - resume.pdf
  - resume_backup.pdf

Duplicate groups found: 2

Do you want to delete duplicates? (y/n): y

Keeping: cat.jpg
Deleted: cat_copy.jpg

Keeping: resume.pdf
Deleted: resume_backup.pdf

Duplicate cleanup completed successfully.
```

## Concepts Practiced

- Binary file handling (`rb`)
- SHA-256 hashing
- File comparison
- Dictionaries
- File metadata (`os.path.getmtime`)
- File deletion (`os.remove`)
- User input validation
- Function decomposition
- CLI application design

## Time Complexity

- **Scanning & Hashing:** `O(total bytes of all files)`
- **Dictionary Lookups:** `O(1)` average
- **Overall:** `O(total bytes read)`

## Space Complexity

- **O(n)**

where **n** is the number of files scanned.

## Future Improvements

- Recursive folder scanning
- Chunk-based hashing for large files
- Move duplicates to a recycle folder instead of permanently deleting them
- Export duplicate report to a text or JSON file
- Filter files by extension
- Compare files by size before hashing for additional optimization

## Project Status

✅ Complete
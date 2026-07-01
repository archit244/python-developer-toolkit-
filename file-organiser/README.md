# File Organizer

A command-line Python application that automatically organizes files in a folder into categorized subfolders based on their file extensions.

## Features

- Organize files into categories automatically
- Creates folders if they don't already exist
- Supports common document, image, music, and video formats
- Ignores existing folders while organizing
- Validates folder paths before processing

## Supported Categories

| Category | Extensions |
|----------|------------|
| Documents | `.pdf`, `.doc`, `.docx`, `.txt` |
| Images | `.jpg`, `.jpeg`, `.png`, `.gif` |
| Music | `.mp3`, `.wav` |
| Videos | `.mp4`, `.mov`, `.mkv` |
| Others | Any unsupported extension |

## Tech Stack

- Python
- `os`
- `shutil`

## Run

```bash
python3 main.py
```

## Example

Before:

```
Downloads/
├── resume.pdf
├── photo.jpg
├── song.mp3
└── movie.mp4
```

After:

```
Downloads/
├── Documents/
│   └── resume.pdf
├── Images/
│   └── photo.jpg
├── Music/
│   └── song.mp3
└── Videos/
    └── movie.mp4
```

## Project Status

✅ Completed
# Design — Project 0.3

## Data

Folder Path

↓

List of Files

↓

Extension

↓

Category

↓

Destination Folder

---

## Categories

Documents

- .pdf
- .doc
- .docx
- .txt

Images

- .jpg
- .jpeg
- .png
- .gif

Music

- .mp3
- .wav

Videos

- .mp4
- .mov
- .mkv

Others

Everything else

---

## High-Level Algorithm

1. Ask user for folder path.

2. Validate the path.

3. Read all files inside the folder.

4. For every file

   - Determine file extension.
   - Find matching category.
   - Create destination folder if necessary.
   - Move file.

5. Display completion message.

---

## Edge Cases

- Empty folder
- Invalid folder path
- Unknown file extension
- Folder already exists
- Duplicate file names
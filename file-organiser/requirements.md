# Requirements — Project 0.3

# Project

File Organizer CLI

---

## Goal

Build a command-line application that automatically organizes files inside a folder based on their file extensions.

---

## Functional Requirements

The application should:

- Accept a folder path from the user.
- Scan all files inside the folder.
- Identify each file's extension.
- Create destination folders if they do not already exist.
- Move files into their corresponding folders.

### Supported Categories

| Extensions | Folder |
|------------|--------|
| .pdf .doc .docx .txt | Documents |
| .jpg .jpeg .png .gif | Images |
| .mp3 .wav | Music |
| .mp4 .mov .mkv | Videos |
| Others | Others |

---

## Non-functional Requirements

- Never delete files.
- Never overwrite existing files.
- Work even if destination folders already exist.
- Handle empty folders gracefully.
- Display progress while organizing.

---

## Success Criteria

Given a folder containing mixed file types,

the application should organize every file into the correct folder without data loss.
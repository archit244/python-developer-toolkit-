# JSON Formatter

A command-line Python application that validates and formats JSON files into a readable, indented version.

## Features

- Validate JSON file paths
- Verify JSON syntax
- Format JSON using indentation
- Save formatted output as a new file
- Preserve the original file

## Tech Stack

- Python
- os
- json

## Run

```bash
python3 main.py
```

## Example

Input:

```json
{"name":"Archit","age":19,"skills":["Python","Java"]}
```

Output (`data_formatted.json`):

```json
{
    "name": "Archit",
    "age": 19,
    "skills": [
        "Python",
        "Java"
    ]
}
```

## Concepts Practiced

- JSON parsing
- Serialization & deserialization
- File handling
- Exception handling
- Path manipulation

## Project Status

✅ Complete
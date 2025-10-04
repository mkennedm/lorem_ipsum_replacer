# Lorem Ipsum Replacer

A Python command-line tool that replaces words in text files with lorem ipsum text while preserving formatting, capitalization, and numbers.

## Features

- **Smart word replacement**: Replaces alphabetic words with lorem ipsum text
- **Preserves formatting**: Maintains original capitalization patterns (uppercase, lowercase, title case)
- **Keeps numbers intact**: Numbers and numeric values remain unchanged
- **Preserves punctuation**: All punctuation and special characters are maintained
- **Cycling lorem words**: Uses a repeating pool of lorem ipsum words for variety
- **UTF-8 support**: Handles international characters properly

## Installation

No installation required. This is a standalone Python script that only uses the standard library.

**Requirements:**
- Python 3.6 or higher

## Usage

```bash
python lorem_ipsum_replacer.py <input_file> <output_file>
```

### Arguments

- `input_file`: Path to the text file you want to process
- `output_file`: Path where the lorem ipsum version will be saved

### Examples

```bash
# Replace words in a document
python lorem_ipsum_replacer.py document.txt lorem_document.txt

# Process a text file
python lorem_ipsum_replacer.py original.txt lorem_original.txt
```

## How It Works

The script uses a predefined pool of lorem ipsum words:
```
lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua
```

### Replacement Logic

1. **Word Detection**: Uses regex to identify alphabetic words (`\b[A-Za-z]+\b`)
2. **Number Preservation**: Numbers are left unchanged
3. **Capitalization Preservation**:
   - `WORD` → `LOREM` (all uppercase)
   - `Word` → `Lorem` (title case)
   - `word` → `lorem` (lowercase)
4. **Cycling**: Cycles through the lorem words in order, repeating when exhausted

### Example Transformations

| Original | Result |
|----------|--------|
| `Hello World!` | `Lorem Ipsum!` |
| `The year is 2025` | `Lorem ipsum dolor 2025` |
| `UPPERCASE TEXT` | `LOREM IPSUM DOLOR` |
| `Mixed Case Text` | `Lorem Ipsum Dolor` |

## Error Handling

The script includes proper error handling for:
- File not found errors
- Permission issues
- General processing errors

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Copyright (c) 2025 Matthew Kennedy

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this tool!

import re
import sys
import argparse

def replace_with_lorem(input_file, output_file):
    # A repeating pool of lorem ipsum words
    lorem_words = (
        "lorem ipsum dolor sit amet consectetur adipiscing elit "
        "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
    ).split()
    
    lorem_index = 0

    def get_lorem_word(match):
        nonlocal lorem_index
        word = match.group(0)

        # Leave numbers unchanged
        if word.isdigit():
            return word

        # Cycle through lorem words
        replacement = lorem_words[lorem_index % len(lorem_words)]
        lorem_index += 1

        # Preserve capitalization style
        if word.isupper():
            replacement = replacement.upper()
        elif word[0].isupper():
            replacement = replacement.capitalize()

        return replacement

    # Regex matches words (alphabetic sequences), keeps numbers/punctuation out
    word_pattern = re.compile(r"\b[A-Za-z]+\b")

    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    replaced_text = word_pattern.sub(get_lorem_word, text)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(replaced_text)


def main():
    parser = argparse.ArgumentParser(description="Replace words in a text file with lorem ipsum text")
    parser.add_argument("input_file", help="Input text file to process")
    parser.add_argument("output_file", help="Output file for the lorem ipsum text")
    
    args = parser.parse_args()
    
    try:
        replace_with_lorem(args.input_file, args.output_file)
        print(f"Successfully processed {args.input_file} -> {args.output_file}")
    except FileNotFoundError:
        print(f"Error: Input file '{args.input_file}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

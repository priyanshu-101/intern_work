import os

def count_words(lines):
    word_count = 0
    for line in lines:
        words = line.split()
        word_count += len(words)
    return word_count

def count_lines(lines):
    return len(lines)

def count_characters(lines):
    char_count = 0
    for line in lines:
        char_count += len(line)
    return char_count

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.writelines(content)
            print(f"File '{file_path}' has been successfully updated.")
    except Exception as e:
        print(f"Error occurred while writing to file: {e}")

def main():
    file_path = 'sample.txt'

    lines = read_file(file_path)
    if not lines:
        return


    word_count = count_words(lines)
    line_count = count_lines(lines)
    char_count = count_characters(lines)

    print(f"Word count: {word_count}")
    print(f"Line count: {line_count}")
    print(f"Character count: {char_count}")


    modified_lines = [line.replace('old_word', 'new_word') for line in lines]

    write_file(file_path, modified_lines)

if __name__ == "__main__":
    main()

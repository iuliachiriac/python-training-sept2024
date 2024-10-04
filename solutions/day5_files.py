# 1. Write a Python program that reads file content and displays the number of
# lines that were read.
no_of_lines = 0
with open("infile.txt") as f:
    for line in f:
        no_of_lines += 1
    print(f"{no_of_lines} lines read.")


# 2. Write a Python program to find the longest word in a file.
# for a small file:
with open("infile.txt") as f:
    longest_word = max(f.read().split(), key=len)
    print(f"v1 Longest word: {longest_word}.")

# for a large file
longest_word = ""
with open("infile.txt") as f:
    for line in f:
        for word in line.split():
            if len(word) > len(longest_word):
                longest_word = word
    print(f"v2 Longest word: {longest_word}.")


# 3. Write a Python function that takes a list of strings.py as an argument and
# writes each string to a new line in a file.
def append_lines(file, lines):
    with open(file, "a") as f:
        for line in lines:
            f.write(f"\n{line}")


append_lines("infile.txt", ["new line", "new line altogether"])

# 4. Write a Python program to append text into a file and display the entire
# content of that file (existing and appended text).
with open("infile.txt", 'a+') as f:
    f.write('New text')
    f.seek(0)
    for line in f:
        print(line, end='')


# 5. Write a function grep that receives text and file as parameters and returns
# a list with all the lines in the file containing text.
def grep(text, file):
    lines_matching = []
    with open(file) as f:
        for line in f:
            if text in line:
                lines_matching.append(line)
    return lines_matching


print(grep("better", "infile.txt"))


# 6. Write another function grepinto that receives text, infile and outfile as
# parameters and writes to outfile the lines in infile that contain text. Open
# both files within one with statement.
def grepinto(text, infile, outfile):
    with open(infile, "r") as fin, open(outfile, "w") as fout:
        for line in fin:
            if text in line:
                fout.write(line)


grepinto("better", "infile.txt", "outfile.txt")


# 7. Write a Python program to replace a word in a file.
with open("infile.txt", "r+") as f:
    content = f.read()
    content = content.replace("better", "worse")
    f.seek(0)
    f.write(content)
    f.truncate()

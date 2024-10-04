with open("script.py", "r") as f:
    for line in f:
        if "sentence" in line:
            break
        print(line, end="")


with open("out.txt", "w") as f:
    f.write("Something\n")
    f.writelines(["hello\n", "world\n"])

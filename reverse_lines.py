
try:
    # Open the file in read mode
    with open("example.txt", "r") as file:
        lines = file.readlines()

    # Reverse the order of lines
    lines.reverse()

    # Reverse and print each line
    for line in lines:
        print(line.rstrip("\n")[::-1])

except FileNotFoundError:
    print("Error: File not found.")

except IOError:
    print("Error: Unable to read the file.")

# Python Program to Print Each Line of a File in Reverse Order

## Aim
To read a file, reverse the order of its lines, reverse each line's characters, and print the result.

## Requirements
- Python 3
- Input file named `example.txt`

## Functions Used
1. `open()` – Opens the file.
2. `readlines()` – Reads all lines from the file.
3. `reverse()` – Reverses the order of lines.
4. `rstrip()` – Removes the newline character.
5. `[::-1]` – Reverses the characters in a line.
6. `try-except` – Handles file errors.

## Algorithm
1. Open the file in read mode.
2. Read all lines using `readlines()`.
3. Reverse the order of the lines.
4. Reverse the characters in each line.
5. Print each reversed line.
6. Handle file errors.

## Sample Input (`example.txt`)
```text
Hello
Python
World
```

## Expected Output
```text
dlroW
nohtyP
olleH
```

## Result
The program successfully prints each line in reverse order, with each line's characters reversed.

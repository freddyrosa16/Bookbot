# BookBot

BookBot is a small command-line program that analyzes books saved as text files. I built it as part of my Python learning path through Boot.dev.

It reads a book, counts the total number of words, counts how often each letter appears, and prints the character counts from highest to lowest.

The project is simple, but it helped me understand how data moves between functions instead of keeping everything in one file.

## What I practiced

- Reading text files with Python
- Organizing logic into separate modules
- Importing functions
- Counting values with dictionaries
- Turning dictionary data into a sortable list
- Sorting with a helper function
- Accepting a file path from the command line

## Run the project

BookBot requires Python 3 and has no external dependencies.

From the project directory, run:

```bash
python3 main.py books/frankenstein.txt
```

You can also analyze either of the other included books:

```bash
python3 main.py books/mobydick.txt
python3 main.py books/prideandprejudice.txt
```

## Project structure

```text
Bookbot/
├── books/       # Text files used for analysis
├── main.py      # Receives the book path and prints the report
└── stats.py     # Reads the book and calculates its statistics
```

## Current output

The report includes:

- The path of the analyzed book
- The total word count
- Alphabetic character counts in descending order


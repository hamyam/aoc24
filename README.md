# aoc24


## makemyday

the `makemyday` script generates a folder with name `dayXX` and creates the prose as markdown file, an empty python code file, an empty sample.dat to hold the sample data and of course your personal input.dat with the input for the specified day.

### requirements

You will need python3 with a venv and pandoc to run all commands successfully.

### setup

Create a `python venv` and pip install the `requirements.txt`. This installs the `AOC` scraper `aocd`. To get your input data, place your authenticated session id key from your browsers cookie at `~/.config/aocd/token` or export it to your PATH. See aocd doc for more info (https://github.com/wimglenn/advent-of-code-data).

Running the `makemyday.sh` will activate the p3 venv and run the aocd scraper and curl the task.

### usage

You can run the script in 2 different ways:

1) `./makemyday.sh` will run the script and prompt you to enter the number of day you want to create.
    a) entering a number creates the corresponding numbered folder
    b) leaving the number blank creates the folder for the current day of month. Works great in december...

2) `./makemyday.sh num` where num is a number creates the folder without prompt.






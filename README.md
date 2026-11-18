# 100 Days of Code: The Complete Python Pro Bootcamp

My solutions and notes while following the **100 Days of Code: The Complete Python Pro Bootcamp** course.

Author: Roberto Sanchez Santoyo

## Project structure

```
.
├── main.py              # Interactive menu to run any day
├── Beginner/            # Days 1-14
│   └── day_N/
│       ├── main.py      # Exercises and project of the day
│       └── notes_day_N.md
├── Intermediate/        # Days 15-...
│   └── day_N/
│       ├── main.py
│       └── notes_day_N.md
├── pyproject.toml
└── .python-version
```

Each day lives in its own folder, and its `main.py` holds everything built that day.

## Requirements

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/) (recommended). There are no external dependencies.

## Usage

Run the menu from the project root:

```bash
uv run python main.py
```

Choose a level, then a day. Type `0` to go back or exit, and press `Ctrl+C` to interrupt a program and return to the menu.

```
=== 100 Days of Code ===
1. Beginner
2. Intermediate
0. Exit
>
```

The menu discovers levels and days automatically. To add a new day, create `<Level>/day_N/main.py` and it will show up on its own. Empty files are skipped.

To run a single day directly:

```bash
uv run python Beginner/day_2/main.py
```

## Progress

| Level | Day | Topic |
|---|---|---|
| Beginner | 1 | Printing, strings and input |
| Beginner | 2 | Data types, numbers and operations (tip calculator) |
| Beginner | 3 | Control flow and conditionals (pizza order, treasure island) |
| Beginner | 4 | Randomisation and lists (rock paper scissors) |
| Beginner | 5 | Loops (password generator) |
| Beginner | 6 | Functions |
| Intermediate | 15 | Coffee machine |
| Intermediate | 16 | In progress |

import runpy
from pathlib import Path

ROOT = Path(__file__).parent
LEVEL_ORDER = ["Beginner", "Intermediate", "Advanced"]


def day_number(path: Path) -> int:
    return int(path.name.split("_")[1])


def discover_days(level: Path) -> list[Path]:
    """Return the non-empty day folders of a level, sorted numerically."""
    days = [
        d for d in level.glob("day_*")
        if d.name.split("_")[1].isdigit()
        and (d / "main.py").is_file()
        and (d / "main.py").stat().st_size > 0
    ]
    return sorted(days, key=day_number)


def discover_levels() -> list[Path]:
    """Return the level folders that contain at least one runnable day."""
    levels = [
        d for d in ROOT.iterdir()
        if d.is_dir() and not d.name.startswith(".") and discover_days(d)
    ]
    return sorted(
        levels,
        key=lambda d: (LEVEL_ORDER.index(d.name) if d.name in LEVEL_ORDER else len(LEVEL_ORDER), d.name),
    )


def choose(title: str, options: list[str], back_label: str) -> int | None:
    """Show a numbered menu; return the chosen index, or None for back/exit."""
    print(f"\n=== {title} ===")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    print(f"0. {back_label}")
    while True:
        answer = input("> ").strip()
        if answer == "0":
            return None
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return int(answer) - 1
        print(f"Please type a number between 0 and {len(options)}.")


def run_day(day: Path) -> None:
    print(f"\n--- Running {day.parent.name} / Day {day_number(day)} ---\n")
    try:
        runpy.run_path(str(day / "main.py"), run_name="__main__")
    except KeyboardInterrupt:
        print("\nInterrupted.")
    except Exception as error:
        print(f"\nThe program failed: {type(error).__name__}: {error}")
    input("\nPress Enter to return to the menu...")


def main() -> None:
    while True:
        levels = discover_levels()
        level_choice = choose("100 Days of Code", [l.name for l in levels], "Exit")
        if level_choice is None:
            print("Bye!")
            return
        level = levels[level_choice]

        while True:
            days = discover_days(level)
            day_choice = choose(level.name, [f"Day {day_number(d)}" for d in days], "Back")
            if day_choice is None:
                break
            run_day(days[day_choice])


if __name__ == "__main__":
    main()

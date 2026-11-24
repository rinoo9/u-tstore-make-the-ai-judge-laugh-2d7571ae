"""Make the AI Judge Laugh — one-line entry (max 200 characters).

Run: python3 main.py
"""

LINE = (
    "My AI judge laughed so hard at my joke that it hallucinated "
    "a better punchline, gave itself full marks, then billed me for the compute."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """The entry must be one funny line of at most 200 characters."""
    assert line.strip(), "entry must not be empty"
    assert "\n" not in line.strip(), "entry must be a single line"
    assert len(line) <= MAX_CHARS, f"entry is {len(line)} chars, over {MAX_CHARS}"


def main() -> None:
    validate(LINE)
    print(LINE)
    print(f"({len(LINE)}/{MAX_CHARS} characters)")


if __name__ == "__main__":
    main()

"""Deadpan forecast for the city of Vexholm, which does not exist.

Writes one line (at most 160 characters) to the entry file: a weather
forecast for an invented city, read deadpan, as if by a TV meteorologist.
"""

import os

ENTRY = (
    "In Vexholm tonight, expect a high of 12, a low of 12, and one small "
    "cloud that has been circling the town hall since 1987."
)


def resolve_output_path():
    """Resolve where the entry goes, without assuming the working directory."""
    explicit = os.environ.get("ENTRY_OUTPUT")
    if explicit:
        return explicit
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def main():
    if not 1 <= len(ENTRY) <= 160:
        raise ValueError("entry must be 1-160 characters, got %d" % len(ENTRY))
    if "\n" in ENTRY or ENTRY != ENTRY.strip():
        raise ValueError("entry must be exactly one non-blank line")
    path = resolve_output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

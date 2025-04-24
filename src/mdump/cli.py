from __future__ import annotations

import argparse
import os
import pathlib
import re
import sys
from typing import Pattern


def _compile(expr: str | None) -> Pattern[str] | None:
    """Compile a regular expression if provided."""
    return re.compile(rf"^({expr})$", re.IGNORECASE) if expr else None


def _ext_ok(path: pathlib.Path, ext_re: Pattern[str] | None) -> bool:
    """Check if the file matches the allowed extensions."""
    if ext_re is None:
        return True
    return bool(ext_re.match(path.suffix.lstrip(".")))


def generate_markdown(
    root: pathlib.Path,
    ignore_re: Pattern[str] | None,
    ext_re: Pattern[str] | None,
    output: pathlib.Path,
) -> None:
    """Writes a Markdown document containing all matching files and their contents."""
    with output.open("w", encoding="utf-8") as md:
        for dirpath, dirnames, filenames in os.walk(root):
            # Filter out ignored directories
            dirnames[:] = [
                d for d in dirnames if ignore_re is None or not ignore_re.match(d)
            ]

            for fname in filenames:
                path = pathlib.Path(dirpath, fname)
                if not _ext_ok(path, ext_re):
                    continue

                rel = path.relative_to(root)
                md.write(f"{rel}\n\n")

                lang = path.suffix.lstrip(".")  # Syntax highlighting language
                md.write(f"```{lang}\n")

                try:
                    text = path.read_text(encoding="utf-8", errors="replace")
                except Exception as exc:
                    # Could not read file (binary, permission error, etc.)
                    sys.stderr.write(f"Skipping {rel}: {exc}\n")
                    md.write(f"**ERROR READING FILE: {exc}**\n")
                else:
                    md.write(text)
                    if not text.endswith("\n"):
                        md.write("\n")

                md.write("```\n\n")


def main() -> None:
    ap = argparse.ArgumentParser(
        prog="mdump",
        description="Recursively collects source files and exports them into a single Markdown document.",
    )
    ap.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Root directory to scan (default: current directory).",
    )
    ap.add_argument(
        "-I",
        "--ignore-dirs",
        metavar="REGEX",
        help="Regular expression for directories to ignore.",
    )
    ap.add_argument(
        "-E",
        "--extensions",
        metavar="REGEX",
        help="Regular expression for file extensions to include (no dot).",
    )
    ap.add_argument(
        "-o", "--output", default="dump.md", help="Path to the output Markdown file."
    )
    args = ap.parse_args()

    root = pathlib.Path(args.root).resolve()
    output = pathlib.Path(args.output).resolve()

    ignore_re = _compile(args.ignore_dirs)
    ext_re = _compile(args.extensions)

    generate_markdown(root, ignore_re, ext_re, output)
    print(f"✔ Generated {output.relative_to(pathlib.Path.cwd())}")


if __name__ == "__main__":
    main()

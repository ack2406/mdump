# mdump

**mdump** is a CLI tool that recursively scans source code directories and exports the contents of selected files into a single, structured Markdown document.

This tool was created to simplify sharing full project context with generative AI systems, making it easier to perform code reviews, debugging, or generate suggestions using LLMs.

## Features

- Recursively walks through project directories
- Skips selected folders using regex filters
- Includes only files matching specific extensions
- Outputs one clean, readable `.md` file with paths and syntax-highlighted code blocks

## Installation

You can install `mdump` from a built wheel:

```bash
uv tool install dist/mdump-1.0.0-py3-none-any.whl
```

Or run it directly from the wheel without installing:

```bash
uvx dist/mdump-1.0.0-py3-none-any.whl
```

Once installed, `mdump` can be used globally:

```bash
mdump --help
```

## Usage

```bash
mdump -I 'bin|obj|node_modules' -E 'cs|json|csproj|sln' -o sources.md
```

### Arguments

- `-I`, `--ignore-dirs`: Regex pattern to ignore folders (e.g., `bin|obj|node_modules`)
- `-E`, `--extensions`: Regex pattern to match file extensions (e.g., `cs|json`)
- `-o`, `--output`: Path to output Markdown file (default: `dump.md`)
- `root`: Optional root path to start scanning (default: current directory)

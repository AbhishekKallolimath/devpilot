from pathlib import Path


EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
}


def get_project_files():
    """Return project files excluding unnecessary directories."""
    project_root = Path.cwd()

    return [
        file
        for file in project_root.rglob("*")
        if file.is_file()
        and not any(part in EXCLUDED_DIRS for part in file.parts)
    ]


def count_python_files():
    """Count Python files in the project."""
    return sum(
        1 for file in get_project_files()
        if file.suffix == ".py"
    )


def count_markdown_files():
    """Count Markdown files in the project."""
    return sum(
        1 for file in get_project_files()
        if file.suffix == ".md"
    )


def count_json_files():
    """Count JSON files in the project."""
    return sum(
        1 for file in get_project_files()
        if file.suffix == ".json"
    )


def count_total_files():
    """Count all project files."""
    return len(get_project_files())


def count_directories():
    """Count project directories excluding unnecessary directories."""
    project_root = Path.cwd()

    return sum(
        1
        for folder in project_root.rglob("*")
        if folder.is_dir()
        and not any(part in EXCLUDED_DIRS for part in folder.parts)
    )


def count_lines_of_code():
    """Count lines of code in Python files."""
    total_lines = 0

    for file in get_project_files():
        if file.suffix != ".py":
            continue

        try:
            with file.open("r", encoding="utf-8") as f:
                total_lines += sum(1 for _ in f)
        except (UnicodeDecodeError, PermissionError):
            continue

    return total_lines
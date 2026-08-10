from pathlib import Path


def count_python_files():
    """
    Count all Python (.py) files in the current project.
    """
    project_root = Path.cwd()

    python_files = list(project_root.rglob("*.py"))

    return len(python_files)


def count_markdown_files():
    """
    Count all Markdown (.md) files in the current project.
    """
    project_root = Path.cwd()

    markdown_files = list(project_root.rglob("*.md"))

    return len(markdown_files)


def count_json_files():
    """
    Count all JSON (.json) files in the current project.
    """
    project_root = Path.cwd()

    json_files = list(project_root.rglob("*.json"))

    return len(json_files)


def count_total_files():
    """
    Count all files in the current project.
    """
    project_root = Path.cwd()

    total_files = [
        file
        for file in project_root.rglob("*")
        if file.is_file()
    ]

    return len(total_files)


def count_directories():
    """
    Count all directories in the current project.
    """
    project_root = Path.cwd()

    directories = [
        folder
        for folder in project_root.rglob("*")
        if folder.is_dir()
    ]

    return len(directories)


def count_lines_of_code():
    """
    Count the total number of lines in Python files.
    """
    project_root = Path.cwd()
    total_lines = 0

    python_files = project_root.rglob("*.py")

    for file in python_files:
        try:
            with file.open("r", encoding="utf-8") as f:
                total_lines += sum(1 for _ in f)
        except (UnicodeDecodeError, PermissionError):
            continue

    return total_lines
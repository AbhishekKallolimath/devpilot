from pathlib import Path


IMPORTANT_FILES = [
    "README.md",
    ".gitignore",
    "requirements.txt",
    "LICENSE",
    "Dockerfile",
    "docker-compose.yml",
]


def check_project_files():
    """
    Check whether important project files exist.
    """

    root = Path.cwd()

    results = {}

    for file in IMPORTANT_FILES:
        results[file] = (root / file).exists()

    return results
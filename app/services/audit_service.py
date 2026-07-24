from pathlib import Path


def check_project_files():
    """
    Check whether important project files exist.
    """

    files = [
        "README.md",
        ".gitignore",
        "requirements.txt",
        "LICENSE",
        "Dockerfile",
        "docker-compose.yml",
    ]

    results = {}

    root = Path.cwd()

    for file in files:
        results[file] = (root / file).exists()

    return results
from pathlib import Path



IMPORTANT_ITEMS = {
    "README.md": "file",
    "LICENSE": "file",
    ".gitignore": "file",
    "requirements.txt": "file",
    "Dockerfile": "file",
    "tests": "directory",
    ".github/workflows": "directory",
}


def check_project_files():
    root = Path.cwd()
    results = {}

    for item, item_type in IMPORTANT_ITEMS.items():
        path = root / item

        if item_type == "file":
            results[item] = path.is_file()
        else:
            results[item] = path.is_dir()

    return results
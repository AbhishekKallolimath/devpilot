from pathlib import Path


def scan_project():
    root = Path.cwd()

    env_files = list(root.rglob(".env"))

    return {
        "status": "Completed",
        "files_scanned": len(list(root.rglob("*"))),
        "secrets_found": len(env_files),
        "env_files": env_files,
    }
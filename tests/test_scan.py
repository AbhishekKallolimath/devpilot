import re
from pathlib import Path


# Common hard-coded secret patterns
PATTERNS = {
    "API_KEY": r"""(?i)\bAPI[_-]?KEY\s*[:=]\s*['"][^'"]{8,}['"]""",
    "PASSWORD": r"""(?i)\bPASSWORD\s*[:=]\s*['"][^'"]{4,}['"]""",
    "SECRET_KEY": r"""(?i)\bSECRET[_-]?KEY\s*[:=]\s*['"][^'"]{8,}['"]""",
    "TOKEN": r"""(?i)\bTOKEN\s*[:=]\s*['"][^'"]{8,}['"]""",
    "AWS_ACCESS_KEY": r"\bAKIA[0-9A-Z]{16}\b",
}


# Directories that should not be scanned
EXCLUDED_DIRECTORIES = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
}


# File types that can contain hard-coded secrets
SCANNABLE_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".java",
    ".c",
    ".cpp",
    ".h",
    ".hpp",
    ".php",
    ".go",
    ".rs",
    ".rb",
    ".json",
    ".yaml",
    ".yml",
    ".xml",
    ".properties",
    ".ini",
    ".cfg",
    ".conf",
    ".txt",
}


def is_excluded(file: Path) -> bool:
    """Check whether a file belongs to an excluded directory."""

    return any(
        part in EXCLUDED_DIRECTORIES
        for part in file.parts
    )


def scan_project():
    """Scan the current project for potential secrets."""

    root = Path.cwd()

    env_files = []
    secret_matches = []

    files_scanned = 0

    for file in root.rglob("*"):

        # Skip directories
        if not file.is_file():
            continue

        # Skip excluded directories
        if is_excluded(file):
            continue

        # Detect .env files BEFORE extension filtering
        if file.name == ".env":
            env_files.append(file)

        # Scan only supported text/code files
        if (
            file.name != ".env"
            and file.suffix.lower() not in SCANNABLE_EXTENSIONS
        ):
            continue

        files_scanned += 1

        try:
            content = file.read_text(
                encoding="utf-8",
                errors="ignore",
            )
        except (PermissionError, OSError):
            continue

        # Check for potential secrets
        for secret_type, pattern in PATTERNS.items():

            if re.search(pattern, content):
                secret_matches.append(
                    {
                        "type": secret_type,
                        "file": file,
                    }
                )

    # Remove duplicate findings
    unique_matches = []
    seen = set()

    for match in secret_matches:

        key = (
            match["type"],
            str(match["file"]),
        )

        if key not in seen:
            seen.add(key)
            unique_matches.append(match)

    # Determine files containing findings
    finding_files = {
        str(file)
        for file in env_files
    }

    finding_files.update(
        str(match["file"])
        for match in unique_matches
    )

    total_findings = len(env_files) + len(unique_matches)

    return {
        "status": "Completed",
        "files_scanned": files_scanned,
        "files_with_findings": len(finding_files),
        "secrets_found": total_findings,
        "env_files": env_files,
        "secret_matches": unique_matches,
    }
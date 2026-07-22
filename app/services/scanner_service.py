import os
import re

PATTERNS = {
    "OpenAI API Key": r"sk-[A-Za-z0-9]{20,}",
    "GitHub Token": r"ghp_[A-Za-z0-9]{36}",
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
}


def scan_directory(path="."):
    findings = []

    for root, _, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)

            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                for name, pattern in PATTERNS.items():
                    if re.search(pattern, content):
                        findings.append((filepath, name))

            except Exception:
                pass

    return findings
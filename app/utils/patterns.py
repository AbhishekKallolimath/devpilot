SECRET_PATTERNS = {
    "OpenAI API Key": r"sk-[A-Za-z0-9]{20,}",
    "GitHub Token": r"ghp_[A-Za-z0-9]{36}",
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "Generic API Key": r"API_KEY\s*=\s*[\"']?.+[\"']?",
    "Password": r"PASSWORD\s*=\s*[\"']?.+[\"']?",
}
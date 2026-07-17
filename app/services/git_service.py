import subprocess


def check_git():
    try:
        result = subprocess.run(
            ["git", "--version"],
            capture_output=True,
            text=True,
            check=True,
        )

        return True, result.stdout.strip()

    except:
        return False, "Git Not Installed"
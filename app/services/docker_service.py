import subprocess


def check_docker():
    try:
        result = subprocess.run(
            ["docker", "--version"],
            capture_output=True,
            text=True,
            check=True,
        )

        version = result.stdout.strip().replace("Docker version ", "")

        return True, version

    except FileNotFoundError:
        return False, "Docker is not installed."

    except subprocess.CalledProcessError:
        return False, "Docker command failed."
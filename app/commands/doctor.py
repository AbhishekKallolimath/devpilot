import platform
import typer

from rich.console import Console
from rich.table import Table

from app.services.git_service import check_git
from app.services.docker_service import check_docker


doctor_app = typer.Typer()
console = Console()


@doctor_app.callback(invoke_without_command=True)
def doctor():
    """
    Check system health.
    """

    table = Table(title="🚀 DevPilot System Doctor")

    table.add_column("Item", style="cyan")
    table.add_column("Status", style="green")

    # Operating System
    table.add_row(
        "Operating System",
        f"{platform.system()} {platform.release()}"
    )

    # Python
    table.add_row(
        "Python Version",
        platform.python_version()
    )

    # Git
    git_installed, git_version = check_git()

    if git_installed:
        table.add_row(
            "Git",
            f"✓ {git_version}"
        )
    else:
        table.add_row(
            "Git",
            "✗ Not Installed"
        )

    # Docker
    docker_installed, docker_version = check_docker()

    if docker_installed:
        table.add_row(
            "Docker",
            f"✓ {docker_version}"
        )
    else:
        table.add_row(
            "Docker",
            "✗ Docker not installed"
        )

    console.print(table)
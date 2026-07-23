import platform
import typer

from rich.console import Console
from rich.table import Table

from app.services.git_service import check_git
from app.services.docker_service import check_docker


doctor_app = typer.Typer()
console = Console()


@doctor_app.callback()
def doctor():
    """
    Check system health.
    """

    table = Table(title="🚀 DevPilot System Doctor")

    table.add_column("Item")
    table.add_column("Status")

    table.add_row(
        "Operating System",
        f"{platform.system()} {platform.release()}"
    )

    table.add_row(
        "Python Version",
        platform.python_version()
    )

    git_installed, git_version = check_git()

    table.add_row(
        "Git",
        git_version if git_installed else "Not Installed"
    )

    docker_installed, docker_version = check_docker()

    table.add_row(
        "Docker",
        docker_version
    )

    console.print(table)
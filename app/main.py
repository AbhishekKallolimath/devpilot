import platform
import typer
from rich.console import Console
from rich.table import Table

from app.services.git_service import check_git
from app.services.docker_service import check_docker

app = typer.Typer()
console = Console()


@app.command()
def doctor():
    """Check the basic system information."""

    table = Table(title="🚀 DevPilot System Doctor")

    table.add_column("Item", style="cyan")
    table.add_column("Status", style="green")

    # Operating System
    table.add_row(
        "Operating System",
        f"{platform.system()} {platform.release()}"
    )

    # Python Version
    table.add_row(
        "Python Version",
        platform.python_version()
    )

    # Git
    git_installed, git_version = check_git()

    if git_installed:
        table.add_row("Git", git_version)
    else:
        table.add_row("Git", "Not Installed")

    # Docker
    docker_installed, docker_version = check_docker()

    if docker_installed:
        table.add_row("Docker", docker_version)
    else:
        table.add_row("Docker", docker_version)

    console.print(table)
    console.print("\n[bold green]DevPilot is running successfully![/bold green]")


if __name__ == "__main__":
    app()
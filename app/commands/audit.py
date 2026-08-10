import typer

from rich.console import Console
from rich.table import Table

from app.services.audit_service import (
    check_project_files,
    is_git_repository,
)


audit_app = typer.Typer()
console = Console()


@audit_app.callback(invoke_without_command=True)
def audit():
    """
    Audit the current project.
    """

    results = check_project_files()

    table = Table(title="📋 DevPilot Project Audit")

    table.add_column("File", style="cyan")
    table.add_column("Status", style="green")

    score = 0

    console.print("\n[bold cyan]Version Control[/bold cyan]")

    if is_git_repository():
        console.print("✅ Git repository detected")
    else:
        console.print("❌ Not a Git repository")

    for file, exists in results.items():

        if exists:
            status = "✅ Found"
            score += 1
        else:
            status = "❌ Missing"

        table.add_row(file, status)

    console.print(table)

    if results:
        percentage = int((score / len(results)) * 100)
    else:
        percentage = 0

    console.print(
        f"\n[bold cyan]Project Health:[/bold cyan] {percentage}/100"
    )
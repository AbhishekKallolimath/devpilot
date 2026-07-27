import typer

from rich.console import Console
from rich.table import Table

from app.services.audit_service import check_project_files

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

    for file, exists in results.items():

        if exists:
            status = "✅ Found"
            score += 1
        else:
            status = "❌ Missing"

        table.add_row(file, status)

    console.print(table)

    percentage = int((score / len(results)) * 100)

    console.print(f"\n[bold cyan]Project Health:[/bold cyan] {percentage}/100")
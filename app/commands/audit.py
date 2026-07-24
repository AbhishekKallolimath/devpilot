import typer
from rich.console import Console
from rich.table import Table

from app.services.audit_service import check_project_files

audit_app = typer.Typer()
console = Console()


@audit_app.callback(invoke_without_command=True)
def audit():
    """Audit the current project."""

    results = check_project_files()

    table = Table(title="📋 DevPilot Project Audit")

    table.add_column("File", style="cyan")
    table.add_column("Status", style="green")

    for file, exists in results.items():
        status = "✅ Found" if exists else "❌ Missing"
        table.add_row(file, status)

    console.print(table)
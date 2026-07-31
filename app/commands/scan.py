import typer

from rich.console import Console
from rich.table import Table

from app.services.scan_service import scan_project

scan_app = typer.Typer()
console = Console()


@scan_app.callback(invoke_without_command=True)
def scan():
    """
    Scan the current project for secrets.
    """

    result = scan_project()

    table = Table(title="🔍 DevPilot Secret Scanner")

    table.add_column("Item", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Status", result["status"])
    table.add_row("Files Scanned", str(result["files_scanned"]))
    table.add_row("Secrets Found", str(result["secrets_found"]))

    console.print(table)
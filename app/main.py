import typer
import platform
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()


@app.command()
def doctor():
    """Check the basic system information."""

    table = Table(title="🚀 DevPilot System Doctor")

    table.add_column("Item", style="cyan")
    table.add_column("Status", style="green")

    table.add_row("Operating System", f"{platform.system()} {platform.release()}")
    table.add_row("Python Version", platform.python_version())

    console.print(table)
    console.print("\n[bold green]DevPilot is running successfully![/bold green]")


if __name__ == "__main__":
    app()
import typer

from app.commands.doctor import doctor_app
from app.commands.audit import audit_app
from app.commands.scan import scan_app
from app.commands.stats import stats_app
from rich.console import Console


VERSION = "0.1.0"

@app.command()
@app.command()
def info():
    """Display information about DevPilot."""

    console.print("\n[bold cyan]🚀 DevPilot[/bold cyan]")
    console.print("Automated Project Health & Security CLI")
    console.print(f"[bold]Version:[/bold] {VERSION}")

    console.print("\n[bold yellow]Features[/bold yellow]")
    console.print("• System Health Checks")
    console.print("• Project Auditing")
    console.print("• Secret Scanning")
    console.print("• Project Statistics")
    console.print("• Git Repository Validation")

app = typer.Typer()
console = Console()

app.add_typer(doctor_app, name="doctor")
app.add_typer(audit_app, name="audit")
app.add_typer(scan_app, name="scan")
app.add_typer(stats_app, name="stats")


@app.command()
def version():
    """Show the DevPilot version."""
    print(f"DevPilot v{VERSION}")


if __name__ == "__main__":
    app()
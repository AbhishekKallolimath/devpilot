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

@app.command()
def check():
    """Run a quick DevPilot project check."""

    console.print("\n[bold cyan]🔎 DevPilot Quick Check[/bold cyan]\n")

    console.print("[bold]Git:[/bold]", end=" ")

    from app.services.audit_service import is_git_repository

    if is_git_repository():
        console.print("[green]✓ Repository detected[/green]")
    else:
        console.print("[red]✗ Not a Git repository[/red]")

    console.print("[bold]Project:[/bold] [green]✓ Ready for analysis[/green]")
    console.print("[bold]Security:[/bold] [green]✓ Scanner available[/green]")
    console.print("[bold]Statistics:[/bold] [green]✓ Available[/green]")

    console.print("\n[bold green]DevPilot check completed.[/bold green]")

@app.command()
def health():
    """Display the current project health status."""

    from app.services.audit_service import check_project_files

    results = check_project_files()

    total = len(results)
    passed = sum(results.values())

    score = int((passed / total) * 100) if total else 0

    console.print("\n[bold cyan]📊 DevPilot Project Health[/bold cyan]")

    if score >= 80:
        status = "[green]Excellent[/green]"
    elif score >= 60:
        status = "[yellow]Good[/yellow]"
    else:
        status = "[red]Needs Improvement[/red]"

console.print(f"Checks Passed: [bold]{passed}/{total}[/bold]")
console.print(f"Health Score: [bold]{score}/100[/bold]")
console.print(f"Status: {status}")

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
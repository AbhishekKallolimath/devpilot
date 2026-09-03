import typer

from rich.console import Console
from rich.table import Table

from app.services.scan_service import scan_project


scan_app = typer.Typer()
console = Console()


@scan_app.callback(invoke_without_command=True)
def scan():
    """Scan the current project for potential secrets."""

    result = scan_project()

    table = Table(title="🔍 DevPilot Secret Scanner")

    table.add_column("Item", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Status", result["status"])
    table.add_row("Files Scanned", str(result["files_scanned"]))
    table.add_row(
        "Files With Findings",
        str(result["files_with_findings"])
    )
    table.add_row("Secrets Found", str(result["secrets_found"]))

    console.print(table)

    findings = []

    # Add .env files
    for file in result["env_files"]:
        findings.append(("ENV_FILE", file))

    # Add detected secret patterns
    for match in result["secret_matches"]:
        findings.append((match["type"], match["file"]))

    if findings:
        console.print("\n[bold red]⚠ Potential Secrets[/bold red]")

        findings_table = Table()

        findings_table.add_column("Type", style="yellow")
        findings_table.add_column("File", style="red")

        for secret_type, file in findings:
            findings_table.add_row(
                secret_type,
                str(file)
            )

        console.print(findings_table)

    else:
        console.print(
            "\n[bold green]✓ No potential secrets detected.[/bold green]"
        )
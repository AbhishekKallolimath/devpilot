import typer

from rich.console import Console
from rich.table import Table

from app.services.project_stats_service import (
    count_python_files,
    count_markdown_files,
    count_json_files,
    count_total_files,
    count_directories,
    count_lines_of_code,
)

stats_app = typer.Typer()
console = Console()


@stats_app.callback(invoke_without_command=True)
def stats():
    """
    Display project statistics.
    """

    table = Table(title="📊 DevPilot Project Statistics")

    table.add_column("Metric", style="cyan")
    table.add_column("Count", style="green")

    table.add_row("Python Files", str(count_python_files()))
    table.add_row("Markdown Files", str(count_markdown_files()))
    table.add_row("JSON Files", str(count_json_files()))
    table.add_row("Total Files", str(count_total_files()))
    table.add_row("Directories", str(count_directories()))
    table.add_row("Lines of Code", str(count_lines_of_code()))

    console.print(table)
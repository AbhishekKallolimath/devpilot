import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def hello():
    """Display welcome message."""
    console.print("[bold green]Welcome to DevPilot! 🚀[/bold green]")


if __name__ == "__main__":
    app()
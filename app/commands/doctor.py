from rich.console import Console
from app.services.system import get_os

console = Console()


def run():
    console.print("[bold cyan]DevPilot System Doctor[/bold cyan]\n")

    console.print(f"Operating System : {get_os()}")
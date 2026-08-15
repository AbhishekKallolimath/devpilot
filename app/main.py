import typer

from app.commands.doctor import doctor_app
from app.commands.audit import audit_app
from app.commands.scan import scan_app
from app.commands.stats import stats_app


VERSION = "0.1.0"

app = typer.Typer()

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
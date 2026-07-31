import typer

from app.commands.doctor import doctor_app
from app.commands.audit import audit_app
from app.commands.scan import scan_app

app = typer.Typer()

app.add_typer(doctor_app, name="doctor")
app.add_typer(audit_app, name="audit")
app.add_typer(scan_app, name="scan")


if __name__ == "__main__":
    app()
import typer

from app.commands.doctor import doctor_app
from app.commands.audit import audit_app

app = typer.Typer()

app.add_typer(doctor_app, name="doctor")
app.add_typer(audit_app, name="audit")

if __name__ == "__main__":
    app()
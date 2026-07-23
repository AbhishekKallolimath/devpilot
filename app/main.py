import typer

from app.commands.doctor import doctor_app


app = typer.Typer()


app.add_typer(
    doctor_app,
    name="doctor"
)


if __name__ == "__main__":
    app()
from pathlib import Path

import typer

app = typer.Typer()


@app.command()
def echo_path(name: Path):
    typer.echo(f"Path: {name}")


@app.command()
def echo_str(name: str):
    typer.echo(f"String: {name}")


if __name__ == "__main__":
    app()

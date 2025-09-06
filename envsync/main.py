import typer
from pathlib import Path
import os

app = typer.Typer(help="A CLI tool to manage and synchronize .env files.")


@app.command()
def switch(source: str):
    """
    Replace the current .env file with the given source file.
    """
    source_path = Path(source)
    target_path = Path(".env")

    if not source_path.exists():
        typer.echo(f"❌ The file {source} does not exist.")
        raise typer.Exit(code=1)

    target_path.write_text(source_path.read_text())
    typer.echo(f"✅ .env has been replaced with {source}.")


@app.command()
def add(variable: str):
    """
    Add a variable to all .env* files in the current directory.

    Examples:
        envsync add "API_KEY=12345"
        envsync add "DEBUG"
    """
    env_files = [f for f in os.listdir('.') if f.startswith('.env')]

    # Handle either KEY=VALUE or KEY (empty value)
    if "=" in variable:
        line_to_add = variable
    else:
        line_to_add = f"{variable}="

    for env_file in env_files:
        file_path = os.path.join('.', env_file)

        with open(file_path, 'r') as f:
            lines = f.read().splitlines()

        if line_to_add not in lines:
            with open(file_path, 'a') as f:
                f.write(f'\n{line_to_add}')
            typer.echo(f"✅ Added '{line_to_add}' to {env_file}")
        else:
            typer.echo(f"ℹ️ '{line_to_add}' already exists in {env_file}")


@app.command()
def sync(source: str, target: str):
    """
    Synchronize two .env files by adding missing keys from each other.

    Example:
        envsync sync dev prod
        (syncs .env.dev and .env.prod)
    """
    def load_env(path):
        env = {}
        with open(path, "r") as f:
            for line in f.read().splitlines():
                if "=" in line and not line.startswith("#"):
                    k, v = line.split("=", 1)
                    env[k.strip()] = v.strip()
        return env

    source_file = f".env.{source}"
    target_file = f".env.{target}"

    if not Path(source_file).exists() or not Path(target_file).exists():
        typer.echo("❌ One of the files does not exist.")
        raise typer.Exit(code=1)

    source_env = load_env(source_file)
    target_env = load_env(target_file)

    # Copy missing keys from source -> target
    with open(target_file, "a") as f:
        for k, v in source_env.items():
            if k not in target_env:
                f.write(f"\n{k}={v}")
                typer.echo(f"➕ Added {k} to {target_file}")

    # Copy missing keys from target -> source
    with open(source_file, "a") as f:
        for k, v in target_env.items():
            if k not in source_env:
                f.write(f"\n{k}={v}")
                typer.echo(f"➕ Added {k} to {source_file}")

    typer.echo(f"✅ {source_file} and {target_file} are now synchronized.")


if __name__ == "__main__":
    app()

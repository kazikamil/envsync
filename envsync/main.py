import typer
from pathlib import Path
import os

app = typer.Typer()

@app.command()
def switch(source: str):
    """
    Remplace le .env par le fichier source donné.
    """
    source_path = Path(source)
    target_path = Path(".env")

    if not source_path.exists():
        typer.echo(f"❌ Le fichier {source} n'existe pas.")
        raise typer.Exit(code=1)

    target_path.write_text(source_path.read_text())
    typer.echo(f"✅ .env remplacé par {source}.")

@app.command()
def add(variable:str):
    """
    Remplace le .env par le fichier source donné.
    """
    env_files = [f for f in os.listdir('.') if f.startswith('.env')]
    line_to_add = f"{variable}={variable}"

    for env_file in env_files:
     file_path = os.path.join('.', env_file)

     # 🗂️ Vérifier si la ligne existe déjà (optionnel)
     with open(file_path, 'r') as f:
        lines = f.read().splitlines()

        if line_to_add not in lines:
         with open(file_path, 'a') as f:
            f.write(f'\n{line_to_add}')
         print(f"Ligne ajoutée à {env_file}")
        else:
         print(f"Ligne déjà présente dans {env_file}")


@app.command()
def sync(source: str, target: str):
    """
    Synchroniser deux .env files
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

    source_env = load_env(source_file)
    target_env = load_env(target_file)

    # Copier les clés manquantes de source -> target
    with open(target_file, "a") as f:
        for k, v in source_env.items():
            if k not in target_env:
                f.write(f"\n{k}={v}")

    # Copier les clés manquantes de target -> source
    with open(source_file, "a") as f:
        for k, v in target_env.items():
            if k not in source_env:
                f.write(f"\n{k}={v}")

    print(f"✅ Les fichiers {source_file} et {target_file} sont synchronisés")
            

if __name__ == "__main__":
    app()

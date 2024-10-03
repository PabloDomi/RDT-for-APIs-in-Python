import time
from InquirerPy import prompt
from tqdm import tqdm
import click
from colorama import Fore
import colorama
from rdt import start_project


def cli_selector(name):
    # Usamos InquirerPy para las selecciones interactivas
    questions = [
        {
            "type": "list",
            "message": "Select a framework",
            "choices": ["FastAPI", "Django-Rest", "Tornado", "Sanic", "Falcon", "Hug", "Flask-Restx"],
        },
        # Si la seleccion de framework es Django-Rest, no se mostrará la opción de ORM
        {
            "type": "list",
            "message": "Select an ORM",
            "choices": ["SQLAlchemy", "TortoiseORM", "Pewee"],
            "when": lambda answers: answers[0] != "Django-Rest"
        },
        {
            "type": "list",
            "message": "Select the database type",
            "choices": ["PostgreSQL", "MySQL", "SQLite"],
        },
    ]

    results = prompt(questions)

    framework = results[0]  # Ahora accedemos al valor usando la clave
    if framework == "Django-Rest":
        orm = "DjangoORM"
    else:
        orm = results[1]  # Corregido acceso como diccionario
    db = results[2]  # Corregido acceso como diccionario

    click.echo("\n")
    click.echo(f"{Fore.CYAN} Creando proyecto '{name}' con {framework}, usando {orm} y {db}")
    click.echo("\n")

    # Mostrar un loader mientras carga
    for _ in tqdm(range(2), desc="Cargando", bar_format="{l_bar}{bar} [time left: {remaining}]"):
        time.sleep(1)

    click.echo("\n")

    return framework, orm, db


colorama.init(autoreset=True)


@click.group()
def cli():
    """Herramienta para la creación rápida de APIs"""
    pass


@cli.command()
@click.option(
    '--name',
    prompt=Fore.GREEN + 'Nombre del proyecto',
    help='El nombre del proyecto o API'
)
@click.option(
    '--auth',
    prompt=Fore.GREEN + '¿Deseas rutas protegidas (JWT)?',
    type=click.Choice(['Yes', 'No', 'y', 'n'], case_sensitive=False),
    help='Añadir rutas protegidas con JWT'
)
@click.option(
    '--github',
    prompt=Fore.GREEN + '¿Deseas crear un repositorio Git?',
    type=click.Choice(['Yes', 'No', 'y', 'n'], case_sensitive=False),
    help='Subir el proyecto a GitHub'
)
def create_project(name, auth, github):
    framework, orm, db = cli_selector(name)
    start_project(name, framework, orm, db, auth, github)


# Asegúrate de que el grupo de comandos CLI se ejecute
if __name__ == '__main__':
    cli()

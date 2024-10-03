import os
import click
from colorama import Fore
import time


def show_virtualenv_tutorial():
    if os.name == 'nt':
        click.echo("\n")
        click.echo(Fore.LIGHTMAGENTA_EX + 'Para activar el entorno virtual, ejecuta los siguientes comandos:')
        click.echo('\tpython -m venv env\n\tsource env\\Scripts\\activate')
    else:
        click.echo('En macOS/Linux: \npython3 -m venv env\nsource env/bin/activate')

    time.sleep(0.5)
    click.echo("\n")
    click.echo(Fore.LIGHTRED_EX + 'Ejecuta "pip install -r requirements.txt" para instalar las dependencias.')
    click.echo("\n")
    click.echo(Fore.LIGHTWHITE_EX + 'Asegurate de crear tu archivo .env con las variables de entorno necesarias. Tienes un ejemplo en el archivo .env-example.\n')
    click.echo(Fore.LIGHTGREEN_EX + '¡Listo! Ahora puedes empezar a trabajar en tu proyecto.\n')
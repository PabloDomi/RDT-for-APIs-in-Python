import click
import time
from colorama import Fore


def create_readme():
    with open('README.md', 'w') as f:
        f.write('# Proyecto API generado con RDT\n\nEste proyecto ha sido generado automáticamente usando la herramienta RDT.\n')
    click.echo(Fore.YELLOW + 'README.md generado.')
    time.sleep(0.5)

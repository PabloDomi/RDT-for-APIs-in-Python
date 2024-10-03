import os
import click
from colorama import Fore


def setup_github_repo(name):
    os.system('git init')
    os.system('git add .')
    os.system(f'git commit -m "Initial commit for {name}"')
    click.echo(Fore.GREEN + '\nRepositorio Git inicializado.')

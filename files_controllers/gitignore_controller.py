import click
import time
from colorama import Fore


def create_gitignore():
    with open('.gitignore', 'w') as f:
        f.write('''env/
.env
.flaskenv
__pycache__/
*.pyc
instance/
''')
    click.echo(Fore.YELLOW + '.gitignore generado.')
    time.sleep(0.5)

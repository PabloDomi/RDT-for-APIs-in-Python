import click
import time
from colorama import Fore


def create_app_file(auth):
    with open('app.py', 'w') as f:
        f.write('''from src import create_app
app = create_app()
''')

        f.write('''
if __name__ == '__main__':
    app.run(port='5300', debug=True)
''')

    click.echo(Fore.YELLOW + 'Archivo app.py generado.')
    time.sleep(0.5)

import click
import time
from colorama import Fore


def create_license():
    with open('LICENSE', 'w') as f:
        f.write('''MIT License

Copyright (c) 2024 [Tu Nombre]

Permission is hereby granted, free of charge, to any person obtaining a copy...
''')
    click.echo(Fore.YELLOW + 'LICENSE de tipo MIT generado.')
    time.sleep(0.5)

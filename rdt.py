from controllers.github_controller import setup_github_repo
from controllers.venv_tuto_controller import show_virtualenv_tutorial
from controllers.folder_structure_controller import create_folder_structure


def start_project(name, framework, orm, db, auth, github):
    """Crea un proyecto API automáticamente"""

    # Lógica para crear la estructura del proyecto
    create_folder_structure(name, framework, orm, auth, db)

    if github.lower() in ['yes', 'y']:
        setup_github_repo(name)

    show_virtualenv_tutorial()

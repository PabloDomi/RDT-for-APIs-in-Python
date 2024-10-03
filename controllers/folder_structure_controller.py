import os
from files_controllers.requirements_controller import create_requirements_txt
from files_controllers.env_example_controller import create_env_example
from files_controllers.config_controller import create_config_file
from files_controllers.extensions_controller import create_extensions_file
from files_controllers.init_controller import create_init_file
from files_controllers.example_files_controller import create_example_files
from files_controllers.gitignore_controller import create_gitignore
from files_controllers.app_file_controller import create_app_file
from files_controllers.license_controller import create_license
from files_controllers.readme_controller import create_readme


# Define todas las funciones de creación de archivos
def create_folder_structure(name, framework, orm, auth, db):

    if auth in ['yes', 'y']:
        auth = 'Sí'
    elif auth in ['no', 'n']:
        auth = 'No'

    # Crear la carpeta del proyecto
    os.makedirs(name)
    os.chdir(name)

    # Crear carpeta src y subcarpetas
    os.makedirs('src/controllers')
    os.makedirs('src/models')
    os.makedirs('src/routes')
    os.makedirs('src/config')
    os.makedirs('src/services')
    os.makedirs('src/tests')
    os.makedirs('src/utils')

    create_requirements_txt(framework, orm, auth, db)
    create_env_example()
    create_config_file(framework, orm, db)
    create_extensions_file(framework, orm, auth, db)
    create_init_file(auth, framework, db, orm)
    create_example_files(auth, framework, orm)
    create_gitignore()
    create_license()
    create_readme()
    create_app_file(auth)

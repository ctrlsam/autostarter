import os
from autostarter.util import remove_list

"""
Linux-specific functions for managing startup scripts.

A startup script is a script that runs automatically when the system boots up. This module provides
functions for adding and removing startup scripts.
"""

def add(identifier: str, script_location: str, interpreter: str = 'sh',
    system_wide: bool = False, arguments: str = ''):
    """
    Add a new startup script.

    identifier: A unique identifier for the startup script.
    script_location: The path to the script to run as the startup script.
    interpreter: Program to run the script with. Defaults to 'sh'.
    system_wide: If True, the startup script will be added for all users on the system.
                 If False (default), the startup script will be added for the current user only.
    arguments: CLI Arguments to provide to script.
    """
    # Make systemd folder if not exists
    start_dir = _startup_folder(system_wide)
    os.makedirs(start_dir, exist_ok=True)

    start_file = f'{start_dir}/{identifier}'

    # Create shell script
    with open(f'{start_file}.sh', 'w') as f:
        f.write(f'#!/bin/bash\n\n{interpreter} {script_location} {arguments}\n')
    os.chmod(f'{start_file}.sh', 0o755)

    # Create .desktop file
    with open(f'{start_file}.desktop', 'w') as f:
        f.write(f'[Desktop Entry]\nType=Application\nName={identifier}\nExec={start_file}.sh\n')

def remove(identifier: str, system_wide: bool = False) -> bool:
    """
    Remove an existing startup script.

    identifier: The unique identifier of the startup script to remove.
    system_wide: If True, the startup script will be removed for all users on the system.
                 If False (default), the startup script will be removed for the current user only.

    Returns: True if the startup script were removed, False otherwise.
    """
    # Remove desktop and shell script files
    to_delete = [
        f'{_startup_folder(system_wide)}/{identifier}.sh',
        f'{_startup_folder(system_wide)}/{identifier}.desktop'
    ]
    return remove_list(to_delete)

def _startup_folder(system_wide):
    """
    Get directory depending on start up target

    system_wide: If True, the startup script will be added for all users on the system.
                 If False (default), the startup script will be added for the current user only.

    Returns: path to folder
    """
    if system_wide:
        return '/etc/init.d'
    return os.path.expanduser('~/.config/autostart')

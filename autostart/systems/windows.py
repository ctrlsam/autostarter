import os

"""
Windows-specific functions for managing startup scripts.

A startup script is a script that runs automatically when the system boots up. This module provides
functions for adding and removing startup scripts.
"""

def add(identifier: str, script_location: str, interpreter: str = r'cmd \c',
    system_wide: bool = False, arguments: str = '') -> None:
    """
    Add a new startup script.

    identifier: A unique identifier for the startup script.
    script_location: The path to the script to run as the startup script.
    interpreter: Program to run the script with. Defaults to 'cmd'.
    system_wide: If True, the startup script will be added for all users on the system.
                 If False (default), the startup script will be added for the current user only.
    arguments: CLI Arguments to provide to script.
    """
    # Create batch script in autorun directory
    with open(f'{_startup_folder(system_wide)}\\{identifier}.bat', 'w') as f:
        f.write(f'@echo off\n{interpreter} {script_location} {arguments}\n')

def remove(identifier: str, system_wide: bool = False) -> bool:
    """
    Remove an existing startup script.

    identifier: The unique identifier of the startup script to remove.
    system_wide: If True, the startup script will be removed for all users on the system.
                 If False (default), the startup script will be removed for the current user only.

    Returns: True if the startup script was found and successfully removed, False otherwise.
    """
    # Remove batch script from autorun directory
    start_file = f'{_startup_folder(system_wide)}\\{identifier}.bat'

    if os.path.exists(start_file):
        os.remove(start_file)
        return True

    return False

def _startup_folder(system_wide):
    """
    Get directory depending on start up target

    system_wide: If True, the startup script will be added for all users on the system.
                 If False (default), the startup script will be added for the current user only.

    Returns: path to folder
    """
    if system_wide:
        return 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp'
    return os.path.expanduser('~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')

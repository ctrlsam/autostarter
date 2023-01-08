import os
import plistlib

"""
Darwin-specific functions for managing launch agents.

A launch agent is a background process that runs on macOS. This module provides
functions for adding and removing launch agents.
"""

def add(identifier: str, script_location: str, interpreter: str = 'sh',
    system_wide: bool = False, arguments: str = '') -> None:
    """
    Add a new launch agent.

    identifier: A unique identifier for the launch agent.
    script_location: The path to the script to run as the launch agent.
    interpreter: Program to run the script with. Defaults to 'sh'.
    system_wide: If True, the launch agent will be added for all users on the system.
                 If False (default), the launch agent will be added for the current user only.
    arguments: CLI Arguments to provide to script.
    """
    # Create shell script to start program
    start_file = f'{_startup_folder(system_wide)}/{identifier}'
    with open(f'{start_file}.sh', 'w') as f:
        f.write(f'#!/bin/bash\n\n{interpreter} {script_location} {arguments}\n')

    # Script must have execute permissions
    os.chmod(f'{start_file}.sh', 0o755)

    # Create the dictionary for the plist file
    plist = {
        'Label': identifier,
        'ProgramArguments': [f'{start_file}.sh'],
        'RunAtLoad': True
    }

    # Write the plist file
    if hasattr(plistlib, 'dump'):
        with open(f'{start_file}.plist', 'wb') as fp:
            plistlib.dump(plist, fp)
    else: # Support plistlib < python 3.9
        plistlib.writePlist(plist, start_file)

def remove(identifier: str, system_wide: bool = False) -> bool:
    """
    Remove an existing launch agent.

    identifier: The unique identifier of the launch agent to remove.
    system_wide: If True, the launch agent will be removed for all users on the system.
                 If False (default), the launch agent will be removed for the current user only.

    Returns: True if the launch agent was found and successfully removed, False otherwise.
    """
    # Remove plist and shell script files
    to_delete = [
        f'{_startup_folder(system_wide)}/{identifier}.plist',
        f'{_startup_folder(system_wide)}/{identifier}.sh'
    ]

    return all(os.remove(file) for file in to_delete)

def _startup_folder(system_wide: bool) -> str:
    """
    Get the file path for the plist file of the launch agent with the given identifier.

    identifier: The unique identifier of the launch agent.
    system_wide: If True, the plist file will be located in the system-wide directory.
                     If False, the plist file will be located in the current user's directory.

    Returns: The file path of the plist file.
    """
    if system_wide:
        return  '/Library/LaunchAgents'
    return os.path.expanduser('~/Library/LaunchAgents')

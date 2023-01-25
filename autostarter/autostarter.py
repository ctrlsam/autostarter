import functools
import importlib
import platform
import uuid

@functools.lru_cache()
def _get_os_module():
    """
    Returns the OS-specific module for the current operating system.
    """
    return importlib.import_module('autostarter.systems.' + platform.system().lower())

def add(script_location, **kwargs):
    """
    Adds a startup script with the specified parameters.

    Parameters:
    - script_location (str): The location of the script to be added as a startup script.
    - identifier (str, optional): An identifier for the startup script. If not provided, a random UUID will be generated.
    - system_wide (bool, optional): Make program open at start for all users. Requires root/admin privileges.
    - arguments (str, optional): CLI Arguments to provide to script.
    - interpreter (str, optional): Program to run the script with. Defaults to 'cmd' on Windows and 'sh' for unix.

    Returns: The identifier for the added startup script.
    """
    identifier = kwargs.pop('identifier', None)
    if not identifier:
        # Generate a random UUID if no identifier is provided
        identifier = str(uuid.uuid4())

    try:
        os_module = _get_os_module()
        os_module.add(identifier, script_location, **kwargs)
    except AttributeError as err:
        raise OSError('Operating system is not supported.') from err

    return identifier

def remove(identifier, **kwargs):
    """
    Removes the startup script with the specified identifier.

    Parameters:
    - identifier (str): The identifier of the startup script to be removed.
    - system_wide (bool, optional): If true, will try remove a system wide (all user) startup script
    Returns: True if the startup script was successfully removed, False otherwise.
    """
    try:
        os_module = _get_os_module()
        return os_module.remove(identifier, **kwargs)
    except AttributeError as err:
        raise OSError('Operating system is not supported.') from err

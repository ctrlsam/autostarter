import os
from typing import List

def remove_list(to_delete: List[str]) -> bool:
    """Helper to remove list of files.

    Args:
        to_delete (List[str]): List of pathnames of files to remove

    Returns:
        bool: True if successfully purged. If not exists, purge will remain successful.
    """
    for filename in to_delete:
        try:
            os.remove(filename)
        except FileNotFoundError:
            print('File %s tried to be removed, however it was not found', filename)
        except OSError as err:
            print('Exception occurred while removing file: ' + str(err))
            return False

    return True

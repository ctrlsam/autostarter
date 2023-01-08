# Autostarter

A Python module for managing startup scripts across different operating systems, requiring no additional dependencies.

## Installation

To install the module, use `pip`:

```bash
pip install autostarter
```

## Usage

You can use the "add" method to include a startup script, and the "remove" method to remove a startup script.

```python
import autostarter
import sys

# Add a python script
script_location = '/path/to/script.py'
autostarter.add(
    script_location,
    identifier='your-app-name',
    interpreter=sys.executable
)

# Remove a startup script
autostarter.remove('your-app-name')
```

### API Reference

#### `add(script_location, **kwargs) -> str`

Adds a startup script with the specified parameters.

##### Parameters:

- `script_location (str)`: The location of the script to be added as a startup script.
- `identifier (str, optional)`: An identifier for the startup script. If not provided, a random UUID will be generated.
- `system_wide (bool, optional)`: Make program open at start for all users. Requires root/admin privileges.
- `arguments (str, optional)`: CLI Arguments to provide to script.
- `interpreter (str, optional)`: Program to run the script with. See usage for how to run a Python script

##### Returns:

- The identifier for the added startup script

#### `remove(identifier, **kwargs) -> Union[bool, str]`

Removes the startup script with the specified identifier.

##### Parameters:

- `identifier (str)`: The identifier of the startup script to be removed.

##### Returns:

- True if the startup script was successfully removed, False otherwise.

## Supported Operating Systems

Autostarter supports the following operating systems:

- Windows, tested on Windows 11
- MacOS, tested on 13.1
- Linux, tested on Ubuntu 22.04

## Contributing

If you want to contribute to Autostarter, please fork the repository and make your changes in a separate branch. Then, submit a pull request with a detailed description of your changes.

## License

Autostarter is licensed under the MIT License.
See [LICENSE](https://github.com/ctrlsam/autostart/blob/main/LICENSE) for more information.
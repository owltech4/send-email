This project is an automated email script.

The config.json module is used to store your settings so that the credentials are encrypted. Initially, you can keep this file empty or add settings that are not sensitive.


## Initial Setup

Before running the project for the first time, follow these steps to set up the environment:

1. Install the project's dependencies by running `pip install -r requirements.txt` in the terminal.
2. Run the initial setup script with `python setup.py`. This will generate the necessary key for credential encryption and install any remaining dependencies.

After completing these steps, you will be able to run the project normally.

Note: Do not run `generate_key()` repeatedly in your production code, as this would overwrite the existing key, making it impossible to decrypt data encrypted with the previous key.

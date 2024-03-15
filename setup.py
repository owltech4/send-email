import os
import json
from cryptography_utils import generate_key, encrypt_message

def setup_project():
    print("Generating encryption key...")
    generate_key()
    print("Key generated successfully.")

    # Asks the user for the email and password to encrypt
    email = input("Enter your email: ")
    senha = input("Enter your password: ")

    # Encrypts the email and password
    email_criptografado = encrypt_message(email)
    senha_criptografada = encrypt_message(senha)

    # Converts from bytes to a decodable string to store in config.json
    email_criptografado_str = email_criptografado.decode('utf-8')
    senha_criptografada_str = senha_criptografada.decode('utf-8')

    # Updates the config.json with the encrypted information
    config_data = {
        "email": email_criptografado_str,
        "password": senha_criptografada_str,
        "smtp_server": "smtp-mail.outlook.com",
        "smtp_port": 587
    }
    with open('config.json', 'w') as config_file:
        json.dump(config_data, config_file, indent=4)

    print("Encrypted settings saved in config.json.")

    print("Installing project dependencies...")
    os.system('pip install -r requirements.txt')
    print("Dependencies installed successfully.")
    print("Project settings completed.")

if __name__ == "__main__":
    generate_key()
    print("Starting program...")
    print("Program finished.")
    setup_project()

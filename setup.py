import os
import json
from cryptography_utils import generate_key, encrypt_message

def setup_project():
    print("Generating encryption key...")
    generate_key()
    print("Key generated successfully.")

    # Pede ao usuário o e-mail e senha para criptografar
    email = input("Enter your email: ")
    senha = input("Enter your password: ")

    # Criptografa o e-mail e a senha
    email_criptografado = encrypt_message(email)
    senha_criptografada = encrypt_message(senha)

    # Converte de bytes para string decodificável para armazenar no config.json
    email_criptografado_str = email_criptografado.decode('utf-8')
    senha_criptografada_str = senha_criptografada.decode('utf-8')

    # Atualiza o config.json com as informações criptografadas
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

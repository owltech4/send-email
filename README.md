This project is an automated email script.

The config.json module is used to store your settings so that the credentials are encrypted. Initially, you can keep this file empty or add settings that are not sensitive.

PS: Before running your project, execute generate_key() once to generate your secret.key and use encrypt_message() to encrypt your credentials. Store the encrypted values in config.json
Nota: Não execute generate_key() repetidamente no seu código de produção, pois isso sobrescreveria a chave existente, tornando impossível descriptografar os dados criptografados com a chave anterior.


## Configuração Inicial

Antes de executar o projeto pela primeira vez, siga estas etapas para configurar o ambiente:

1. Instale as dependências do projeto executando `pip install -r requirements.txt` no terminal.
2. Execute o script de setup inicial com `python setup.py`. Isso irá gerar a chave necessária para a criptografia das credenciais e instalar quaisquer dependências restantes.

Após completar estes passos, você poderá executar o projeto normalmente.

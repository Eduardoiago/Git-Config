
<img src="/assets/img/title-gitconfig.png" alt="titleNameGitconfig">

> # gitConfig

#### Python Script to Configure git 

O gitConfig é um menu interativo em python para configurar o git em um novo computador. Com o gitConfig você pode configurar o username, email principal, username e email por repositório, o editor, a branch principal e faz o processo de gerar uma nova chave SSH usando o algoritimo Ed25519. Caso seu sistema não suporte o Ed25519, use rsa 4096 para gerar a chave.

Para iniciar as configurações, basta executar o script `gitconfigCLI.py` no terminal e escolher as opções que deseja configurar. As opções nome de usuário local (por repositório) e endereço de e-mail local (por repositório) devem ser configuradas dentro do repositório que está sendo desenvolvido. As demais configurações podem ser feitas em qualquer repositório.

A ferramenta ainda está em desenvolvimento. Todas as configurações do git serão adicionadas, tornando mais rápido para o usuário configurar a nova máquina.
_______

### Installing Git:

- To get started, install Git on your operating system. You can download the appropriate installer for your operating system at https://git-scm.com/.

- Follow the installation instructions provided to complete the process.
_______

## Layout

<img src="" alt="layout">

## Technologies used:

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)&nbsp; 

#### Python libraries

Only the `os` library was used to inject the commands into the terminal.

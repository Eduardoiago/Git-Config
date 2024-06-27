import os

# GIT CONFIG™ | Console 

def set_username():
    username = input("\nDigite seu nome de usuário do Git: ")
    os.system(f'git config --global user.name "{username}"') # Configurar username global.
    print("\nNome de usuário global configurado com sucesso!")
    input("\nPressione ENTER para voltar ao Menu.")

def set_email():
    email = input("\nDigite seu endereço de e-mail do Git: ")
    os.system(f'git config --global user.email "{email}"') # Configurar email global.
    print("\nEndereço de e-mail global configurado com sucesso!")
    input("\nPressione ENTER para voltar ao Menu.")

def set_editor():
    editor = input("\nDigite seu editor de texto preferido para usar com o Git: ")
    os.system(f'git config --global core.editor "{editor}"') # Configurar editor padrão.
    print("\nEditor padrão configurado com sucesso!")
    input("\nPressione ENTER para voltar ao Menu.")

def set_default_branch():
    branch_name = input("\nDigite o nome da branch principal: ")
    os.system(f'git config --global init.defaultBranch {branch_name}') # Configurar branch padrão.
    print("\nBranch principal configurada com sucesso!")
    input("\nPressione ENTER para voltar ao Menu.")

def set_username_repo():
    username = input("\nDigite seu nome de usuário do Git para este repositório: ")
    os.system(f'git config user.name "{username}"') # Configurar username por repositório.
    print("\nNome de usuário local configurado com sucesso!")
    input("\nPressione ENTER para voltar ao Menu.")

def set_email_repo():
    email = input("\nDigite seu endereço de e-mail do Git para este repositório: ")
    os.system(f'git config user.email "{email}"') # Configurar email por repositório.
    print("\nEndereço de e-mail local configurado com sucesso!")
    input("\nPressione ENTER para voltar ao Menu.")

def info():
    clear_screen()
    print(line)
    print("♦ GIT CONFIG™ ♦")
    print(line)
    print("Github: https://github.com/Eduardoiago")
    print("Developed by Eduardo Iago | Versão: 1.0.0\n")
    print("O gitConfig é uma ferramenta desenvolvida em python para configurar o git em uma nova máquina.")
    input("\nPressione ENTER para voltar ao Menu.")

def genssh_key():  
    print("\nSSH CONFIG")
    print("Se você estiver usando um sistema legado que não suporta o algoritmo Ed25519, use RSA 4093.\n")
    print("1. Gerar chave SSH usando \033[3mEd25519\033[m")
    print("2. Gerar chave SSH usando \033[3mRSA 4093\033[m")
    print("3. Voltar ao Menu")
    
    choice = input("\nInsira a opção: ")

    if choice == '1':
        email = input("\nDigite seu email do Github: ")
        os.system(f'ssh-keygen -t ed25519 -C "{email}"') # Gerando uma nova chave SSH Ed25519.
        print("\nChave SSH-Ed25519 gerada com sucesso!")
        print("Para visualizar seus IDs vá até (.ssh) em home.")
    elif choice == '2':
        email_rsa = input("\nDigite seu email do Github: ")
        os.system(f'ssh-keygen -t rsa -b 4096 -C "{email_rsa}"') # Gerando uma nova chave SSH rsa 4096.
        os.system('eval "$(ssh-agent -s)"')
        os.system('ssh-add ~/.ssh/id_rsa')
        print("\nChave SSH RSA 4096 gerada com sucesso!")
        print("Para visualizar seus IDs vá até (.ssh) em home.")
    elif choice == '3':
        main()      
    else:
        print("\nOpção inválida. Por favor, escolha uma opção válida.")

def set_alias(): # Configurar alias.
    alias_name = input("Digite o nome do alias: ")
    command = input("\nDigite o comando Git para associar ao alias: ")
    os.system(f'git config --global alias.{alias_name} "{command}"')
    print(f"Alias '{alias_name}' configurado com sucesso!")

def list_config():
    os.system("git config --list") # Listar todas as configurações do git.

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls") # Limpa a tela do console.

line = 27*"⣿⣿"  
titleMenu = """\033[3m

            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠐⢿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⢀⣴⣿⣦⡀⠙⠉⠻⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀
            ⠀⠀⠀⢀⣴⣿⣿⣿⣿⣇⠀⠀⠀⢽⣿⣿⣿⣿⣦⡀⠀⠀⠀
            ⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⡇⠀⣦⡀⠙⢿⢿⣿⣿⣿⣦⡀⠀
            ⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⡆⠀⠀⠈⢻⣿⣿⣿⣆
            ⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣷⣄⣀⣠⣿⣿⣿⠟⠁
            ⠀⠀⠙⢿⣿⣿⣿⣿⣿⡿⠃⠀⠻⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀
            ⠀⠀⠀⠀⠙⢿⣿⣿⣿⣇⠀⠀⠀⣽⣿⣿⣿⠟⠁⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣷⣶⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

            ♦ GIT CONFIG™ version 1.0 ♦
\033[m"""

def main():
    while True:
        clear_screen()
        print(titleMenu)
        print("\n1. Configurar nome de usuário global")
        print("2. Configurar endereço de e-mail global")
        print("3. Configurar editor padrão")
        print("4. Configurar branch principal")
        print("5. Configurar nome de usuário local (por repositório)")
        print("6. Configurar endereço de e-mail local (por repositório)")
        print("7. Gerar chave SSH (Ed25519 ou rsa 4096)")
        print("8. Configurar alias")
        print("9. Listar as configurações do git")
        print("x. Sair")
        
        choice = input("\nDigite o número da opção desejada: ")
        
        if choice == '1':
            set_username()
        elif choice == '2':
            set_email()
        elif choice == '3':
            set_editor()
        elif choice == '4':
            set_default_branch()        
        elif choice == '5':
            set_username_repo()
        elif choice == '6':
            set_email_repo()
        elif choice == '7':
            genssh_key()
        elif choice == '8':
            set_alias()
        elif choice == '9':
            list_config()
        elif choice == '--info':
            info()
        elif choice == 'x':
            print("\nSaindo do GIT Config...\n")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()

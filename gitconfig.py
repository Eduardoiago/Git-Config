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
        print(line)
        print(titleMenu)
        print(line)
        print("\n1. Configurar nome de usuário global")
        print("2. Configurar endereço de e-mail global")
        print("3. Configurar editor padrão")
        print("4. Configurar branch principal")
        print("5. Configurar nome de usuário local (por repositório)")
        print("6. Configurar endereço de e-mail local (por repositório)")
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

D='\nPressione ENTER para voltar ao Menu.'
B=input
A=print
import os as C
def G():E=B('\nDigite seu nome de usuário do Git: ');C.system(f'git config --global user.name "{E}"');A('\nNome de usuário global configurado com sucesso!');B(D)
def H():E=B('\nDigite seu endereço de e-mail do Git: ');C.system(f'git config --global user.email "{E}"');A('\nEndereço de e-mail global configurado com sucesso!');B(D)
def I():E=B('\nDigite seu editor de texto preferido para usar com o Git: ');C.system(f'git config --global core.editor "{E}"');A('\nEditor padrão configurado com sucesso!');B(D)
def J():E=B('\nDigite o nome da branch principal: ');C.system(f"git config --global init.defaultBranch {E}");A('\nBranch principal configurada com sucesso!');B(D)
def K():E=B('\nDigite seu nome de usuário do Git para este repositório: ');C.system(f'git config user.name "{E}"');A('\nNome de usuário local configurado com sucesso!');B(D)
def L():E=B('\nDigite seu endereço de e-mail do Git para este repositório: ');C.system(f'git config user.email "{E}"');A('\nEndereço de e-mail local configurado com sucesso!');B(D)
def M():F();A(E);A('♦ GIT CONFIG™ ♦');A(E);A('Github: https://github.com/Eduardoiago');A('Developed by Eduardo Iago | Versão: 1.0.0\n');A('O gitConfig é uma ferramenta desenvolvida em python para configurar o git em uma nova máquina.');B(D)
def N():C.system('git config --list')
def F():C.system('clear'if C.name=='posix'else'cls')
E=27*'⣿⣿'
O='\x1b[3m\n\n            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n            ⠀⠀⠀⠀⠀⠀⠀⠀⠐⢿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀\n            ⠀⠀⠀⠀⠀⢀⣴⣿⣦⡀⠙⠉⠻⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀\n            ⠀⠀⠀⢀⣴⣿⣿⣿⣿⣇⠀⠀⠀⢽⣿⣿⣿⣿⣦⡀⠀⠀⠀\n            ⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⡇⠀⣦⡀⠙⢿⢿⣿⣿⣿⣦⡀⠀\n            ⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⡆⠀⠀⠈⢻⣿⣿⣿⣆\n            ⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣷⣄⣀⣠⣿⣿⣿⠟⠁\n            ⠀⠀⠙⢿⣿⣿⣿⣿⣿⡿⠃⠀⠻⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀\n            ⠀⠀⠀⠀⠙⢿⣿⣿⣿⣇⠀⠀⠀⣽⣿⣿⣿⠟⠁⠀⠀⠀⠀\n            ⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣷⣶⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀\n            ⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀\n            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n\n            ♦ GIT CONFIG™ version 1.0 ♦\n\x1b[m'
def P():
	while True:
		F();A(E);A(O);A(E);A('\n1. Configurar nome de usuário global');A('2. Configurar endereço de e-mail global');A('3. Configurar editor padrão');A('4. Configurar branch principal');A('5. Configurar nome de usuário local (por repositório)');A('6. Configurar endereço de e-mail local (por repositório)');A('9. Listar as configurações do git');A('x. Sair');C=B('\nDigite o número da opção desejada: ')
		if C=='1':G()
		elif C=='2':H()
		elif C=='3':I()
		elif C=='4':J()
		elif C=='5':K()
		elif C=='6':L()
		elif C=='9':N()
		elif C=='--info':M()
		elif C=='x':A('\nSaindo do GIT Config...\n');break
		else:A('\nOpção inválida. Por favor, escolha uma opção válida.')
if __name__=='__main__':P()

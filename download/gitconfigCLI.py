H='\nOpção inválida. Por favor, escolha uma opção válida.'
D='\nPressione ENTER para voltar ao Menu.'
B=input
A=print
import os as C
def I():E=B('\nDigite seu nome de usuário do Git: ');C.system(f'git config --global user.name "{E}"');A('\nNome de usuário global configurado com sucesso!');B(D)
def J():E=B('\nDigite seu endereço de e-mail do Git: ');C.system(f'git config --global user.email "{E}"');A('\nEndereço de e-mail global configurado com sucesso!');B(D)
def K():E=B('\nDigite seu editor de texto preferido para usar com o Git: ');C.system(f'git config --global core.editor "{E}"');A('\nEditor padrão configurado com sucesso!');B(D)
def L():E=B('\nDigite o nome da branch principal: ');C.system(f"git config --global init.defaultBranch {E}");A('\nBranch principal configurada com sucesso!');B(D)
def M():E=B('\nDigite seu nome de usuário do Git para este repositório: ');C.system(f'git config user.name "{E}"');A('\nNome de usuário local configurado com sucesso!');B(D)
def N():E=B('\nDigite seu endereço de e-mail do Git para este repositório: ');C.system(f'git config user.email "{E}"');A('\nEndereço de e-mail local configurado com sucesso!');B(D)
def O():E();A(F);A('♦ GIT CONFIG™ ♦');A(F);A('Github: https://github.com/Eduardoiago');A('Developed by Eduardo Iago | Versão: 1.0.0\n');A('O gitConfig é uma ferramenta desenvolvida em python para configurar o git em uma nova máquina.');B(D)
def P():
	F='Para visualizar seus IDs vá até (.ssh) em home.';E='\nDigite seu email do Github: ';A('\nSSH CONFIG');A('Se você estiver usando um sistema legado que não suporta o algoritmo Ed25519, use RSA 4093.\n');A('1. Gerar chave SSH usando \x1b[3mEd25519\x1b[m');A('2. Gerar chave SSH usando \x1b[3mRSA 4093\x1b[m');A('3. Voltar ao Menu');D=B('\nInsira a opção: ')
	if D=='1':I=B(E);C.system(f'ssh-keygen -t ed25519 -C "{I}"');A('\nChave SSH-Ed25519 gerada com sucesso!');A(F)
	elif D=='2':J=B(E);C.system(f'ssh-keygen -t rsa -b 4096 -C "{J}"');C.system('eval "$(ssh-agent -s)"');C.system('ssh-add ~/.ssh/id_rsa');A('\nChave SSH RSA 4096 gerada com sucesso!');A(F)
	elif D=='3':G()
	else:A(H)
def Q():D=B('Digite o nome do alias: ');E=B('\nDigite o comando Git para associar ao alias: ');C.system(f'git config --global alias.{D} "{E}"');A(f"Alias '{D}' configurado com sucesso!")
def R():C.system('git config --list')
def E():C.system('clear'if C.name=='posix'else'cls')
F=27*'⣿⣿'
S='\x1b[3m\n\n            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n            ⠀⠀⠀⠀⠀⠀⠀⠀⠐⢿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀\n            ⠀⠀⠀⠀⠀⢀⣴⣿⣦⡀⠙⠉⠻⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀\n            ⠀⠀⠀⢀⣴⣿⣿⣿⣿⣇⠀⠀⠀⢽⣿⣿⣿⣿⣦⡀⠀⠀⠀\n            ⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⡇⠀⣦⡀⠙⢿⢿⣿⣿⣿⣦⡀⠀\n            ⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⡆⠀⠀⠈⢻⣿⣿⣿⣆\n            ⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣷⣄⣀⣠⣿⣿⣿⠟⠁\n            ⠀⠀⠙⢿⣿⣿⣿⣿⣿⡿⠃⠀⠻⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀\n            ⠀⠀⠀⠀⠙⢿⣿⣿⣿⣇⠀⠀⠀⣽⣿⣿⣿⠟⠁⠀⠀⠀⠀\n            ⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣷⣶⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀\n            ⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀\n            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n\n            ♦ GIT CONFIG™ version 1.0 ♦\n\x1b[m'
def G():
	while True:
		E();A(S);A('\n1. Configurar nome de usuário global');A('2. Configurar endereço de e-mail global');A('3. Configurar editor padrão');A('4. Configurar branch principal');A('5. Configurar nome de usuário local (por repositório)');A('6. Configurar endereço de e-mail local (por repositório)');A('7. Gerar chave SSH (Ed25519 ou rsa 4096)');A('8. Configurar alias');A('9. Listar as configurações do git');A('x. Sair');C=B('\nDigite o número da opção desejada: ')
		if C=='1':I()
		elif C=='2':J()
		elif C=='3':K()
		elif C=='4':L()
		elif C=='5':M()
		elif C=='6':N()
		elif C=='7':P()
		elif C=='8':Q()
		elif C=='9':R()
		elif C=='--info':O()
		elif C=='x':A('\nSaindo do GIT Config...\n');break
		else:A(H)
if __name__=='__main__':G()

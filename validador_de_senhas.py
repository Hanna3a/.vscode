# Sistema de Login e Cadastro
# Objetivo:
# - Permitir que o usuário se cadastre com login e senha
# - Armazenar os dados em um dicionário
# - Permitir que o usuário faça login
# - Exibir um menu simples de opções
# - proximas melorias: fazer um sistema que libere uma musica apenas para usuarios logados.
# Author: Ana Carolina
#feito em janeiro de 2026.

CORES = [
    "\033[35m",  # lilás (magenta)
    "\033[34m",  # azul
]

RESET = "\033[0m"

usuarios = {
    "Hanna" : "Choc@123",
    "abacate" : "Cookie@123"
    
}

def login():
    """
    função para fazer o login do usuario com limites de tentativas.
    verifica se o nome e senha então no dicionario 'usuarios'.
    retorna True se o login for bem sucedido, e False caoso contrario.
    
    """
    print("\n--- Login ---")
    
    max_tentativas = 3
    tentativas = 0
    
    print(f"Voce tem {max_tentativas} tentativas para entrar no sistema.")
    
    while tentativas < max_tentativas:
        entrada_deusuario = input("Digite seu nome de usuario: ")
        entrada_senha = input("Dgite sua senha: ")
        if entrada_deusuario in usuarios and entrada_senha == usuarios[entrada_deusuario]:
            print("Bem-vindo(a)! ao sistema.")
            return True
        else:
            tentativas += 1
            print(
                f"❌ Dados incorretos. "
                f"Tentativas restantes: {max_tentativas - tentativas}")
    return False

def cadastrar_usuario():
    """
    Cadastra um novo usuário no sistema.
    - Impede nomes repetidos
    - Exige senha mínima
    - Confirma a senha
    - Impede senha igual ao nome
    """
    print("\n--- Cadastro de Usuário ---")

    nome_usuario = input("Digite o nome de usuário desejado: ")

    if nome_usuario in usuarios:
        print("❌ Nome de usuário já existe. Tente outro.")
        return

    while True:
        senha = input("Digite a senha desejada: ")
        confirmar_senha = input("Confirme a senha: ")

        if senha != confirmar_senha:
            print("❌ As senhas não coincidem. Tente novamente.")
        elif len(senha) < 6:
            print("❌ A senha deve ter no mínimo 6 caracteres.")
        elif senha == nome_usuario:
            print("❌ A senha não pode ser igual ao nome de usuário.")
        else:
            usuarios[nome_usuario] = senha
            print("✅ Usuário cadastrado com sucesso!")
            return


def menu_usuario():
    while True:
        print("1- Desbloquear música 🎵")
        print("2- Mudar senha 🔐")
        print("3- Logout 🔁")
        
        opccao = input("Escolha uma opção:")
        if opcao == "1":
            musica_desbloqueada()
        elif opcao == "2":
            print("Senha alterada com sucesso!")
        elif opcao == "3":
            print("Fazendo logout....")
            break
        
 
def musica_desbloqueada():
    import time
    import sys
    print("Musica desbloqueada!")
    
    letra = [
    "I'm so blessed (I'm so blessed)",
    "Hallelujah, I'm blessed",
    "I'm so blessed (I'm so blessed)",
    "Hallelujah, I'm blessed",

    "Trouble knocking at my door today",
    "I ain't gonna let it in",
    "And worry wanna steal my joy away",
    "But I ain't gonna let it win",

    "'Cause on my best day, I'm a child of God",
    "On my worst day, I'm a child of God",
    "Oh, everyday is a good day",
    "And You're the reason why",

    "I'm so blessed, I'm so blessed",
    "Got this heartbeat in my chest",
    "No, it doesn't matter about the rest",
    "If I got You Lord, I'm so blessed",

    "I'm so blessed (I'm so blessed)",
    "Hallelujah, I'm blessed",
    "I'm so blessed (I'm so blessed) (okay)",
    "Hallelujah, I'm blessed",

    "And when I count the problems that I see",
    "Hope looks all, but gone (yeah)",
    "But when I count the ways You're good to me",
    "You got me counting all day long",
    "Oh, yeah",

    "I'm so blessed, I'm so blessed",
    "Got this heartbeat in my chest",
    "No, it doesn't matter about the rest",
    "If I got You Lord, I'm so blessed",

    "Hey, I'm so blessed, I'm so blessed",
    "Got this heartbeat in my chest",
    "No, it doesn't matter about the rest",
    "If I got You Lord, I'm so blessed",

    "'Cause on my best day, I'm a child of God",
    "On my worst day, I'm a child of God",
    "Oh, everyday is a good day",
    "And You're the reason why",

    "'Cause on my best day, I'm a child of God",
    "On my worst day, I'm a child of God",
    "Oh, everyday is a good day (everyday is a good day)",
    "And You're the reason why (reason why)",

    "I'm so blessed, I'm so blessed",
    "Got this heartbeat in my chest",
    "No, it doesn't matter about the rest",
    "If I got You Lord, I'm so blessed (sing it again)",

    "I'm so blessed, I'm so blessed",
    "And I got this heartbeat in my chest",
    "No, it doesn't matter about the rest",
    "If I got You Lord, I'm so blessed (hey)",

    "'Cause on my best day, I'm a child of God",
    "On my worst day, I'm a child of God",
    "Oh, everyday is a good day",
    "And You're the reason why (reason why)",

    "'Cause on my best day, I'm a child of God",
    "On my worst day, I'm a child of God",
    "Oh, everyday is a good day",
    "And You're the reason why",

    "I'm so blessed (I'm so blessed)",
    "Hallelujah, I'm blessed",
    "I'm so blessed (I'm so blessed)",
    "Hallelujah, I'm blessed",

    "No, it doesn't matter about the rest",
    "(Hallelujah, I'm blessed)",
    "If I got You Lord",
    "Hallelujah, I'm blessed",
        ]
    indice_cor = 0

    for frase in letra:
        for caractere in frase:
            cor_atual = CORES[indice_cor % len(CORES)]
            sys.stdout.write(cor_atual + caractere + RESET)
            sys.stdout.flush()
            time.sleep(0.05) # pequena pausa para efeito de digitação
            indice_cor += 1

        sys.stdout.write("\n")
        time.sleep(0.4) #pausa entre as frases

print("---SISTEMA---")
while True:
    print("1- Login.")
    print("2- Cadastrar novo usuario.")
    print("3- Sair.")
    
    opcao = input("Escolha uma opção:")
    if opcao == "1":
        if login():
            menu_usuario()
    elif opcao == "2":
        cadastrar_usuario()
    elif opcao == "3":
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")
              

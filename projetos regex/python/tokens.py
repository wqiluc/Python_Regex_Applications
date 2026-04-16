import secrets
import hashlib
from cores import *

while True:
    senha_usuario = str(input(f"\n{CinzaClaro}Digite a senha (letras, números e min. 8 caracteres): {Reset}")).strip()
    if (len(senha_usuario) >= 8 and 
        any(c.isdigit() for c in senha_usuario) and 
        any(c.isalpha() for c in senha_usuario)):
        break
    else:
        print(f"{Vermelho}Senha inválida! Tente novamente.{Reset}")

while True:
    opcao = input(f"""\n{CinzaClaro}Digite qual opção quer acessar:{Reset}
    1 - Ver a senha Criptografada
    2 - Alterar Senha
    3 - Sair
    > """)

    match opcao:
        case "1":
            salt = secrets.token_hex(16)
            token_final = hashlib.sha256((senha_usuario + salt).encode()).hexdigest()
            print(f"\n{Verde}Salt:{Reset} {salt}")
            print(f"{Verde}Hash:{Reset} {token_final}")
        
        case "2":
            while True:
                nova_senha = str(input(f"{CinzaClaro}Digite a nova senha: {Reset}")).strip()
                if (len(nova_senha) >= 8 and 
                    any(c.isdigit() for c in nova_senha) and 
                    any(c.isalpha() for c in nova_senha)):
                    senha_usuario = nova_senha
                    print(f"{Verde}Senha alterada com sucesso!{Reset}")
                    break
                else:
                    print(f"{Vermelho}Nova senha não atende aos requisitos!{Reset}")
            
        case "3":
            print(f"{Amarelo}Saindo. . .{Reset}")
            break
            
        case _:
            print(f"{Vermelho}Opção inválida! Digite: 1, 2 ou 3{Reset}")
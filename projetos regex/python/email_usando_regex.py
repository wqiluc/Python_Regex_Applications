(f"""
Crie um programa que dado o e-mail de um usuário, 
valide se aquele e-mail é válido com as seguintes regras:
    - Tem que ter .com ou .gov;
    - Tem que ter @;
    - Tem que ter mais de 5 caracteres; e
    - Não pode ter espaço. """)

#solução:👇
from cores import *
from re import fullmatch as padrao

email_usuario = str(input(f"{Negrito}Digite o email do usuário: {Reset}")).strip()
while not (padrao(r"^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.(com|gov)$",(f"{email_usuario[0:].lower()}"))):
    print(f"{Vermelho}Termo Inválido!! ❌ Digite um padrão VÁLIDO para o email. Siga as regras acima 👆{Reset}")
    email_usuario = str(input(f"{Negrito}Digite o email do usuário: {Reset}")).strip()

print(f"{Negrito}Email do usuário:{Reset} {AmareloClaro}{email_usuario.lower()}{Reset}")
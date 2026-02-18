print(f"""
╔══════════════════════════════════════════════════════╗
║              🪪 MASCARADOR DE CPF 🇧🇷 🎭               ║
╠══════════════════════════════════════════════════════╣

🎯 Objetivo:
Identificar e mascarar CPFs em um texto garantindo:

• Reconhecimento do formato 123.456.789-00;
• Validação estrutural do padrão brasileiro;
• Substituição segura dos 9 primeiros dígitos;
• Preservação dos 2 dígitos verificadores;
• Tratamento automatizado via Regex;
• Proteção de dados sensíveis;

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 Exemplo tratado pelo algoritmo:

Entrada:
CPF do cliente: 123.456.789-00

Saída:
CPF do cliente: ***.***.***-00

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 Conceitos aplicados:
Regex (re);
Grupos de captura ();
Referência a grupos (\\4);
Escape de caracteres especiais (\\.);
Quantificadores {3} e {2};
Substituição com re.sub(); e
Mascaramento parcial de padrões sensíveis.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 Sistema preparado para anonimização estrutural de CPFs """)

#resolução👇🎭:
from cores import *
import re as padrao
cpf = str(input(f"\n {CinzaClaro}Digite o seu CPF: (ex: XXX.XXX.XXX-XX){Reset}")).strip()
padrao_cpf = (r"(\d{3})\.(\d{3})\.(\d{3})-(\d{2})")
while not (padrao.fullmatch(padrao_cpf,cpf)):
    print(f"{Vermelho}Termo Inválido!! ❌ Digite um CPF (ex: XXX.XXX.XXX-XX){Reset}")
    cpf = str(input(f"\n {CinzaClaro}Digite o seu CPF: (ex: XXX.XXX.XXX-XX){Reset}")).strip()
    padrao_cpf = (r"(^\d{3})\.(\d{3}\.{3})-(\d{2}$)")

resultado = padrao.sub(padrao_cpf,(r"***.***.***-\4"),cpf)

print(f"\n {CinzaClaro}O cpf Mascarado é:{Reset} {Amarelo}{resultado[0:12]}{Reset}{CinzaClaro}{resultado[12:]}{Reset}")
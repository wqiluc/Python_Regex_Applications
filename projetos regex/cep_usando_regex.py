print(f"""
╔══════════════════════════════════════════════════════╗
║              📮 ANALISADOR DE CEP BRASILEIRO 🇧🇷       ║
╠══════════════════════════════════════════════════════╣

🎯 Objetivo:
Validar CEPs brasileiros garantindo:

• Estrutura obrigatória de 8 dígitos;
• Aceitação no formato 12345-678;
• Validação de hífen na posição correta;
• Bloqueio de caracteres inválidos;
• Garantia de início e fim exatos da string;
• Possibilidade de normalização automática;

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 Exemplos válidos tratados pelo algoritmo:

✅ 01001-000;
✅ 30140-110;
✅ 69900-000; e
✅ 12345-678.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 Conceitos aplicados:
Regex (re);
Âncoras (^ e $);
Metacaractere \\d;
Quantificadores {5} e {3};
Escape de caracteres especiais (\\-); e
Validação com re.fullmatch().

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 Sistema preparado para validação estrutural precisa de CEPs
""")

#resolução👇:

from cores import *
import re as padrao

cep = str(input(f"\n {CinzaClaro}Digite o seu CEP: (ex: XXXXX-XXX) {Reset}"))
padrao_cep = (r"^\d{5}-\d{3}$")
while not (padrao.fullmatch(padrao_cep,cep)):
    print(f"{Vermelho}Termo Inválido!! Digite o CEP novamente{Reset}")
    cep = str(input(f"{CinzaClaro}Digite o seu CEP: (ex: XXXXX-XXX){Reset}"))
    padrao_cep = (r"^\d{5}-\d{3}$")

print(f"{CinzaClaro}O Cep é:{Reset} {Amarelo}{cep[0:]}{Reset}")
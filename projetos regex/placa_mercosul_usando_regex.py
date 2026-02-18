print(f"""
╔══════════════════════════════════════════════════════╗
║           🚗 ANALISADOR DE PLACA MERCOSUL 🇧🇷          ║
╠══════════════════════════════════════════════════════╣

🎯 Objetivo:
Validar placas no padrão Mercosul garantindo:

• Estrutura obrigatória de 7 caracteres;
• Três letras iniciais;
• Um número na 4ª posição;
• Uma letra na 5ª posição;
• Dois números finais;
• Bloqueio de caracteres especiais;
• Garantia de início e fim exatos da string;

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 Exemplos válidos tratados pelo algoritmo:

✅ ABC1D23;
✅ BRA2E19;
✅ XYZ9K88; e
✅ QWE4T56.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 Conceitos aplicados:
Regex (re);
Classe de caracteres [A-Z];
Metacaractere \\d;👇
Quantificadores {3} e {2};
Âncoras (^ e $);
Conversão para maiúsculo (.upper()); e
Validação com re.fullmatch().

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 Sistema preparado para validação estrutural do padrão Mercosul
""")

#resolução👇:
from cores import *
import re as padrao

placa_mercosul = str(input(f"\n {CinzaClaro}Digite a placa Merco_Sul aqui: {Reset}"))
padrao_placa_mercosul = (r"^[A-Z]{3}\d[A-Z]\d{2}$")

while not (padrao.fullmatch(padrao_placa_mercosul,placa_mercosul)):
    print(f"{Vermelho}Termo Inválido!! ❌ Siga o padrão das placas MercoSul{Reset}")
    placa_mercosul = str(input(f"{CinzaClaro}Digite a placa Merco_Sul aqui: {Reset}"))
    padrao_placa_mercosul = (r"^[A-Z]{3}\d[A-Z]\d{2}$")

print(f"\n {CinzaClaro}Placa MercoSul:{Reset} {Cyan}{placa_mercosul}{Reset}")
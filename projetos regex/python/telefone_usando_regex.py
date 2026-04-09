print(f"""
╔══════════════════════════════════════════════════════╗
║        🔎 ANALISADOR DE TELEFONE BRASILEIRO🇧🇷         ║
╠══════════════════════════════════════════════════════╣

🎯 Objetivo:
Validar números de telefone brasileiros garantindo:

• Obrigatoriedade do código do país +55 🇧🇷;
• Aceitação de DDD com ou sem parênteses;
• Tratamento de espaços em branco;
• Tratamento de hífens;
• Suporte a números com 8 ou 9 dígitos;
• Validação estrutural real do padrão brasileiro;

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 Exemplos válidos tratados pelo algoritmo:

✅ +55 21 9799999999;
✅ +55 21 79999999;
✅ +55 (21)79999-9999; e
✅ +5521799999999.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 Conceitos aplicados:
Regex (re);
Grupos de captura;
Quantificadores;
Âncoras (^ e $);
Tratamento de padrões opcionais (?); e
Normalização de entrada do usuário.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 Sistema preparado para validação robusta de padrões """)

#resolução👇:
from cores import *
from re import fullmatch as padrao

numero_telefone = str(input(f"{Negrito}Digite seu número de telefone. ex: (+55DDD9XXXXXXXX){Reset}")).strip()
while not (padrao(r"^\+55\s?(\(?\d{2}\)?)\s?\d{4,5}-?\d{4}$", numero_telefone)):
    print(f"{Vermelho}Termo Inválido! ❌ Digite de acordo com o padrão de um telefone.{Reset}")
    numero_telefone = str(input(f"{Negrito}Digite seu número de telefone. ex: (+55DDD9XXXXXXXX){Reset}")).strip()

print(f"{Negrito}Número de telefone: {numero_telefone}{Reset}")
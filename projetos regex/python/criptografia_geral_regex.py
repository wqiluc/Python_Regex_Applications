from cores import *
from re import fullmatch as padrao

def criptografia_geral_regex():
    print(f"\n{CinzaClaro} --- Criptografia Geral usando Regex --- {Reset}")
    
    texto_comum = str(input(f"{CinzaClaro}Digite o texto comum: {Reset}")).strip()
    while not (padrao(r'[A-Za-z]+', texto_comum)):
        print(f"{Vermelho}Texto inválido. Digite apenas letras.{Reset}")
        texto_comum = str(input(f"{CinzaClaro}Digite o texto comum: {Reset}")).strip()
    
    mapa_estranho = {
        'a': 'æ', 'A': 'Å', 'e': '€', 'E': 'Σ', 'i': 'ɨ', 'I': '‡',
        'o': 'ø', 'O': 'Ω', 'u': 'µ', 'U': 'Ц', 's': '§', 'S': '∫',
        't': '†', 'T': 'Ŧ', 'l': '£', 'L': 'Ł', 'b': 'ß', 'B': '฿',
        'n': 'ñ', 'r': '®', 'c': '©', 'x': '×', 'y': '¥'
    }
    
    lista_caracteres = list(texto_comum)
    
    for indicecaracter, caracter in (enumerate(lista_caracteres)):
        if (caracter in mapa_estranho):
            lista_caracteres[indicecaracter] = mapa_estranho[caracter]
        else:
            lista_caracteres[indicecaracter] = "¤" 

    texto_criptografado = "".join(lista_caracteres)
    print(f"{Verde}Criptografado: {texto_criptografado}{Reset}")
    
    return (texto_criptografado)

def main():
    criptografia_geral_regex()

if (__name__ == "__main__"):
    main()
palavras = ["BELEZA", "CARRO", "PYTHON", "CODIGO" , "LEGAL", "DOIDEIRA"]
import random 
import string
def escolha_palavra(palavras):
    palavra = random.choice(palavras)
    return palavra
def forca():
    palavra = escolha_palavra(palavras)
    letrasPalavra = set(palavra)
    alfabeto = set(string.ascii_uppercase)
    letrasEsc = set()
    vidas = 6
    while len(letrasPalavra) > 0 and vidas > 0:
        print ('Você tem ',vidas, 'restantes e usou as seguintes letras' ,''.join(letrasEsc))
        listaPalavras = [letra if letra in letrasEsc else '-' for letra in palavra]
        print('Palavra atual: ',''.join(listaPalavras))
        letraUsu = input("Tente uma letra ").upper()
        if letraUsu in alfabeto - letrasEsc:
            letrasEsc.add(letraUsu)
            if letraUsu in letrasPalavra:
                letrasPalavra.remove(letraUsu)
            else: 
                vidas = vidas -1
                print("A letra que você escolheu não tem na palavra")
        elif letraUsu in letrasEsc:
            print("Essa letra já foi usada, tente outra")
        else:
            print("Caractér inválido")
    if vidas == 0:
        print('Você morreu, a palavra era', palavra)
    else:
        print('Você acertou a palavra' ,palavra, '!!')
forca()
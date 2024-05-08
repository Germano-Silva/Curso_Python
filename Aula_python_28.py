"""
Exercício:
Peça ao usuário para digitar seu nome.
Peça ao usuário para digitar sua idade
se nome e idade forem digitador:
        Exiba:
            Seu nome é {nome}
            Seu nome invertido é {nome invertido}
            Seu nome contem (ou não) espaços
            Seu nome tem(n) letras
            A primeira letra do seu nome é{letra}
            Aultima letra do seu nome é {letra}
    Se nada for digitado em nome ou idade:
        Exiba "Desculpe, você deixou campos vazioa."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome[::-1]}.')
    if ' ' in nome:
        print('Seu nome contem espaços.')
    else:
        print('Su nome não contem espaços.')
    print('Seu nome tem {len(nome)} letras')
    print('A primeira letra do seu nome é {nome[0]}')
    print('A ultima letra do seu nome é {nome[(len(nome)-1)]}')
    

else:
    print('Desculpe, você deixou campos vazioa.')
from random import randint

def menu(): # Cria uma interface de escolha no script, que retorna uma opção de 1 a 3
    select = None
    while select not in ['1', '2', '3']:
        select = input('''
1 - GERAR CPF
2 - VER LISTA DE CPF GERADOR
3 - SAIR
SELECIONE UMA OPÇÃO: ''')
        
        if select not in ['1', '2', '3']:
            print('\033[31mERRO: Digite uma opção válida!\033[0m')
        
    return select


def armazenar_cpf(cpf): # Armazena o CPF gerado em um arquivo txt
    arquivo = open(r'.\lista_cpf.txt', 'a')
    arquivo.write(cpf + '/')
    arquivo.close()


def lista_cpf(): # Mostra para o usuário a lista de CPFs gerados
    try:
        arquivo = open(r'.\lista_cpf.txt', 'r')
    except:
        arquivo = open(r'.\lista_cpf.txt', 'a')
        arquivo = open(r'.\lista_cpf.txt', 'r')

    conteudo = arquivo.read()
    arquivo.close()

    if '/' in conteudo:
        conteudo = conteudo.split('/')
    
    print()
    print('-' * 10, 'LISTA DE CPFs GERADO', '-' * 10)
    print('NUM   CPF')
    for i, j in enumerate(conteudo):
        if i < (len(conteudo) - 1):
            print(f'{i+1}     {j}')
    print('-' * 42)
        


def cpf(): # Gera os 9 primeiros digítos do CPF usando números pseudoaleatórios
    cpf = [randint(0,9),randint(0,9),randint(0,9),
           randint(0,9),randint(0,9),randint(0,9),
           randint(0,9),randint(0,9),randint(0,9)]
    
    return cpf


def gerar(cpf): # Cria um CPF de 11 digitos de acordo com o algoritmo do CPF
    resultado_digito1 = 0
    resultado_digito2 = 0

    for i, j in enumerate(cpf, -10):
        i = i * -1
        resultado_digito1 += i * j

    digito1 = (resultado_digito1 * 10) % 11
    digito1 = digito1 if digito1 <= 9 else 0
    cpf.append(digito1)

    for i, j in enumerate(cpf, -11):
        i = i * -1
        resultado_digito2 += i * j

    digito2 = (resultado_digito2 * 10) % 11
    digito2 = digito2 if digito2 <= 9 else 0
    cpf.append(digito2)

    cpf.insert(3, '.')
    cpf.insert(7, '.')
    cpf.insert(11, '-')
    cpf = ''.join(map(str, cpf))

    return cpf


def menuInicial(): # Menu ASCII pra deixar bonitinho o ínicio
    menu_ascii = r'''
  /$$$$$$   /$$                                                           /$$                       /$$$$$$ 
 /$$__  $$ | $$                                                          | $$                      /$$__  $$
| $$  \__//$$$$$$    /$$$$$$  /$$    /$$ /$$$$$$  /$$$$$$$           /$$$$$$$  /$$$$$$  /$$    /$$| $$  \ $$
|  $$$$$$|_  $$_/   /$$__  $$|  $$  /$$//$$__  $$| $$__  $$ /$$$$$$ /$$__  $$ /$$__  $$|  $$  /$$/|  $$$$$$/
 \____  $$ | $$    | $$$$$$$$ \  $$/$$/| $$$$$$$$| $$  \ $$|______/| $$  | $$| $$$$$$$$ \  $$/$$/  >$$__  $$
 /$$  \ $$ | $$ /$$| $$_____/  \  $$$/ | $$_____/| $$  | $$        | $$  | $$| $$_____/  \  $$$/  | $$  \ $$
|  $$$$$$/ |  $$$$/|  $$$$$$$   \  $/  |  $$$$$$$| $$  | $$        |  $$$$$$$|  $$$$$$$   \  $/   |  $$$$$$/
 \______/   \___/   \_______/    \_/    \_______/|__/  |__/         \_______/ \_______/    \_/     \______/                            
    '''
    return print(f'{menu_ascii}\n'
                 f'{'-' * 60}\n'
                 f'{'MENU GERADOR DE CPF'.center(60)}\n'
                 f'{'-' * 60}\n')

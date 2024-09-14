import generator
from time import sleep

generator.menuInicial()

while True:
    select = generator.menu()
    
    if select == '1':
        digito = generator.cpf()
        cpf = generator.gerar(digito)
        generator.armazenar_cpf(cpf)
    
        print(f'CPF GERADO: {cpf}')

    elif select == '2':
        generator.lista_cpf()

    else:
        print('FIM')
        break
    
    sleep(0.6)
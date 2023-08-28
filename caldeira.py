import math
import random

def calculos(temperatura, pressao, Volume_Agua0, tempo_max, t):
    # loop do tempo
    tempo_max = int(tempo_max)
    tempo_loop = tempo_max + 1
    for loop in range(tempo_loop):
        # Cálculo do Volume de Água
        VolumeAgua=Volume_Agua0*(1-(t/tempo_max)/(1+0.01*math.cos(t)))-1*random.uniform(1, 10)

        # Cálculo da Pressão
        pressao=pressao/VolumeAgua+ 1*(Volume_Agua0/(1+math.exp(-0.09*(t-tempo_max/2)))+ math.sin(2*t/tempo_max))-1*random.uniform(1, 10)

        # Cálculo da Temperatura
        temperatura=temperatura/pressao+20*t/tempo_max*10*math.cos(t/tempo_max)-1*random.uniform(1, 10)
        
        dados = [t, VolumeAgua, pressao, temperatura]
        print('='*130)
        print(f'Os valores são: Tempo = {dados[0]}; Volume de Água = {dados[1]}; Pressão = {dados[2]}; Temperatura = {dados[3]}')
        if dados[1] < 20:
            print(f'O volume de água não atingiu o valor mínimo a partir do minuto {dados[0]}.')
            print('='*130)
            break
        elif dados[2] > 80:
            print(f'O valor da pressão excedeu o limite a partir do minuto {dados[0]}.')
            print('='*130)
            break
        elif dados[3] > 90:
            print(f'O valor da temperatura excedeu o limite a partir do minuto {dados[0]}.')
            print('='*130)
            break
        print('='*130)
        t += 1
    return dados

continuar = 's'
while continuar != 'n':    
    # Mensagens ao usuário
    print('\nSoftware de Cálculo de Controle de Temperatura, Pressão e Volume de Água da Caldeia\n')
    print('Observações importantes para o usuário: A caldeia possui limitações de fábrica, sendo elas:')
    print('* O volume de água não pode ser menor que 20 Litros.\n* O valor da pressão não pode ser maior que 80.')
    print('* O valor da temperatura não pode ser maior que 90 graus celsius.\n')

    # Variáveis

    t = int (0) # Tempo
    temperatura = 0 # Temperatura
    pressao = 0 # Pressão

    while True:  # Variável Tempo Máximo e sua verificação
        tempo_max= (input('Digite o tempo máximo da simulação em minutos (Deve ser maior que zero):'))
        if tempo_max.isdigit() == False:
            print('Por favor, digite um valor numérico válido para o tempo máximo da simulação.')
        elif tempo_max.isdigit() == True:
            tempo_max = float(tempo_max)
            if tempo_max == 0 or tempo_max < 0:
                print('Por favor, digite um valor válido para o tempo máximo da simulação.')
            else:
                break

    while True:  # Variável Volume de Água Inicial
        try:
            Volume_Agua0 = float(input('Digite o volume inicial de água em litros (Entre 20 e 50 Litros):'))
            if Volume_Agua0 < 20 or Volume_Agua0 > 50: raise ValueError
        except ValueError:
            print('Por favor, digite um valor numérico válido para o volume inicial de água.')
        else:
            break
        
    calculos(temperatura, pressao, Volume_Agua0, tempo_max, t)
    
    continuar = input('Você deseja executar o programa novamente? (Pressione qualquer tecla para continuar ou "n" para sair.): ')
    continuar = continuar.lower()
    if continuar == 'n':
        print('Obrigado por utilizar o software!')

        #temperatura inicial = 0 pressão inicial = 0
        #Tempo máximo e volume inicial de água.
        #tempo começa em 0 e vai até o máximo, com um for

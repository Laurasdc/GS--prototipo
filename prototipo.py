# Listas para armazenar as medições
medicoes_ph = []
medicoes_temperatura = []
medicoes_turbidez = []

# Valores padrão do oceano para pH, temperatura e turbidez do oceano
padrao_ph = 8.2
padrao_temperatura = 21.0
padrao_turbidez = 3.0 

# Função para adicionar uma medição e compará-la com o padrão
def adicionar_medicao(tipo, valor):
    if tipo == 'ph':
        medicoes_ph.append(valor)
        if valor == padrao_ph:
            print(f"O pH medido ({valor}) é igual ao padrão do oceano ({padrao_ph})")
        elif valor != padrao_ph:
            print(f"O pH medido ({valor}) é diferente do padrão do oceano ({padrao_ph})")
    elif tipo == 'temperatura':
        medicoes_temperatura.append(valor)
        if valor == padrao_temperatura:
            print(f"A temperatura medida ({valor}) é igual ao padrão do oceano ({padrao_temperatura})")
        elif valor != padrao_temperatura:
            print(f"A temperatura medida ({valor}) é diferente do padrão do oceano ({padrao_temperatura})")
    elif tipo == 'turbidez':
        medicoes_turbidez.append(valor)
        if valor == padrao_turbidez:
            print(f"A turbidez medida ({valor}) é igual ao padrão do oceano ({padrao_turbidez})")
        elif valor != padrao_turbidez:
            print(f"A turbidez medida ({valor}) é diferente do padrão do oceano ({padrao_turbidez})")

# Função para obter as medições
def obter_medicoes(tipo):
    if tipo == 'ph':
        return medicoes_ph
    elif tipo == 'temperatura':
        return medicoes_temperatura
    elif tipo == 'turbidez':
        return medicoes_turbidez

# Função para forçar o usuário a escolher uma opção válida
def forcar(msg, opcoes):
    forcarescolha = input(msg)
    while forcarescolha not in opcoes:
        forcarescolha = input(msg)
    return forcarescolha

# Função para verificar se o valor inserido é um número
def eh_numero(valor):
    for char in valor:
        if not (char >= '0' and char <= '9' or char == '.'):
            return False
    return True

# Função para obter um valor de medição válido do usuário
def obter_valor():
    while True:
        valor = input("Digite o valor da medição: ")
        if eh_numero(valor):
            return float(valor)
        else:
            print("Valor inválido. Por favor, digite um número.")

# Loop principal do programa
while True:
    print("Escolha uma opção:")
    print("1. Adicionar medição")
    print("2. Visualizar medições")
    print("3. Sair")
    
    opcao = forcar("", ['1', '2', '3'])
    
    if opcao == '1':
        print("Digite o tipo de medição:")
        tipo = forcar("ph\n temperatura\n turbidez\n", ['ph', 'temperatura', 'turbidez'])
        valor = obter_valor()
        adicionar_medicao(tipo, valor)
    elif opcao == '2':
        print("Digite o tipo de medição que deseja visualizar:")
        tipo = forcar("ph\n temperatura\n turbidez\n", ['ph', 'temperatura', 'turbidez'])
        print(obter_medicoes(tipo))
    elif opcao == '3':
        break

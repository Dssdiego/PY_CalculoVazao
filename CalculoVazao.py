#--------------------------------------------------
#   Trabalho de Automação Industrial
#   Software Desenvolvido para Calculo da Vazão
#   Grupo:
#       Arthur Almeida,
#       Guilherme Guedes,
#       Larissa Rodrigues,
#       Lucas Lemos,
#       Marcelo Andrade,
#       Stevan Chaves
#--------------------------------------------------

#--------------------------------------------------
#   Descrição de Uso de Variáveis
#
#   "v_" -> Variáveis
#   "p_" -> Parâmetros de Funções
#
#--------------------------------------------------

# Importando a biblioteca 'matplotlib' para a plotagem dos gráficos
import matplotlib.pyplot as plt
# Importando a biblioteca 'pandas' (Python Data Analysis Library) para leitura do arquivo ".csv"
import pandas as pd
# Importando a biblioteca 'numpy' para executar contas matemáticas (como Raiz Quadrada,  etc)
import numpy as np
# Importando a biblioteca 'sys' para ler o arquivo passado na linha de comando
import sys

# Realizando a leitura do arquivo ".csv" na posição 1 (parâmetro passado na linha de comando)
csv = pd.read_csv(sys.argv[1], sep=';')

# "Jogando" os valores do csv em um Array para os valores de Tempo
v_Tempo = csv['Tempo'].values
# "Jogando" os valores do csv em um Array para os valores de Pressão
v_Pressao = csv['Pressao'].values
# "Jogando" os valores do csv em um Array para os valores de Temperatura
v_Temperatura = csv['Temperatura'].values


# Definição de Funções - Primeiro Sensor

# Cálculo da Pressão em Função da Tensão
# 6,227222708329802 x V
def calculaPressao (p_Tensao):
    return 6.227222708329802 * p_Tensao
    
# Cálculo da Velocidade de Escoamento
# V = \sqrt{2P / p2}
def calculaVesc (p_Pressao, p_Densidade):
    return np.sqrt((2 * p_Pressao) / p_Densidade)

# Q = 0,28274333882308139146163790449516 x V
def calculaVazaoVEsc (p_Vesc):
    return 0.07068583470577034786540947612379 * p_Vesc

    
# Definição de Funções - Segundo Sensor

# T(R) = 2,62 x R + 266,687
def calculaTemperatura (p_Resistencia):
    return 2.62 * p_Resistencia + 266.687
    
# D = (1,2754 x 293,15) / (t1) 
def calculaDensidade (p_Temp):
    return ((1.2754 * 293.15) / p_Temp)
    
    
# Definição de Funções - Resultados

# Função que calcula a Vazão Mássica
def calculaVazaoMassica (p_Vazao,p_Densidade):
    return p_Vazao * p_Densidade
   
    
# Realização das Contas 

P = calculaPressao(v_Pressao)
t1 = calculaTemperatura(v_Temperatura)
p2 = calculaDensidade(t1)
Vesc = calculaVesc(P,p2)
Q = calculaVazaoVEsc(Vesc)
VM = calculaVazaoMassica(Q,p2)
VMA = [] #Vazão Mássica para a Atmosfera

for i in range(len(VM)):
  if i == VM[0]:
    VMA.append(VM[0])
  else:
    VMA.append(VM[i] + VM[i-1])
   
print('Saída de Dados:\n')    

print('P:')
print(P)

print('t1:')
print(t1)

print('p2')
print(p2)

print('Vesc:')
print(Vesc)

print('Q')
print(Q)

print('VM:')
print (VM)

print('VMA:')
print(VMA)

# Gráfico 1 - Vazão Mássica vs Tempo

plt.figure('Vazão Mássica vs Tempo')
plt.grid(True)
plt.plot(v_Tempo,VM, 'k')
plt.xlabel('Tempo (s)')
plt.ylabel('Vazão Mássica (kg/s)', multialignment='center')

# Gráfico 2 - Vazão Total para Atmosfera vs Tempo

plt.figure('Vazão Total para Atmosfera vs Tempo')
plt.grid(True)
plt.plot(v_Tempo,VMA, 'k')
plt.xlabel('Tempo (s)')
plt.ylabel('Vazão Total para a Atmosfera (kg)', multialignment='center')

# Gráfico 3 - Vazão Mássica/Temperatura vs Tempo

fig, vm = plt.subplots()
plt.grid(True)

vm.plot(v_Tempo,VM, 'k')
vm.set_xlabel('Tempo (s)')
vm.set_ylabel('Vazão Mássica (kg/s)', multialignment='center')

temp = vm.twinx()
temp.plot(v_Tempo, v_Temperatura, 'r')
temp.set_ylabel('Temperatura (ºC)', color='r')

fig.tight_layout()

# Mostra os gráficos
plt.show()


#--------------------------------------------------
#   Trabalho de Automação Industrial
#   Software Desenvolvido para Calculo da Vazão
#   Autores:
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
#   "r_" -> Resultados
#
#--------------------------------------------------

# Importando a biblioteca 'matplotlib' para a plotagem dos gráficos
import matplotlib as matplotlib
import matplotlib.pyplot as plt
# Importando a biblioteca 'pandas' (Python Data Analysis Library) para leitura do arquivo ".csv"
import pandas as pd
# Importando a biblioteca 'math' para executar contas matemáticas (como Raiz Quadrada,  etc)
import math

# Realizando a leitura do arquivo ".csv"
csv = pd.read_csv('Arquivo.csv', sep=';')

# "Jogando" os valores do csv em um Array para os valores de Tempo
v_Tempo = csv['Tempo'].values
# "Jogando" os valores do csv em um Array para os valores de Pressão
v_Pressao = csv['Pressao'].values
# "Jogando" os valores do csv em um Array para os valores de Temperatura
v_Temperatura = csv['Temperatura'].values


# Definição de Funções - Primeiro Sensor

# f(P) = 0,0125 x P
def funcaoDePressao (p_Pressao):
    return 0.0125 * p_Pressao
    
# Função que calcula a Velocidade de Escoamento
# V = \sqrt{0.5 x P}
def calcVelocEscoamento (p_FuncPressao):
    return math.sqrt(0.5) * p_FuncPressao

# Q = 0,28274333882308139146163790449516 x V
def calcValorQ (p_Velocidade):
    return 0.28274333882308139146163790449516 * p_Velocidade

    
# Definição de Funções - Segundo Sensor

# f(T) = 2,62 x T + 266,687
def funcaoDeTemperatura (p_Temp):
    return 2.62 * p_Temp + 266.687
    
# D = (1,2754 x 293,15) / (t1) 
def calcValorD (p_FuncTemp):
    return ((1.2754 * 293.15) / p_FuncTemp)
    
    
# Definição de Funções - Resultados

# Função que calcula a Vazão Mássica
# @param Q [Valores do Primeiro Sensor]
# @param D [Valores do Segundo Sensor]
def calculaVazaoMassica (Q,D):
    return Q*D
   
    
# Realização das Contas 
    
v_FuncaoP = funcaoDePressao(v_Pressao)
v_VelEscoamento = calcVelocEscoamento(v_FuncaoP)
v_Q = calcValorQ(v_VelEscoamento)

v_FuncaoT = funcaoDeTemperatura(v_Temperatura)
v_D = calcValorD(v_FuncaoT)

v_VM = calculaVazaoMassica(v_Q, v_D)

#print('Velocidade de Escoamento:')
#print(calcVelocEscoamento(v_Pressao))

print('Q')
print(v_Q)

print('D')
print(v_D)

print('VM:')
print (v_VM)

plt.plot(v_Tempo,v_VM)
plt.xlabel('Tempo (s)')
plt.ylabel('Vazão Mássica (kg/s)', multialignment='center')

plt.show()


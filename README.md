# Cálculo de Vazão

## Descrição

O programa deve gerar gráficos de uma quantidade de massa lida por sensores ao longo do tempo.

Pra isso são utilizados 2 sensores, um de pressão e o outro de temperatura...

Funciona assim, o programa deve buscar os dados no CSV e jogar eles em funções...

Os dados de pressão do CSV devem ser jogados nessa função:

```
f(P) = 0,0125 x P
```

Os valores encontrados nesse cálculo devem ser jogados nessa outra fórmula:

```
V = \sqrt{0.5 x P}
```

O **“V”** achado, deverá ser jogado nessa outra fórmula:

```
Q = 0,28274333882308139146163790449516 x V
```

Com o primeiro sensor, esses foram os cálculos... 

Já o segundo deve receber os dados de temperatura do CSV e jogar na fórmula:

```
f(T) = 2,62 x T + 266,687
```
A temperatura encontrada aqui deve ser considerada como “t1” na próxima fórmula que é:

```
D = (1,2754 x 293,15) / (t1) 
```

Daí, terminado os cálculos com os sensores, deve se multiplicar valor de “Q” (do primeiro sensor) x “D” do segundo (sensor) que dará o valor de vazão mássica (VM):

```
VM: Q x D
```

O programa deve gerar um gráfico com todos os pontos que estão no CSV... Além disso o programa deve mostrar quanto de massa foi contada ao todo somando as massas de cada segundo... ou seja, somar as massas do segundos 1, 2, 3 ...                        


1. Método de Monte Carlo

Implementación del algoritmo de Metrópolis para una red cuadrada de
spines, con el Hamiltoniano dado en la teórica. Se obtendrá una
colección representativa de distintos estados del *ensemble* canónico.
Considerar una red cuadrada de $20\times20$ espines.

Condiciones de contorno periódicas: Estas condiciones se utilizan para
suprimir los efectos de borde. Se busca estudiar la magnetización como
si estuviera en el seno de un material magnético (*bulk*), sin
considerar los efectos particulares de las superficies o bordes del
sistema. Esta es una forma numérica usual de considerar un sistema
infinito.

Tome como configuración inicial del sistema una asignación aleatoria de
1 o -1 para cada espin. Luego de verificar que el programa funcione
calcule los valores medios de las magnitudes físicas de interés. Tome
para los cálculos kB=1

1\. Presentar gráficos de las siguientes cantidades como función de la
temperatura:

-   Magnetización media

-   Energía media

2\. Calcule el calor específico por partícula y la susceptibilidad a
campo nulo.

3\. Discutir brevemente los efectos de tamaño finito, debidos a que las
muestras usadas en la simulación tienen un número de espines pequeño en
comparación con el límite termodinámico.

4\. A partir de la curva de M vs. T estime la temperatura crítica Tc.
Explique qué observa con los valores medios de M a medida que se acerca
al punto crítico. Tome como referencia que la temperatura crítica del
cálculo exacto es Tc = 2,269.

**<u>Sugerencias:</u>**

Implementar primero el algoritmo de Monte Carlo y luego de confirmar que
está funcionando, agregue las cantidades a medir.

La configuración inicial, al ser aleatoria, pone al sistema en un punto
del espacio de fases, que seguramente no será de equilibrio respecto de
las condiciones físicas. Realice una primera corrida, de la cual no
promediará datos, para *termalizar* al sistema. Es decir, llegar al
equilibrio compatible con las condiciones físicas impuestas. Luego
realice otra simulación, desde donde termina la anterior, en la que sí
se medirán las magnitudes de interés.

La llegada al equilibrio puede verificarse observando que la energía,
por ejemplo, fluctúa respecto de un dado valor en lugar de tener derivas
al observar un gráfico de energía vs. paso de Monte Carlo.

Fíjese como no hace falta calcular la energía total de cada
configuración, si no sólo la diferencia de energía.

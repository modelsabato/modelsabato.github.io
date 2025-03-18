# Guía 1 

1.  Haga un programa que lea una serie de datos en un vector, que los ordene en forma ascendente y que tanto muestre el vector ordenado en pantalla como lo grabe en un archivo.

1.  La función exponencial se puede calcular como la serie:

    $$ e^x = 1+x+\frac{x^2}{2}+\frac{x^3}{3!}+\frac{x^4}{4!}+\;...\;+\frac{x^n}{n!} +\; ... $$

    evalúe la serie para calcular $e^{0.5}$, agregando sucesivos términos hasta asegurarse al menos 3 cifras significativas correctas. Comparar con el valor 1.64872127...

    Analice los resultados.

1.  
    - Un paracaidista de 70 kg salta desde un globo aerostático fijo. El coeficiente de resistencia del aire es de aproximadamente 12.5 $\frac{kg}{s}$ (tome la aceleración de la gravedad como 10 $\frac{m}{s^2}$). Utilizando la expresión exacta evalúe la velocidad del paracaidista cada 2 s después del salto y calcule su velocidad límite. Grafique el resultado.
    - Repita el gráfico con la solución discreta, tomando intervalos de 2 s, 1 s y 0.5 s.
    - Haga el mismo cálculo pero suponiendo ahora que la fuerza de rozamiento se debe expresar como $F = – c' v^2$ (tome c' = 0.25 $\frac{kg}{m}$).

1.  Encuentre la solución al sistemas $[A][x]=[b]$ correspondiente al siguiente sistema de ecuaciones
    
    $$
       \begin{eqnarray} x - 3y - 2z = 6 \\ 2x - 4y - 3z = 8 \\ -3x + 6y + 8z =  -5 \end{eqnarray}
    $$

1.  El agua de un lago de zonas templadas puede dividirse en estratos térmicos. Cerca de la superficie el agua es tibia y liviana (epilimnion) y en el fondo más fría y densa (hipolimnion). Lo mismo sucede en reactores químicos. Ambas capas están separadas, aproximadamente, por un plano conocido por thermocline, donde la derivada segunda de la temperatura respecto de la profundidad se hace cero (o la derivada primera tiene su máximo). A esta profundidad el flujo de calor de la superficie al fondo de la capa se puede calcular con la ley de Fourier, $J = -k\frac{dT}{dz}$. Dados los datos de la tabla siguiente, correspondientes a la temperatura del líquido de un reactor en función de la profundidad y usando el método de splines, realice un ajuste de la temperatura en función de la profundidad y de su derivada. Encuentre la posición aproximada de la thermocline y calcule el flujo de calor a través de la interfaz (tome $k = 0.01\;cal(s\;cm\;^\circ C)$)

    | $z\;[m]$              | 0 | 0.5 | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 |
    | :---------------- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
    | $T\;[^\circ C]$        | 70 | 68 | 55 | 22 | 13 | 11 | 10 |

1.  La fuerza efectiva que realiza el viento sobre el mástil de un bote de velas puede aproximarse por la siguiente expresión:
    
    $$
      F = \int_0^{30} 200 \left(\frac{z}{5+z}\right) e^{-\frac{2z}{30}} dz
    $$
    
    donde $F$ está dada en libras y las distancias en pies.

    Estime, utilizando los métodos de trapecios y de Simpson 1/3, cuánto vale la fuerza total y dónde será el punto de acción efectiva de esta fuerza.

    $$
      d = \frac{1}{F}\int_0^{30} z f(z) dz
    $$

    Utilice varios tamaños de paso de integración, entre 5 y 0.05 pies, y estudie la convergencia de cada método.

1.  Evalúe, utilizando los métodos de Euler, de Heun y de Runge Kutta de cuarto orden, la ecuación diferencial:

    $$
      \frac{dy}{dx} = 4 e^{0.8x} - 0.5 y
    $$

    con la condicióin de contorno $y(0) = 2$, desde $x = 0$ hasta $x = 4$, con varios tamaños de paso. Compare la exactitud de los diferentes métodos con el resultado exacto en $x = 4$, . Grafique este error en función del esfuerzo de cálculo realizado (cantidad de veces que tuvo que evaluar la función). Compare la soluciones numéricas obtenidas, $y(x)$, con la solución teórica:

    $$
      y(x) = \frac{4}{1.3}(e^{0.8x} - e^-{0.5x}) + 2 e^-{0.5x}
    $$

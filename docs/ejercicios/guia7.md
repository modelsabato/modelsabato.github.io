1. Potencial de Lennard-Jones
Considere un conjunto de \(N=20\) partículas puntuales confinadas dentro de una caja cuadrada bidimensional de lado \(L=10\).

Las partículas interactúan mediante el potencial de Lennard-Jones y evolucionan de acuerdo con las ecuaciones de Newton:

\[
m\frac{d^2\vec r}{dt^2}=\vec F
\]

Utilice los siguientes parámetros:

- Masa: \(m=1\)
- Parámetro de longitud: \(\sigma=1\)
- Parámetro energético: \(\varepsilon=1\)
- Paso temporal: \(\Delta t=0.002\)

La simulación deberá implementarse utilizando el algoritmo **Velocity-Verlet**.

La caja deberá poseer **condiciones de contorno periódicas**, es decir, cuando una partícula abandona la caja por uno de sus lados deberá reingresar por el lado opuesto.

---
## Parte A: Implementación

1. Implementar el potencial de Lennard-Jones:

\[
V(r)=4\varepsilon
\left[
\left(\frac{\sigma}{r}\right)^{12}
-
\left(\frac{\sigma}{r}\right)^6
\right]
\]

2. Implementar la fuerza correspondiente:

\[
\vec F(r)
=
24\varepsilon
\left[
2\left(\frac{\sigma}{r}\right)^{12}
-
\left(\frac{\sigma}{r}\right)^6
\right]
\frac{\vec r}{r^2}
\]

3. Generar posiciones iniciales aleatorias dentro de la caja.

4. Asignar velocidades iniciales aleatorias de pequeña magnitud.

5. Simular la evolución temporal del sistema durante al menos 10000 pasos temporales.

---

## Parte B: Visualización

Generar una animación que muestre:

- La posición de todas las partículas durante la simulación.
- Un identificador numérico asociado a cada partícula.
- Un color distinto para cada partícula.

A partir de la animación, describir:

1. Qué ocurre cuando dos partículas se encuentran muy próximas.
2. Qué ocurre cuando dos partículas se encuentran a distancias intermedias.
4. Si se observan agrupamientos o estructuras temporales.

---

## Parte C: Influencia de los parámetros del potencial

Repita la simulación modificando los parámetros \(\varepsilon\) y \(\sigma\).

### Variación de \(\varepsilon\)

Manteniendo \(\sigma=1\), realizar simulaciones con:

- \(\varepsilon=0.5\)
- \(\varepsilon=1.0\)
- \(\varepsilon=2.0\)

### Variación de \(\sigma\)

Manteniendo \(\varepsilon=1\), realizar simulaciones con:

- \(\sigma=0.8\)
- \(\sigma=1.0\)
- \(\sigma=1.2\)

---

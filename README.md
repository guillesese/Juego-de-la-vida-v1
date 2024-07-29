# Juego de la vida v1 en Python


## Descripción 
El juego de la vida es un autómata celular diseñado por el matemático británico John Horton Conway en 1970. Es un juego de cero jugadores, en el que su evolución es determinada por un estado inicial, sin requerir intervención adicional. Se considera un sistema Turing completo que puede simular cualquier otra Máquina de Turing. 

Se trata de un juego de cero jugadores, lo que quiere decir que su evolución está determinada por el estado inicial y no necesita ninguna entrada de datos posterior. El "tablero de juego" es una malla plana formada por cuadrados (las "células") que se extiende por el infinito en todas las direcciones. Por tanto, cada célula tiene 8 células "vecinas", que son las que están próximas a ella, incluidas las diagonales. Las células tienen dos estados: están "vivas" o "muertas" (o "encendidas" y "apagadas"). El estado de las células evoluciona a lo largo de unidades de tiempo discretas (se podría decir que por turnos). El estado de todas las células se tiene en cuenta para calcular el estado de las mismas al turno siguiente. Todas las células se actualizan simultáneamente en cada turno, siguiendo estas reglas:
- Nace: Si una célula muerta tiene exactamente 3 células vecinas vivas "nace" (es decir, al turno siguiente estará viva).
- Muere: una célula viva puede morir por uno de 2 casos:
  - Sobrepoblación: si tiene más de tres vecinos alrededor.
  - Aislamiento: si tiene solo un vecino alrededor o ninguno.
- Vive: una célula se mantiene viva si tiene 2 o 3 vecinos a su alrededor.

## Estados finales
Después de un determinado número de ciclos, se puede llegar a alguno de los siguientes estados finales:
- Extinción: Al cabo de un número finito de generaciones desaparecen todos los miembros de la población o células vivas.
- Estabilizacion: Al cabo de un número finito de generaciones la población queda estabilizada, ya sea de forma rígida o bien de forma oscilante entre dos o más formas.
- Crecimiento constante: La población crece turno tras turno y se mantiene así un número infinito de generaciones. En un principio esta evolución solo se contemplo de forma teórica, aunque más tarde se encontrarán patrones que crecían de forma indefinida, durante un número infinito de turnos. 

> PC

> Index

> Stack

> Acumulador A y B

> Sel-Dato

> Tri-Est

> Sel-Dir

> Dir-Val

> Alu

> Unidad de Control

# Ejecución

### Intrucciones

Para poder correr este programa basta con colocar la lista de instrucciones en el
objeto "instrucciones" del archivo _processor.py_ el cual es una lista de Strings.

### Correr el programa

Una vez colocadas las instrucciones, se guarda el archivo y se ejecuta con el comando
en terminal:
`$ python processor.py`

### Salida de programa

El programa dará una salida con los cambios de las variables de cada bloque, según sea la instrucción


# Test

Para este test se hizo una prueba con instrucciones desde *0000* hasta *1111*

```
Procesador de Maxines


Reset

<<Instrucción: 0000>>

cs <= bitarray('11111')
q <= 3
=============================
<<Instrucción: 0001>>

cs <= bitarray('10110')
rw <= bitarray('1')
q <= 4
=============================
<<Instrucción: 0010>>

datoin <= bitarray('0000')
datoin <= bitarray('0000')
rw <= bitarray('0')
cs <= bitarray('00001')
q <= 2
=============================
<<Instrucción: 0011>>

operacion <= bitarray('0000')
rc <= bitarray('0010')
cs <= bitarray('00001')
q <= 5
=============================
<<Instrucción: 0100>>

operacion <= bitarray('0000')
rc <= bitarray('0010')
cs <= bitarray('10101')
q <= 11
=============================
<<Instrucción: 0101>>

datoin <= bitarray('0000')
datoin <= bitarray('0000')
cs <= bitarray('10001')
rw <= bitarray('0')
q <= 0
=============================
<<Instrucción: 0110>>

cs <= bitarray('11111')
q <= 3
=============================
<<Instrucción: 0111>>

cs <= bitarray('10110')
rw <= bitarray('1')
q <= 4
=============================
<<Instrucción: 1000>>

datoin <= bitarray('0000')
datoin <= bitarray('0000')
rw <= bitarray('0')
cs <= bitarray('00001')
q <= 2
=============================
<<Instrucción: 1001>>

operacion <= bitarray('0000')
rc <= bitarray('0010')
direccion <= bitarray('00000000')
pcout <= bitarray('00000000')
cs <= bitarray('00001')
q <= 5
=============================
<<Instrucción: 1010>>

cs <= bitarray('10101')
q <= 11
=============================
<<Instrucción: 1011>>

datoin <= bitarray('0000')
datoin <= bitarray('0000')
cs <= bitarray('10001')
rw <= bitarray('0')
q <= 0
=============================
<<Instrucción: 1100>>

cs <= bitarray('11111')
q <= 3
=============================
<<Instrucción: 1101>>

cs <= bitarray('10110')
rw <= bitarray('1')
q <= 4
=============================
<<Instrucción: 1110>>

datoin <= bitarray('0000')
datoin <= bitarray('0000')
rw <= bitarray('0')
cs <= bitarray('00001')
q <= 2
=============================
<<Instrucción: 1111>>

cs <= bitarray('00001')
q <= 5
=============================
```

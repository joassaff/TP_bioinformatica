# Bioinformática 

## Trabajo Práctico

### Integrantes 
- Vacas Castro, Justina                     
- Assaff, Josefina	 
- Mejalelaty, Ian		 
- Gomez, Lucas 

### Requerimientos 
```
Python3 
Clustalw
Muscle
Blast 
```
### Ejercicio 1 – PROCESAMIENTO DE SECUENCIAS
Leer una o múltiples secuencias de nucleótidos de un archivo en formato Genbank (*.gb) y guardaarlas en un archivo FASTA (*.fas). 

Ejemplo de ejecución
```
python3 ./ex1.py sequencesPSEN1.gb
```
### Ejercicio 2 – BLAST
Para realizar un BLAST de una o varias secuencias y escribir el resultado en un archivo.

Ejemplo de ejecución
```
python3 ./ex2.py --input ./orf/NM_000021.4/. --output resultsN --method blastn
python3 ./ex2.py --input ./orf/NM_000021.4/. --output resultsP --method blastp 
```
### Ejercicio 3 – Multiple Sequence Alignment (MSA)
Ejemplo de ejecución
```
python3 ./ex3.py 
```
### Ejercicio 4 – EMBOSS
### Ejercicio 5 
### Ejercicio 6 – Trabajo con Bases de Datos Biológica
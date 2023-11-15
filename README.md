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
python3 ./ex1.py sequencePSEN1.gb
```
### Ejercicio 2 – BLAST
Para realizar un BLAST de una o varias secuencias y escribir el resultado en un archivo.

Ejemplo de ejecución
```
python3 ./ex2.py --input ./orf/NM_000021.4/. --output resultsN --method blastn
python3 ./ex2.py --input ./orf/NM_000021.4/. --output resultsP --method blastp 
```
### Ejercicio 3 – Multiple Sequence Alignment (MSA)
Se cuenta con el script `ex3/create_sequences_file.py` el cual es el encargado de descargar las secuencias y almacenarlas en el archivo `sequences.fasta` de los 10 mejores resultados BLAST. 
Luego, el script `ex3/msa.py` se encarga de realizar el alineamiento multiple de las secuencias descargadas.
Ejemplo de ejecución
```
sh ex3.sh sequence.fas
```
Para ejecutar los scripts por separado
```
python3 create_sequences_file.py --input input_file.fasta
python3 ./msa.py --input sequences.fasta
```
Para visualizar el arbol filogenetico a partir del alineamiento, se debe ejecutar los siguientes comandos:
```
seqmagick convert --output-format phylip multiple_alignment output_alignment.phy
FastTree -nt output_alignment.phy > output_tree.nwk
python3 tree.py
```
### Ejercicio 4 – EMBOSS
El script encuentra ORFs en la secuencia de entrada (a nivel de proteínas o nucleótidos). Luego, realiza un análisis de dominios en las secuencias de aminoácidos obtenidas.
Ejemplo de ejecución
```
python3 ex4.py --input input_file.fas --method={orf_nt, orf_prot}
```
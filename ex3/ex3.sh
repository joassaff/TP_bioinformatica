#!/bin/bash

if [ -z "$1" ]; then
    echo "Error: Se debe proporcionar un archivo de entrada."
    exit 1
fi

input_file="$1"

python3 create_sequences_file.py --input "$input_file"
python3 ./msa.py --input sequences.fasta

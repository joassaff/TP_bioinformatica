import os
import subprocess
import argparse
from Bio import SeqIO
from Bio.Seq import Seq

def blast(target, input_path, output_path):
    if os.path.isfile(input_path):
        target(input_path, output_path)
    elif os.path.isdir(input_path):
        for file in os.listdir(input_path):
            target(os.path.join(input_path, file), output_path)

def online_blastn(input_file, output_folder):
    record = SeqIO.read(input_file, format="fasta")
    result = run_online_blastn(record)
    save_result(result, input_file, output_folder)

def run_online_blastn(record):
    result = None
    try:
        result = blastn("blastn", "nt", record.seq)
    except Exception as e:
        print(f"Error: NCBI Remote blastn failed - {e}")
    return result

def blastn(blast_type, database, sequence):
    from Bio.Blast import NCBIWWW
    return NCBIWWW.qblast(blast_type, database, sequence)

def save_result(result, input_file, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file = os.path.join(output_folder, os.path.basename(input_file).replace('.fasta', '_blast.xml'))

    # Obtener el contenido del objeto StringIO como una cadena de texto
    result_str = result.getvalue()

    # Guardar el resultado en un archivo XML
    with open(output_file, "w") as output:
        output.write(result_str)

def local_blastp(input_file, output_folder):
    record = SeqIO.read(input_file, format="fasta")
    protein_sequence = record.seq.translate(stop_symbol="")
    save_protein_sequence(protein_sequence, input_file, output_folder)

def save_protein_sequence(protein_sequence, input_file, output_folder):
    file_name = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(output_folder, f"{file_name}_protein.fasta")

    os.makedirs(output_folder, exist_ok=True)  # Create the output folder if it doesn't exist

    with open(output_file, "w") as output:
        output.write(f">{file_name}\n{protein_sequence}\n")

def run_local_blastp(query_file, output_folder):
    db_path = "/root/swissprot"
    output_file = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(query_file))[0]}_blast.xml")
    command = f'blastp -query {query_file} -db {db_path} -outfmt 5 -out {output_file}'
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Local BLASTP failed - {e}")

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output",
                        type=str, default="blast_output", required=False)
    parser.add_argument("--method", type=str, default="blastn",
                        required=False, choices=["blastn", "blastp"])

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()

    if args.method == "blastn":
        blast(online_blastn, args.input, args.output)
    elif args.method == "blastp":
        blast(local_blastp, args.input, args.output)
    else:
        print("Please enter a blastp or blastn method")

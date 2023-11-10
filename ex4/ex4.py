import argparse
import subprocess
from enum import Enum
import os

class ORF(Enum):
    PROTEIN = 1
    NUCLEOTIDE = 3


def get_orf(method):
    try:
        subprocess.run(f"getorf -sequence {args.input} \
                    -outseq {args.output}.orf \
                    -find {method.value}", shell=True)
    except Exception:
        print("Error: Failed to excute getorf emboss command.")
        exit(1)


def run_emboss_patmatdb(input_proteins, output_domains):
    prosite_database_path = "/ruta/completa/al/nuevo_prosite.dat"
    os.environ["PROSITE_DATABASE"] = prosite_database_path

    subprocess.run(f"patmatdb -sequence {input_proteins} -outfile {output_domains}", shell=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="ej4.py")
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, default="sequence", required=False)
    parser.add_argument("--method", type=str, required=True, choices=["orf_prot", "orf_nt"])

    args = parser.parse_args()

    if args.method == "orf_prot":
        get_orf(ORF.PROTEIN)
    if args.method == "orf_nt":
        get_orf(ORF.NUCLEOTIDE)

    run_emboss_patmatdb(args.input, "output.patmatdb")

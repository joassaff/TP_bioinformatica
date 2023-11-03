import os
import sys
from Bio import SeqIO
#jujis


def search_codon(seq_record, start, codons):
    return next((i for i in range(start, len(seq_record), 3) if seq_record[i:i + 3] in codons), -1)


def find_with_start_codon(seq_record):
    start = 0
    start_codon = ["ATG"]
    start = next((i for i in range(start, len(seq_record), 3) if seq_record[i:i + 3] in start_codon), -1)
    if start == -1:
        return ""

    stop_codons = ["TAA", "TAG", "TGA"]
    end = next((i for i in range(start, len(seq_record), 3) if seq_record[i:i + 3] in stop_codons), -1) + 3

    if end != -1:
        return seq_record[start:end]


def search_orfs(sequence):
    ORFS = []
    for seq in [sequence, sequence[::-1]]:
        for i in range(3):
            ORFS.append(find_with_start_codon(seq[i:]))
    return ORFS


def process_genbank(input_file):
    output_folder = os.path.join(os.getcwd(), 'ORF')
    records = SeqIO.parse(input_file, "genbank")

    for record in records:
        sequence = str(record.seq)
        orfs = search_orfs(sequence)
        if not orfs:
            print("No ORFs")
            exit()

        dir = f"{output_folder}/{record.id}/"
        os.makedirs(dir, exist_ok=True)

        for i, orf in enumerate(orfs):
            with open(f"{dir}ORF{i+1}_L{len(orf)}.fas", "w") as f:
                f.write(f"{i+1} length {len(orf)}\n")
                f.write(orf)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py input_file.gbk")
        sys.exit(1)

    process_genbank(sys.argv[1])


import os
import argparse
from Bio.Blast import NCBIXML
from Bio import Entrez, SeqIO
Entrez.email = "lugomez@itba.edu.ar"


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str,
                        default="sequences.fasta", required=False)

    return parser.parse_args()


def get_sequences(xml_file, num_sequences=10):
    blast_record = list(NCBIXML.parse(open(xml_file)))[0]
    sequences = []

    print("> Sorting sequences...")
    sorted_alignments = sorted(
            blast_record.alignments,
            key=lambda alignment: min(hsp.expect for hsp in alignment.hsps)
    )
    top_alignments = sorted_alignments[:num_sequences]

    print("> Downloading sequences...")
    for alignment in top_alignments:
        accession = alignment.accession
        sequence = fetch_sequence_from_genbank(accession)
        if sequence:
            sequences.append((accession, sequence))
    return sequences


def fetch_sequence_from_genbank(accession):
    try:
        handle = Entrez.efetch(
            db="nucleotide",
            id=accession,
            rettype="gb",
            retmode="text")
        record = SeqIO.read(handle, "genbank")
        handle.close()
        return record
    except Exception as e:
        print(f"Error fetching sequence: {e}")
        return None


def create_fasta(selected_sequences, gb_file):
    print("> Creating .fasta file...")
    with open("sequences.fasta", "w") as fasta_file:
        gb_record = next(SeqIO.parse(gb_file, "genbank"))
        fasta_file.write(f">{gb_record.id} {gb_record.description}\n")
        fasta_file.write(f"{gb_record.seq}\n")
        for accession, sequence in selected_sequences:
            seq = str(sequence.seq)
            fasta_file.write(f">{accession}\n")
            fasta_file.write(f"{seq}\n")


if __name__ == "__main__":
    args = parse_arguments()
    in_file = args.input
    out_file = args.output
    xml_file = f"../resultsN/{os.path.basename(in_file)}"
    if not os.path.exists(xml_file):
        print(f"Error: XML file '{xml_file}' does not exist.")
        exit(1)
    sequences = get_sequences(xml_file)
    if not sequences:
        print("Error: Not sequences were found.")
        exit(1)
    create_fasta(sequences, "../sequencePSEN1.gb")

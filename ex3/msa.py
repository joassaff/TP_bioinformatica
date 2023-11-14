import argparse
import subprocess
from Bio.Application import ApplicationError


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str,
                        default="multiple_alignment", required=False)

    return parser.parse_args()


def run_muscle(in_file, out_file):
    subprocess.run(
        ["muscle", "-align", in_file, "-output", out_file],
        check=True
    )


if __name__ == "__main__":
    args = parse_arguments()
    in_file = args.input
    out_file = args.output

    try:
        run_muscle(in_file, out_file)
    except ApplicationError:
        print("Error: Unable to run MSA.")
        exit(1)
    except OSError as e:
        print(f"Error: Unable to open {in_file}: {e}")
        exit(1)

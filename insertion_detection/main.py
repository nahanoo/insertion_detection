import argparse
from .insertion_detection import Insertion

def parse_args():
    parser = argparse.ArgumentParser(
        description='Detect insertions in evolved bacterial strains.')
    parser.add_argument(
        'ancestral', help='fasta file of the ancestral strain'
    )
    parser.add_argument(
        'mutant', help='genbank file of the mutated strain')
    parser.add_argument('out_dir', help='output directory')
    parser.add_argument('--plot', help='if this flag is added the alignment of every insertion\
        is plotted', action='store_true')

    return parser.parse_args()

def main():
    args = parse_args()
    i = Insertion(args)
    i.chunk_assembly()
    i.mapper()
    i.get_insertions()
    i.annotate()
    i.dump()
    if args.plot:
        i.plot_insertions()
        i.plot_annotation()
    i.clean()
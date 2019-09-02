from synbiolib import codon
import itertools

## Setup dictionaries
#DNA = ['A', 'T', 'G', 'C']
#for block in [''.join(i) for i in itertools.product(DNA, repeat = 5)]:
#    print(block)

forward_attachment = "AGATGGCTCTTCT"
reverse_attachment = "TGAAGAGCCACGG"

def block_to_oligo(block_seq):
    for_primer = forward_attachment + block_seq + reverse_attachment
    rev_primer = codon.reverse_complement(for_primer)
    return (for_primer, rev_primer)

def oligo_to_block(oligo_seq):
    if forward_attachment in oligo_seq:
        block = oligo_seq[len(forward_attachment)-1:len(forward_attachment)+4]
    elif codon.reverse_complement(forward_attachment):
        block = oligo[len(reverse_attachment)-1:len(reverse_attachment)+4]
    else:
        block = "NOT_BLOCK"
    return block

def sequence_to_block(seq):
    seq = "GCC" + seq + "CAG"
    def next_base(seq, block_list):
        if len(seq[0:5]) < 5:
            return block_list
        block_list.append(seq[0:5])
        return next_base(seq[3:], block_list)
    return next_base(seq, [])

def find_repeat_overlap(overlap_list):
    repeats = []
    for overlap,repeat in dict(Counter(overlap_list)).items():
        if repeat > 1:
            repeats.append(overlap)
    return repeats
find_repeat_overlap(sequence_to_block(string))

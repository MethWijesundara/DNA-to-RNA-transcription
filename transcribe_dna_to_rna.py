def transcribe(dna_sequence):
    complement = {
        'A' : 'U',
        'T' : 'A',
        'C' : 'G',
        'G' : 'C'
    }

    rna = ''.join(complement[base] for base in dna_sequence.upper())
    return rna

in1 = "ATCG"
in2 = "GATTACA"
in3 = "agct"

out1 = transcribe(in1)
out2 = transcribe(in2)
out3 = transcribe(in3)


print(f"DNA: {in1} -> RNA: {out1} ")
print(f"DNA: {in2} -> RNA: {out2} ")
print(f"DNA: {in3} -> RNA: {out3}")


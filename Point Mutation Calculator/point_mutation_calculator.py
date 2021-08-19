
hamming = 0 #hamming distance value
seq1 = input("Enter the first sequence:\n")
seq2 = input("Enter the second sequence:\n")

if len(seq1) == len(seq2):
    """Checks whether the two sequences are of identical lengths"""

    for i in range(0, len(seq1), 1):
        """Compares the two sequences nucleotide by nucleotide"""
        
        nucleotide_1 = seq1[i]
        nucleotide_2 = seq2[i]

        if nucleotide_1 in ("A") and nucleotide_2 in ("G", "C", "T"): #hamming value increases if non-identical nucleotides are paired
            hamming += 1

        elif nucleotide_1 in ("T") and nucleotide_2 in ("G", "C", "A"):
            hamming += 1

        elif nucleotide_1 in ("G") and nucleotide_2 in ("A", "T", "C"):
            hamming += 1

        elif nucleotide_1 in ("C") and nucleotide_2 in ("A", "T", "G"):
            hamming += 1
        
    print(f"The Hamming distance is: {hamming}")

else:
    print("The two sequences are different lengths")





































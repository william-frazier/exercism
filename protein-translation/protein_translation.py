

def proteins(strand):
    amino_acids = []
    mapping = {"AUG": "Methionine","UUU": "Phenylalanine", "UUC": "Phenylalanine", "UUA": "Leucine", "UUG": "Leucine", "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine", "UAU": "Tyrosine", "UAC": "Tyrosine", "UGU": "Cysteine", "UGC": "Cysteine", "UGG":	"Tryptophan", "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"}
    if len(strand) % 3 != 0:
        raise Exception("The strand must be a multiple of 3 proteins long.")
    i = 0
    while i < len(strand):
        triplet = strand[i:i+3]
        print(triplet)
        if triplet in mapping:
            amino_acid = mapping[triplet]
            if amino_acid == "STOP":
                return amino_acids
            amino_acids.append(amino_acid)
        i += 3
    return amino_acids

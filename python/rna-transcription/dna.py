from string import maketrans

def to_rna(inp):
    return inp.translate(maketrans("GCTA","CGAU"))

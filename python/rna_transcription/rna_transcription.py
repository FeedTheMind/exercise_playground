def to_rna(DNA):
    '''Converts a DNA strand to its
    RNA complement

    Args:
        DNA = string 
    Returns:
        RNA complement
    '''
    trans = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    
    # Comment out this block of code if you want question
    # marks (?) to substitute incorrect characters
    for char in DNA:
        if char not in 'GTCA':
            return '' 

    return ''.join(trans.get(char) if char in 'GTCA' else '?' for char in DNA)

    
print('ACGTGGTCTTAA . . . ', to_rna('ACGTGGTCTTAA'))
print('XACGTXGGTCTX . . . ', to_rna('XACGTXGGTCTX'))

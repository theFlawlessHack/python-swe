def cigar_party(cigars, is_weekend):
    '''When squirrels get together for a party, they like to have cigars.
    A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.
    Unless it is the weekend, in which case there is no upper bound on the number of cigars.
    Returns True if the party with the given values is successful, or False otherwise. '''
    if is_weekend == True:
        if cigars >= 40:
            return True
        else:
            return False
    else:
        if 40 <= cigars <= 60:
            return True
        else:
            return False

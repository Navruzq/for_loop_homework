def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    i=0
    
    while i<n:
        print('"',i,end=',')
        i+=1
    return '"'

print(main(3))
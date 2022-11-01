def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    s=0
    
    while A<B:
        s+=A
        A+=1
    return s
print(main(3,6))

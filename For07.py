def main(N):
    """
    Return the sum of odd numbers from zero to N.
    Args:
        N: int
    Returns:
        int: return  answer
    """
    s=0
    i=0
    while i<N:
        if i%2==1:
           s+=i
        i+=1
    return s
print(main(12))
def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    i=0
    a=n-1
    while i<a:
        print(i,end=',')
        i+=1
    return a

print(main(3))